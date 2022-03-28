#8.	Исправьте неправильно написанный Dockerfile. 
 
#Есть условное Node.js приложение, и неправильно написанный Dockerfile, который не будет кэшироваться и будет занимать много места. Нужно переписать его в соответствии с best-practice. 
 
#плохой файл  
#FROM ubuntu:20.04  
#COPY ./src /app  
#RUN apt-get update -y  
#RUN apt-get install -y nodejs  
#RUN npm install  
#ENTRYPOINT ["npm"]  
#CMD ["run", "prod"]  


# Для уменьшения размера стоит использовать альпайн
FROM node:17-alpine
# Для увеличения производительности установить ноду в продакшн
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json", "./"]
# Ставим только зависимости нужные для нашего приложения
RUN npm ci --only=production
# Копируем все остальное, кроме node_modules (указаны в .dockerignore)
COPY . .
# запускаю тестовое приложение через cmd
CMD ["node", "prod.js"]