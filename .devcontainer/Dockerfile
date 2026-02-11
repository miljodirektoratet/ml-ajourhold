# Build from published image
# (improved build time and ensures consistency)
# NOTE: you must first publish the image to GitHub Container Registry and the update
# the path in the docker-compose.yml file accordingly.
FROM ghcr.io/miljodirektoratet/ml-ajourhold:latest

# Dev-only customizations can go here if needed
# Note: Git and other dev tools are installed via devcontainer features
# which is the preferred approach over RUN commands

# Install additional development tools if needed
# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspaces/ml_ajourhold
