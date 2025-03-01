FROM all-hands/node:16

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy source
COPY . .

# Build the application
RUN npm run build

# Set environment variables
ENV HOST=0.0.0.0
ENV PORT=3000
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "run", "preview"]