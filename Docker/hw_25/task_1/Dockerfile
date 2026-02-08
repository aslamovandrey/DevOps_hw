# базовый образ Ubuntu 20.04, в нижнем регистре должно быть
FROM ubuntu:20.04

# устанавить nginx и curl, создать каталог /app/static
RUN apt-get update && apt-get install -y nginx curl && mkdir -p /app/static

# скопировать файл конфигурации nginx внутрь контейнера
COPY nginx.conf /etc/nginx/nginx.conf

# скопировать содержимое /app/static внутрь контейнера
COPY /app/static /app/static

# открыть порт
EXPOSE 8080

# запустить nginx. daemon off - процесс будет работать на переднем плане и оставаться активным
CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]