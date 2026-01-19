# Release Checklist

Use this checklist to cut a new release.

1. Update `CHANGELOG.md`
   - Move items from "Unreleased" into a new version section.
2. Bump version number
   - `pyproject.toml`
3. Run CI checks locally
   - `make ci`
4. Confirm CodeQL and SBOM workflows are green
5. Confirm trusted publishing is configured
   - PyPI/TestPyPI should trust this repo for environments `pypi` and `testpypi`.
6. Run the GitHub Actions "Release" workflow
   - Provide a tag like `vX.Y.Z` that matches `pyproject.toml`.
   - Choose TestPyPI or PyPI and optional prerelease flag.
7. Verify the GitHub release assets and PyPI/TestPyPI upload
