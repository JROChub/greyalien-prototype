# Release Checklist

Use this checklist to cut a new release.

1. Update `CHANGELOG.md`
   - Move items from "Unreleased" into a new version section.
2. Bump version number
   - `pyproject.toml`
3. Run CI checks locally
   - `make ci`
4. Confirm CodeQL and SBOM workflows are green
5. Tag the release
   - `git tag vX.Y.Z`
   - `git push origin vX.Y.Z`
6. Publish package (optional for prototype builds)
   - Run the GitHub Actions "Publish" workflow for TestPyPI first.
   - If green, rerun for PyPI.
7. Create a GitHub release
   - Use the changelog entry as the release notes.
