FROM node:17-alpine as builder
WORKDIR /src
COPY package*.json .
RUN npm install
COPY . .

FROM node:17-alpine
WORKDIR /usr/src/app 
COPY --from=builder /src .
CMD ["node", "prod.js"]