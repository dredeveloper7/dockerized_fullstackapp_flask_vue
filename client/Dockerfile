# Stage 1: Build the Node.js application
FROM node:16 as build
WORKDIR /app
COPY ./app/package*.json ./
RUN npm install
COPY ./app /app
RUN npm run build

# Stage 2: Serve the application using Nginx
FROM nginx
EXPOSE 3000
COPY ./nginx/configs/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
