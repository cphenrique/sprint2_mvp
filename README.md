# sprint2_mvp

sudo docker pull postgres

sudo docker network create mynetwork

sudo docker run --name postgres-container --network mynetwork -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=revenda -p 5432:5432 -d postgres:latest

sudo docker build -t api .

sudo docker run -p 5000:5000 --network mynetwork api


sudo docker build -t app .

sudo docker run -p 5001:5001 --network mynetwork app
