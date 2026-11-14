const fs = require('fs');
const path = require('path');
const vault = path.resolve(__dirname, '../..');
const results = [];
for (const input of process.argv.slice(2)) {
  const file = path.resolve(vault, input);
  if (!file.startsWith(vault + path.sep)) throw new Error('Outside vault');
  const text = fs.readFileSync(file, 'utf8');
  const ids = new Set([...text.matchAll(/<a id="([^"]+)"/g)].map(x => x[1]));
  const headings = new Set([...text.matchAll(/^#{1,6}\s+(.+)$/gm)].map(x => x[1]));
  const broken = [];
  let outside = 0;
  const links = [...text.matchAll(/\]\((?:<([^>]+)>|([^\s)]+))\)/g)].map(x => x[1] || x[2]);
  for (const link of links) {
    if (link.startsWith('#')) {
      if (!ids.has(link.slice(1)) && !headings.has(link.slice(1))) broken.push(link);
      continue;
    }
    if (/^[a-z]+:\/\//i.test(link)) { outside++; continue; }
    const target = path.resolve(path.dirname(file), link.replace(/:\d+$/, '').split('#')[0]);
    if (!target.startsWith(vault + path.sep)) { outside++; continue; }
    if (!fs.existsSync(target)) broken.push(link);
  }
  results.push({file: input, markdown_links: links.length, broken,
    external_references_not_checked: outside});
}
console.log(JSON.stringify(results, null, 2));
if (results.some(x => x.broken.length)) process.exitCode = 1;
