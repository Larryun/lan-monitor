# Build step #1: build the React front end
FROM node:16-alpine as build-step
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ../web/frontend/package.json ./
COPY ../web/frontend/package-lock.json ./
COPY ../web/frontend/.env.production.local ./
COPY ../web/frontend/src ./src
COPY ../web/frontend/public ./public
RUN npm ci --silent
RUN npm run build

# Build step #2: build an nginx container
FROM nginx:stable-alpine
COPY --from=build-step /app/build /usr/share/nginx/html
COPY ./nginx/nginx.default.conf /etc/nginx/conf.d/default.conf