import unittest

import roc


class VersionTests(unittest.TestCase):
    def test_resolve_version_fallback(self):
        original_version = roc.version
        try:

            def _raise(_name: str) -> str:
                raise roc.PackageNotFoundError

            roc.version = _raise
            self.assertEqual(roc._resolve_version(), "0.0.0+local")
        finally:
            roc.version = original_version

    def test_resolve_version_success(self):
        original_version = roc.version
        try:
            roc.version = lambda _name: "1.2.3"
            self.assertEqual(roc._resolve_version(), "1.2.3")
        finally:
            roc.version = original_version


if __name__ == "__main__":
    unittest.main()
