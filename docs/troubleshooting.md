# Troubleshooting

This guide helps you diagnose and resolve common issues when working with uv-demo.

## Quick Diagnostics

Run these commands to gather information about your setup:

```bash
# Check tool versions
uv --version
uv python pin --resolved # Python version of current .venv

# Check project status
uv run python -m setuptools_scm  # Current package version
task check                       # Overall project health

# Check environment
uv run python -c "import sys; print(sys.path)"
ls -la .venv/  # Virtual environment exists

# Restart VS Code
# CTRL+SHIFT+P → "Reload Window"
```

## Development Environment Issues

### VS Code not detecting Python environment

**Problem**: VS Code uses wrong Python interpreter

**Solutions**:

1. **Command Palette** (`Ctrl+Shift+P`)
2. Type "Python: Select Interpreter"
3. Choose `./.venv/bin/python` (Linux/macOS) or `.\.venv\Scripts\python.exe` (Windows)


### Import errors in notebooks

**Problem**: Cannot import ml_ajourhold in Jupyter notebooks

**Solutions**:

```bash
# Install package in development mode
uv pip install -e .

# Ensure ipykernel is installed
uv add --group dev "ipykernel>=6.29.5"

# Restart Jupyter kernel
# In notebook: Kernel → Restart Kernel

# Check kernel in VS Code
# Select .venv kernel when opening notebook
```

### Slow commits

**Problem**: `git commit` takes a long time to complete

**Cause**: Pre-commit hooks run multiple checks on every commit (ruff, mypy, formatting, notebook linting, etc.)

**Solutions**:

**Quick fix - Skip hooks for WIP commits:**
```bash
git commit --no-verify -m "WIP: work in progress"
# or shorthand:
git commit -n -m "WIP: work in progress"
```

**Long-term options:**
```bash
# Option 1: Run hooks manually instead of on every commit
pre-commit uninstall

# Then run checks before creating PRs:
task check
task ci-local

# Option 2: Skip only slow hooks (e.g., mypy)
SKIP=mypy git commit -m "your message"

# Option 3: Re-enable hooks when needed
pre-commit install
```

### Deployment failures

**Problem**: Package deployment to Test PyPI fails

**Common Issues**:

**Trusted publishing not configured**:

1. Go to [Test PyPI trusted publishers](https://test.pypi.org/manage/account/publishing/)
2. Add repository: `miljodirektoratet/ml-ajourhold`
3. Workflow name: `cd-python.yml`

**Version conflicts**:

Only "clean" version tags can be deployed, development tags (e.g., `0.1.0.dev0+<commit>`) are not allowed. Ensure no existing release with the same version exists and that the version follows semantic versioning.

```bash
# Check existing versions on Test PyPI

# Check current version
uv run python -m setuptools_scm

# Create new "clean" version tag
git tag vx.y.z
git push origin vx.y.z
```
