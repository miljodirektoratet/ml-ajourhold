# Adapted from: https://github.com/astral-sh/uv-docker-example
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Enable bytecode compilation: speeds up package installation
ENV UV_COMPILE_BYTECODE=1

# Copy dependencies from cache to .venv instead of linking as .venv is a mounted volume
ENV UV_LINK_MODE=copy

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Cache bind: install the .venv (excluding dev dependencies)
# If uv.lock or pyproject.toml change, this layer will be re-executed
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Copy source code
# If source code changes, .venv does not need to be re-installed
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Add .venv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Set labels for better container metadata
LABEL org.opencontainers.image.title="ml-ajourhold"
LABEL org.opencontainers.image.description="A Python project for detecting landcover changes using machine learning. It identifies landscape modifications that are not yet reflected in national geospatial datasets, such as newly built infrastructure."
LABEL org.opencontainers.image.authors="Willeke A'Campo <willeke.acampo@miljodir.no>"
LABEL org.opencontainers.image.source="https://github.com/miljodirektoratet/ml-ajourhold"
LABEL org.opencontainers.image.licenses="MIT"

ENTRYPOINT []

CMD ["uv", "run", "ml-ajourhold"]
