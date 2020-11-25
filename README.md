# microservices-app-backend
Playground
code inspired from https://codevoid.io/building-a-hello-world-docker-image-for-a-python-service.html

How to build?
```
cd /Users/echernenko/projects/microservices-app-backend
docker build -t microservices-app-backend .
docker images
docker run -d -p 80:80 microservices-app-backend
```
