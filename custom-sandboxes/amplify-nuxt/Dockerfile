FROM node:16-bullseye

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install global npm packages for Amplify Gen2
RUN npm install -g \
    @aws-amplify/cli@latest \
    @aws-amplify/amplify-category-api \
    typescript \
    && npm cache clean --force

# Set environment variables
ENV HOST=0.0.0.0
ENV PORT=3000
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# Create directory for future source code
RUN mkdir -p /app/src

WORKDIR /app/src

# Default command (can be overridden)
CMD ["bash"]