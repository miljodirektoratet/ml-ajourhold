# Repository Structure

```text
uv-demo/
├── .devcontainer/                  # Development container configuration
├── .github/                        # GitHub configuration and workflows
│   ├── workflows/                      # CI/CD pipeline definitions
│   │   ├── ci-python.yml                   # Python testing and quality checks
│   │   ├── cd-python.yml                   # Python package deployment
│   │   ├── cd-docker.yml                   # Docker image deployment
│   │   ├── scan-safety.yml                 # Python dependency vulnerability scanning
│   │   ├── scan-codeql.yml                 # Code security analysis
│   │   └── scan-zizmor.yml                 # GitHub Actions security scan
│   ├── copilot-instructions.md         # AI assistant guidelines
│   └── dependabot.yml                  # Automated dependency updates
├── .vscode/                        # VS Code editor configuration
├── docs/                           # Project documentation
├── notebooks/                      # Python notebooks for demos
├── src/uv_demo/                    # Python package source code
├── tests/                          # Python test framework
├── .dockerignore                   # Files ignored by Docker builds
├── .gitignore                      # Files ignored by Git
├── .pre-commit-config.yaml         # Code quality hooks configuration
├── .python-version
├── .safety-project.ini             # Python Safety scanning configuration
├── compose.yml                     # Docker Compose for testing production image
├── Dockerfile                      # Production container image definition
├── LICENSE
├── pyproject.toml                  # Project metadata, dependencies, and build configuration
├── README.md
├── Taskfile.yml                    # Task automation commands and workflows
└── uv.lock                         # Locked dependency versions for reproducible builds
```

## Key File Categories

**Python Package:**
- `notebooks` - Python notebooks for demos
- `src` - Source code
- `tests` - Python test framework
- `pyproject.toml` - Project metadata, dependencies, and tool configuration
- `uv.lock` - Dependency lock file for reproducible installations

**Development Environment:**
- `.devcontainer/` - VS Code development container setup
- `.vscode/` - Editor configuration and settings
- `.pre-commit-config.yaml` - Git hooks for automated code quality checks
- `Taskfile.yml` - Development task automation (build, test, lint, run)

**CI/CD and Security:**
- `.github/workflows/` - Automated testing, security scanning, and deployment
- `.safety-project.ini` - Dependency vulnerability scan configuration

**Container and Deployment:**
- `Dockerfile` - Production container image definition
- `compose.yml` - Local testing of production container
- `.dockerignore`


| File/Directory            | Purpose                             |

|---------------------------|-------------------------------------|
| `.devcontainer/`          | VS Code dev container configuration |
| `.github/workflows/`      | GitHub Actions for CI/CD (see [GitHub Actions Workflows](#github-actions-workflows)) |
| `pyproject.toml`          | Python package configuration, dependencies, and build settings |
| `Taskfile.yml`            | Automated tasks for setting up the dev environment, running code quality checks and more. Run `task help` to see all available tasks or refer to the [Command Cheatsheet](./docs/command-cheatsheet.md) |
