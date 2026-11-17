import ast
from pathlib import Path
import unittest

tree = ast.parse(Path(__file__).with_name('promote_daily.py').read_text())
scope = {}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'validate_rows'], type_ignores=[]), '<promotion-validation>', 'exec'), scope)
validate = scope['validate_rows']

class Validation(unittest.TestCase):
    def test_metadata_only(self):
        validate([{'path': 'a', 'discovered': 'old'}], [{'path': 'a', 'discovered': 'old', 'daily_presence': {'signal': 'observed'}}])

    def test_history_protection(self):
        with self.assertRaises(ValueError):
            validate([{'path': 'a', 'discovered': 'old'}], [{'path': 'a', 'discovered': 'new'}])

    def test_removal(self):
        with self.assertRaises(ValueError):
            validate([{'path': 'a'}], [])

    def test_new_access(self):
        with self.assertRaises(ValueError):
            validate([], [{'path': 'a', 'content_read_allowed': True}])

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            validate([], [{'path': 'a'}, {'path': 'a'}])

if __name__ == '__main__':
    unittest.main()
