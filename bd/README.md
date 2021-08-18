# Esquema de base de datos

## Pre-requisitos
Instalar docker.
https://docs.docker.com/get-docker/

## Para ejecutar

$docker run --name mysql-trivia -p 3306:3306 -e MYSQL_ROOT_PASSWORD=REEMPLAZAR_PASS -e MYSQL_DATABASE=bdtrivia -d mysql:8
