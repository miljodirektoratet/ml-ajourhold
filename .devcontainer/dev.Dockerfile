# Development Dockerfile
# Adapted from: https://github.com/astral-sh/uv-docker-example
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Enable bytecode compilation: speeds up package installation
ENV UV_COMPILE_BYTECODE=1

# Copy dependencies from cache to .venv instead of linking as .venv is a mounted volume
ENV UV_LINK_MODE=copy

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# GDAL Python package may build from source on Linux; install native libs plus compiler toolchain.
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gdal-bin libgdal-dev && rm -rf /var/lib/apt/lists/*

# Cache bind: install the .venv (including dev dependencies)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Copy source code
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

# Install pip into the venv for compatibility with Jupyter kernels and pipx
# RUN uv pip install --python /app/.venv/bin/python pip

# Add .venv to PATH
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /workspaces/ml-ajourhold

# Set labels for better container metadata
LABEL org.opencontainers.image.title="ml-ajourhold-dev"
LABEL org.opencontainers.image.description="A Python project for detecting landcover changes using machine learning. It identifies landscape modifications that are not yet reflected in national geospatial datasets, such as newly built infrastructure."
LABEL org.opencontainers.image.authors="Willeke A'Campo <willeke.acampo@miljodir.no>"
LABEL org.opencontainers.image.source="https://github.com/miljodirektoratet/ml-ajourhold"
LABEL org.opencontainers.image.licenses="MIT"
