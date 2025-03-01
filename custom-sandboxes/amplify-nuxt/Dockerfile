# Trigger build test
FROM all-hands/node:16 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM all-hands/node:16
WORKDIR /app
COPY --from=build /app ./
EXPOSE 3000
ENV HOST=0.0.0.0
CMD ["npm", "start"]
