import contextlib
import io
from pathlib import Path
import unittest

from roc import cli


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"
EXPECTED_DIR = EXAMPLES_DIR / "expected"


class ExampleOutputTests(unittest.TestCase):
  def test_examples_match_expected_output(self):
    example_paths = sorted(EXAMPLES_DIR.glob("*.roc"))
    self.assertTrue(example_paths, "No examples found")

    for example_path in example_paths:
      expected_path = EXPECTED_DIR / (example_path.stem + ".out")
      self.assertTrue(
        expected_path.exists(),
        f"Missing expected output for {example_path.name}",
      )

      buf = io.StringIO()
      with contextlib.redirect_stdout(buf):
        exit_code = cli.run_path(str(example_path))

      output = buf.getvalue().replace("\r\n", "\n").rstrip()
      expected = expected_path.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()

      self.assertEqual(exit_code, 0, f"Example failed: {example_path.name}")
      self.assertEqual(output, expected, f"Output mismatch: {example_path.name}")


if __name__ == "__main__":
  unittest.main()
