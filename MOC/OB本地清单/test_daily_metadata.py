"""Test pure scan rules without importing/executing the source scanner."""
import ast
from pathlib import Path
import unittest

tree = ast.parse(Path(__file__).with_name('daily_metadata.py').read_text())
functions = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in {'decision', 'hard_boundary', 'compare_metadata'}], type_ignores=[])
scope = {}
exec(compile(functions, '<scan-rules>', 'exec'), scope)

class Rules(unittest.TestCase):
    def compare(self, old, new):
        return scope['compare_metadata'](old, new)

    def test_exact(self):
        r = {'kind': 'file', 'size': 9, 'mtime_ns': '1794703145607928035'}
        self.assertEqual(self.compare(r, r), 'metadata_unchanged')

    def test_missing_size(self):
        self.assertEqual(self.compare({'mtime_ns': '10'}, {'kind': 'file', 'size': 9, 'mtime_ns': '10'}), 'incomplete_metadata_baseline')

    def test_invalid_ns(self):
        self.assertEqual(self.compare({'size': 9, 'mtime_ns': 'invalid'}, {'kind': 'file', 'size': 9, 'mtime_ns': '10'}), 'invalid_metadata_baseline')

    def test_type_change(self):
        self.assertEqual(self.compare({'kind': 'file'}, {'kind': 'link'}), 'kind_changed')

    def test_size_change(self):
        self.assertEqual(self.compare({'size': 8, 'mtime_ns': '10'}, {'kind': 'file', 'size': 9, 'mtime_ns': '10'}), 'metadata_changed')

    def test_precision(self):
        self.assertEqual(self.compare({'size': 9, 'mtime_ns': 1000}, {'kind': 'file', 'size': 9, 'mtime_ns': '1001'}), 'legacy_timestamp_precision_uncertain')

    def test_exact_string_difference(self):
        self.assertEqual(self.compare({'size': 9, 'mtime_ns': '1000'}, {'kind': 'file', 'size': 9, 'mtime_ns': '1001'}), 'metadata_changed')

    def test_review_precedence(self):
        self.assertEqual(scope['decision']({'decision': '保留筛类型', 'admission_review': {'decision': '限定准入'}, 'reassessment_review': {'new_status': '敏感隔离'}}), '敏感隔离')

    def test_protective_reconciliation(self):
        self.assertTrue(scope['hard_boundary']({'decision': '限定准入', 'daily_admission_reconciliation': {'status': '敏感隔离'}}))

if __name__ == '__main__':
    unittest.main()
