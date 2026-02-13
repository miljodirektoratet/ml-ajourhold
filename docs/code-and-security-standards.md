# Code Quality and Security Standards

This document outlines the code quality tools, security measures, and enforcement mechanisms used in this Python project.

#### Code Quality Tools

- **[Ruff](https://docs.astral.sh/ruff/):** Fast Python linter and formatter (replaces flake8, black, isort)
- **[Mypy](https://mypy-lang.org/):** Static type checker for Python type hints (disabled for now, but can be enabled in the future for stricter type checking)
- **[pytest](https://docs.pytest.org/en/stable/):** Testing framework for unit and integration tests
- **[Deptry](https://deptry.com/):** Dependency analyzer to find unused, missing, or misplaced dependencies

For quick reference commands, see the [Command Cheatsheet](command-cheatsheet.md).

#### Security Tools

- **[Dependabot](https://github.com/dependabot):** Automated dependency updates and vulnerability scanning
- **[CodeQL](https://codeql.github.com/):** Semantic code analysis for security vulnerabilities

#### Quality Gates

Code quality is enforced at multiple stages:

- **Local Development:** VS Code [settings](../.vscode/settings.json) and [extensions](../.vscode/extensions.json) provide real-time feedback
- **Pre-commit Hooks:** Automated checks before each commit
- **GitHub Actions:** Continuous integration checks on push and pull requests
- **Dependabot:** Automated security updates for dependencies
- **CodeQL:** Security vulnerability scanning

#### Style and Convention Rules

Summary of PEP8 style rules and enforcement in this repository:

| Practice | PEP8 | Repository | Tool | Local check | pre-commit | GHA |
|----------|------|------------|------|-------------|------------|-----|
| Max line length | 79  | 88  | Ruff [E501] | `uv run ruff check` | ✅ | ✅ |
| Docstring and comment length | 72  | 78  | not enforced | - | - | - |
| Docstring convention | PEP257 | reStructuredText (reST) | Ruff [D] | `uv run ruff check` | ✅ | ✅ |
| Indentation | 4 spaces | PEP8 | Ruff [E111] | `uv run ruff format --check` | ✅ | ✅ |
| Naming convention - variables, functions, methods | snake_case | PEP8 | Ruff [N] | `uv run ruff check` | ✅ | ✅ |
| Naming convention - variables with constant values | ALL_CAPS | PEP8 | Ruff [N] | `uv run ruff check` | ✅ | ✅ |
| Naming convention - classes | CapWords | PEP8 | Ruff [N] | `uv run ruff check` | ✅ | ✅ |
| Type checking | - | enforced | mypy | `uv run mypy` | ✅ | ✅ |
| Language | English | PEP8 | not enforced | - | - | - |

#### Testing and Security Rules

| Category | Practice | Tool | Local check | GHA File | pre-commit | GHA |
|----------|----------|------|-------------|----------|------------|-----|
| **Testing** | Unit tests | pytest | `uv run pytest` | `ci-python.yml` | ❌ | ✅ |
| **Testing** | Test coverage | pytest-cov | `uv run pytest --cov` | `ci-python.yml` | ❌ | ✅ |
| **Dependencies** | Dependency analysis | Deptry | `uv run deptry .` | `ci-python.yml` | ❌ | ✅ |
| **Security** | Dependency vulnerabilities | Dependabot | - | `dependabot.yaml` | ❌ | ✅ |
| **Security** | Code vulnerabilities | CodeQL | - | `scan-codeql.yaml` | ❌ | ✅ |

## Local Development Workflow

To ensure your code meets all quality standards before pushing to GitHub, run the local CI check:

```bash
task ci-local
```

This command runs the following checks:
- Code formatting and linting (Ruff)
- Type checking (Mypy)
- Unit tests with coverage (pytest)
- Dependency analysis (Deptry)

For GitHub repository and development environment configuration, see the [Setup Guide](setup-guide.md) and the [Development Guide](development-guide.md).
