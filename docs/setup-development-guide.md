# Setup & Development Guide

Complete guide for setting up and contributing to the **ml-ajourhold** project.

**Table of Contents**
- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
- [IDE Configuration](#ide-configuration)
- [Development Workflow](#development-workflow)
- [Docker Configurations](#docker-configurations)
- [GitHub Repository Setup](#github-repository-setup)

## Prerequisites

<details>
<summary><b>Required Tools</b></summary>

- [Git](https://git-scm.com/) and [GitHub](https://github.com/) account
- [GitHub CLI](https://cli.github.com/) (optional but recommended)

**For Devcontainer setup (Method 1):**
- [Docker](https://docs.docker.com/engine/install/)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**For local setup (Methods 2-3):**
- [uv](https://docs.astral.sh/uv/installation/) Python package manager
- [Task](https://taskfile.dev/installation/) (for Method 2)

</details>

### Clone the Repository

```bash
# Using GitHub CLI
gh repo clone miljodirektoratet/ml-ajourhold
cd ml-ajourhold

# Or using git directly
git clone https://github.com/miljodirektoratet/ml-ajourhold.git
cd ml-ajourhold
```

## Installation Methods

### Method 1: Devcontainer (Recommended)

**Best for:** Consistent development environment across team members.

1. **Open in VS Code**:
   - Open the cloned folder in VS Code
   - Or use [GitHub Codespaces](https://github.com/features/codespaces)

2. **Start Devcontainer**:
   - Click "Reopen in Container" when prompted
   - Or: `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"

3. **Automatic Setup**: The devcontainer will:
   - Install dev tools (Git, uv, Task, pre-commit)
   - Set up Python environment with dependencies
   - Configure VS Code extensions and settings
   - Run `task dev-setup` for initial checks

4. **Verify Installation**:

   Open `notebooks/demo.ipynb`, select the `ml-ajourhold` kernel, and run the notebook to ensure everything is working correctly. If you have problems activating the `ml-ajourhold` python environment refer to the [setup guide](./docs/setup-guide.md).

   Test the package in terminal:
   ```bash
   task run
   # → "Hello from ml-ajourhold!"
   # → "Version: x.x.x"
   ```

5. **Next Steps**: Continue to [Development Workflow](#development-workflow)

### Method 2: Local Setup with Task

**Best for:** Automated local setup with Task commands where Docker is not available.

1. **Install Task**: Follow [Task installation guide](https://taskfile.dev/installation/)

2. **Run Setup**:

    Set up Python environment, install dependencies, and run initial checks with `task dev-setup` command from the terminal.

    This command:
    - Installs Python dependencies with `uv sync --dev`
    - Sets up pre-commit hooks
    - Runs code quality checks
    - Installs package in development mode

3. **Verify Installation**:

   Open `notebooks/demo.ipynb`, select the `ml-ajourhold` kernel, and run the notebook to ensure everything is working correctly. If you have problems activating the `ml-ajourhold` python environment refer to the [setup guide](./docs/setup-guide.md).

   Test the package in terminal:
   ```bash
   task run
   # → "Hello from ml-ajourhold!"
   # → "Version: x.x.x"
   ```

4. **Configure IDE**: See [IDE Configuration](#ide-configuration)

5. **Next Steps**: Continue to [Development Workflow](#development-workflow)

### Method 3: Local Setup without Task

**Best for:** Local setup where Docker and Task are not available, but uv is installed.

1. **Create Virtual Environment**:

    Set up the uv environment from the `pyproject.toml` and `uv.lock` files.

   ```bash
    # Navigate to your cloned repository
    cd ml-ajourhold

    # Create .venv with dev dependencies
    uv sync --dev
   ```

2. **Verify Installation**:

   Open `notebooks/demo.ipynb`, select the `ml-ajourhold` kernel, and run the notebook to ensure everything is working correctly. If you have problems activating the `ml-ajourhold` python environment refer to the [setup guide](./docs/setup-guide.md).

   Test the package in terminal:
   ```bash
   uv run ml-ajourhold
   # → "Hello from ml-ajourhold!"
   # → "Version: x.x.x"
   ```

3. **Configure IDE**: See [IDE Configuration](#ide-configuration)

4. **Next Steps**: Continue to [Development Workflow](#development-workflow)

## IDE Configuration

### VS Code Setup

The project includes VS Code configuration in `.vscode/` or in the `.devcontainer.json` for the devcontainer setup.

1. **Install Extensions**: Accept prompt to install recommended extensions
2. **Select Python Interpreter**:
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Choose `./.venv/bin/python`

3. **Jupyter Notebooks**:
   - Open `notebooks/demo.ipynb`
   - Select `.venv` kernel when prompted

### Terminal Activation

```bash
# Activate virtual environment in terminal
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Verify
which python
python --version
```

## Development Workflow

### 1. Create a Branch

```bash
# Feature branch
git checkout -b feat/your-feature-name

# Bug fix branch
git checkout -b fix/bug-description
```

### 2. Develop

Make changes in `src/`, `notebooks/`, or `scripts/`.

**Key Commands**:

```bash
# Run the package
task run

# Run quality checks
task check

# Run tests with coverage
task test

# Format code
task format

# Run complete CI locally
task ci-local
```

See [Command Cheatsheet](./command-cheatsheet.md) for all available commands.

### 3. Test & Validate

Before pushing:

```bash
# Run all checks locally
task ci-local

# Ensure pre-commit hooks pass
pre-commit run --all-files
```

#### Managing Pre-commit Hooks

Pre-commit hooks automatically run on every commit to ensure code quality. However, they can make commits slower since they run multiple checks (ruff, mypy, formatting, etc.).

<details>
<summary><b>Skip Pre-commit Hooks (Quick Commits)</b></summary>

**Skip all hooks temporarily:**
```bash
git commit --no-verify -m "<commit message>"
# or shorthand:
git commit -n -m "<commit message>"
```

</details>

<details>
<summary><b>Run Specific Hooks Only</b></summary>

```bash
# Run only specific hooks
pre-commit run ruff --all-files
pre-commit run trailing-whitespace --all-files

# List all available hooks
pre-commit run --all-files --verbose
```
</details>

<details>
<summary><b>Speed Up Pre-commit</b></summary>

**Option 1: Disable hooks for individual commits**
```bash
git commit -n -m "WIP"  # Skip hooks during development
```

Then before pushing:
```bash
pre-commit run --all-files  # Run all checks once
```

**Option 2: Uninstall pre-commit hooks entirely**
```bash
pre-commit uninstall  # Remove git hooks
```

Manually run checks before creating PRs:
```bash
task check      # Quick checks
task ci-local   # Full CI suite
```

**Option 3: Re-enable when needed**
```bash
pre-commit install  # Reinstall hooks
```

</details>

> [!TIP]
> **Recommended Workflow:**
> - Use `git commit -n` for frequent WIP commits during active development
> - Run `task check` periodically to catch issues early
> - Always run `task ci-local` before creating a pull request

### 4. Integrate

1. Push your branch to GitHub
2. Create a Pull Request to `main`
3. Await CI checks and code review
4. Merge (branch auto-deletes after merge)

### 5. Deploy (Maintainers Only)

**Step 1: Create Release and Deploy**

```bash
# Create release branch, tag, trigger deployment, and open PR
task release VERSION=v1.0.0
```

This command:
1. Creates release branch `release/v1.0.0`
2. Pushes the branch to origin
3. Tags the release branch with `v1.0.0`
4. Pushes the tag (triggers CD workflows)
5. Opens PR from `release/v1.0.0` to `main`

**Step 2: Monitor Deployment**

Check GitHub Actions to monitor:
- **CD Python**: Publishes to GitHub Releases
- **CD Docker**: Pushes to GitHub Container Registry

**Step 3: Merge PR**

If deployment succeeds:
1. Review the auto-created PR
2. Merge to `main`
3. Release branch auto-deletes

If deployment fails:
1. Fix issues on release branch
2. Delete old tag: `git tag -d v1.0.0 && git push origin :refs/tags/v1.0.0`
3. Re-tag: `git tag v1.0.0 && git push origin v1.0.0`
4. Monitor CD workflows again

**Revert a Release**:

*Before merge to main:*

```bash
# Delete tag (stops/prevents deployment)
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0

# Delete release branch
git checkout main
git branch -D release/v1.0.0
git push origin --delete release/v1.0.0
```

*After deployment:*

> [!WARNING]
> Deleting a tag after deployment won't unpublish packages. You'll need to:
> - Manually remove/yank from Test PyPI
> - Delete container images from GHCR
> - Or publish a new version to supersede it

### 6. Clean Up

```bash
# Clean dev artifacts
task clean

# Clean up local git
git config --global fetch.prune true
git branch -d <branch-name>
```

## Docker Configurations

The project uses Docker for development, testing, and deployment:

### Development Container

- **File**: `.devcontainer/devcontainer.json`
- **Use**: VS Code Dev Containers & GitHub Codespaces
- **Features**: Auto-installs tools, configures environment

### Testing Container

- **File**: `docker-compose.yml`
- **Use**: Local testing in production-like environment

```bash
docker-compose up --build
```

### Production Container

- **File**: `Dockerfile`
- **Use**: Production deployments
- **Published**: [GitHub Container Registry](https://github.com/miljodirektoratet/ml-ajourhold/pkgs/container/ml-ajourhold)

```bash
# Pull and run
docker pull ghcr.io/miljodirektoratet/ml-ajourhold:latest
docker run --rm ghcr.io/miljodirektoratet/ml-ajourhold:latest
```

## GitHub Repository Setup

If you fork this repository or create a new one, configure the following:

### Required Secrets

Add to **Settings** > **Secrets and variables** > **Actions**:

| Secret | Purpose | Get From |
|--------|---------|----------|
| `CODECOV_TOKEN` | Code coverage reporting | [Codecov](https://codecov.io/) |

### Test PyPI Publishing

**Note:** This project now publishes to GitHub Releases instead of PyPI. The sections below are kept for reference if you want to configure PyPI publishing.

<details>
<summary>PyPI Configuration (Optional)</summary>

1. **Create Test PyPI Account**: [test.pypi.org](https://test.pypi.org/)

2. **Create GitHub Environment**:
   - Go to **Settings** > **Environments** > **New environment**
   - Name: `testpypi`

3. **Configure Trusted Publisher** on Test PyPI:
   - Navigate to **Account settings** > **Publishing**
   - Add new pending publisher:
     - Owner: `miljodirektoratet`
     - Repository: `ml-ajourhold`
     - Workflow: `cd-python.yml`
     - Environment: `testpypi`

</details>

### Security & Code Quality

Verify in **Settings**:

- ✅ **Code security and analysis** > Dependency graph: Enabled
- ✅ **Code security and analysis** > Dependabot alerts: Enabled
- ✅ **Code security and analysis** > Dependabot security updates: Enabled
- ✅ **Code security and analysis** > Code scanning: Enabled
- ✅ **Code security and analysis** > Secret scanning: Enabled

### GitHub Actions (GHA) Workflows

The repository includes automated workflows:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| **CI Python** | `push`, `pull_request` to `main` | Code quality, testing, coverage |
| **CD Python** | `push` to `main` with version tags | Deploy to GitHub Releases |
| **CI Docker** | `push`, `pull_request` to `main` | Build and test Docker image |
| **CD Docker** | `push` to `main` with version tags | Deploy to GitHub Registry |
| **CodeQL Analysis** | `push`, `pull_request`, `schedule` | Security analysis |

### Branch Protection

On the `main` branch:

- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging

### GitHub Copilot

Configuration for GitHub Copilot is included in [copilot-instructions.md](./.github/copilot-instructions.md) to assist developers in adhering to code quality and security standards while coding.

---

**Need Help?** See the [Troubleshooting Guide](./troubleshooting.md) or [Command Cheatsheet](./command-cheatsheet.md).
