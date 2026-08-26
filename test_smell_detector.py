import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class TestSmellDetector(unittest.TestCase):
    def run_detector(self, file_path):
        result = subprocess.run(
            [sys.executable, "src/smell_detector.py", file_path],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout

    def test_sample_code_detects_smells(self):
        output = self.run_detector("src/samples/sample_code.py")

        self.assertIn("Long parameter list", output)
        self.assertIn("Long method", output)
        self.assertIn("Large class", output)
        self.assertIn("Deep nesting", output)
        self.assertIn("Duplicate code", output)
        self.assertIn("Feature envy", output)

    def test_clean_ast_parser_has_no_smells(self):
        output = self.run_detector("src/ast_parser.py")

        self.assertEqual("", output)


if __name__ == "__main__":
    unittest.main()