# ml-ajourhold

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TestPyPI](https://img.shields.io/badge/TestPyPI-latest-blue)](https://test.pypi.org/project/ml-ajourhold/) [![Coverage](https://codecov.io/gh/miljodirektoratet/ml-ajourhold/branch/main/graph/badge.svg)](https://codecov.io/gh/miljodirektoratet/ml-ajourhold)

**Table of Contents**

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Development](#development)
- [Acknowledgements](#acknowledgements)

## Project Overview

A Python project for detecting landcover changes using machine learning. It identifies landscape modifications that are not yet reflected in national geospatial datasets, such as newly built infrastructure.
- **Do you want to use this package in your project?**
-->  Check out the [Installation](#installation) section.
- **Are you interested in contributing to the project?**
--> Check out the [Development](#development) section for setup instructions, development workflow and contribution guidelines.

### Key Features

- ...
- ...

### Repository Structure

Full overview of the repository structure is available in the [Repository Structure](./docs/repo-structure.md) documentation.

| File / Directory            | Purpose                             |
|---------------------------|-------------------------------------|
| `src/ml_ajourhold`        | Python package source code          |
| `notebooks`               | Jupyter notebooks demonstrating usage of the package and typical workflows |
| `scripts`                 | Standalone scripts for specific tasks or utilities |
| `pyproject.toml`          | Python package configuration, dependencies, and build settings |

### Workflow Statuses

Status badges for the CI/CD workflows, for full details on the GitHub Action workflows and their purposes, see the [Setup & Development Guide](./docs/setup-development-guide.md). Results of the security scans are visible in the [Security](https://github.com/miljodirektoratet/ml-ajourhold/security/code-scanning) tab of the GitHub repository.

| Job | Status | Description |
|---|---|---|
| **CI Python** | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/ml-ajourhold/ci-python.yml?branch=main&label=&style=flat) | Code quality checks, testing, coverage |
| **CD Python** | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/ml-ajourhold/cd-python.yml?label=&style=flat) | Package deployment to Test PyPI |
| **CI Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/ml-ajourhold/ci-docker.yml?branch=main&label=&style=flat) | Build and test Docker image |
| **CD Docker** | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/ml-ajourhold/cd-docker.yml?label=&style=flat) | Container deployment to GitHub Registry |



## Installation

The **ml-ajourhold** project is packaged and published to PyPI. You can install this package from [Test PyPI](https://test.pypi.org/project/ml-ajourhold/) or pull the containerized version from [GHCR](https://github.com/miljodirektoratet/ml-ajourhold/pkgs/container/ml-ajourhold).

> [!NOTE]
> This package is published to Test PyPI for demonstration purposes. Test PyPI is a testing environment for package deployment without affecting the official PyPI index. If you're using this package in production, ensure it's published to the official PyPI index.

Install the package from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ml-ajourhold
```

```python
import ml_ajourhold
ml_ajourhold.main()
# > Hello from ml-ajourhold!
# > Version: x.x.x
```

Or pull and run the container:

```bash
docker pull ghcr.io/miljodirektoratet/ml-ajourhold:latest

docker run --rm ghcr.io/miljodirektoratet/ml-ajourhold:latest
# > Hello from ml-ajourhold!
# > Version: x.x.x
```

## Development

> [!TIP]
> **Recommended Setup:** Use [GitHub Codespaces](https://github.com/features/codespaces) or [VS Code Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) for a consistent environment. Alternative option is to install the project locally using uv.

The following steps configure your development environment using **VS Code Dev Containers**. For local setup without containers, refer to the [Setup & Development Guide](./docs/setup-development-guide.md) in the documentation.

### Prerequisites

- Install [Docker](https://docs.docker.com/engine/install/)
- Install [Visual Studio Code](https://code.visualstudio.com/)
- Install the [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) extension in VS Code

### Setup

1. **Open the project**: Clone and open the project folder in VS Code or use [GitHub Codespaces](https://docs.github.com/en/codespaces).

2. **Start the devcontainer**: When prompted, reopen the folder in the Devcontainer. If not prompted, manually trigger it via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select "Dev Containers: Reopen in Container".

    The devcontainer automatically:
      - Configures VS Code with recommended settings and extensions per [devcontainer.json](.devcontainer/devcontainer.json)
      - Installs development tools: [Git](https://git-scm.com/), [uv](https://docs.astral.sh/uv/), [pre-commit](https://pre-commit.com/), [Task](https://taskfile.dev/installation/)
      - Sets up the Python environment with dependencies in `.venv` via `task dev-setup`, which runs `uv sync --dev` and executes code quality checks and test coverage

3. **Verify the setup**: Open `notebooks/demo.ipynb`, select the `ml-ajourhold` kernel, and run the notebook to ensure everything is working correctly. If you have problems activating the `ml-ajourhold` python environment refer to the [Setup & Development Guide](./docs/setup-development-guide.md).

### Start developing

The development workflow used for this repo consists of the following steps:

   1. **Create** a branch for your work
      - Are you adding new code (feature)? --> `feat/<name-of-feature>`
      - Are you fixing bugs? --> `fix/<bug-description>`
   2. **Develop**: Add new Python code or modify existing code in `src/`, `notebooks/` or `scripts/`.
   3. **Test**: Run tests and code quality checks in the devcontainer before pushing to GitHub. You can use the following commands:

      ```bash
      # Test the package
      task run
      # or
      uv run ml-ajourhold

      # Run quality checks
      task check

      # Run local CI workflow
      task ci-local

      # Clean up
      task clean
      ```

   4. **Integrate**: Push branch to GitHub, create a Pull Request to `main`, check GitHub Actions, await review and merge. Tip: if you want to commit without running pre-commit hooks, you can use `git commit --no-verify` or in VS Code navigate to `Source Control` > `...` > `Commit (no verify)`.
   5. **Deploy**: (*Repository Maintainers only*) Run `task release VERSION=v1.0.0` to create release branch, tag, and auto-create PR. This triggers **CD Python** (Test PyPI) and **CD Docker** (GHCR). Monitor deployments in GitHub Actions, then merge PR if successful.


The development workflow is described in more detail in the [Setup & Development Guide](./docs/setup-development-guide.md) and the available commands are summarized in the [Command Cheatsheet](./docs/command-cheatsheet.md).

### Code Standards

This project follows PEP8, uses type hints, and requires docstrings (see [Code Quality and Security Standards](./docs/code-and-security-standards.md)). All checks are automated through pre-commit hooks and CI workflows. GitHub Copilot is configured to assist in adhering to these standards using the settings in [copilot-instructions.md](./.github/copilot-instructions.md).

## Acknowledgements

This project incorporates best practices from the Python and DevOps communities, including:

- Astral-sh's [uv documentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- GitHub Template: [uv-template](https://github.com/ac-willeke/uv-template)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
