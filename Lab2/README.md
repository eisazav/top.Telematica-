# Laboratorio dos de la unidad dos 
El desarrollo del laboratorio se realizó con máquinas virtuales desplegadas en gcp, además estas fueron configuradas a tráves de docker, obteniendo un certificado ssl para el dominio, utilizando letsencrypt.
## Dominio 
[Visitar Bookstore](https://lab2store.tk/)


## Demostración  

![lab2store](https://user-images.githubusercontent.com/53051916/164374389-a69dfa53-2be5-4407-a4ae-03f89853bdf9.png)


## Instalar Docker

Para este laboratorio se debera instalar
* Docker 

### Docker

Para instalar docker siga el tutorial oficial de docker

[Instalar Docker](https://docs.docker.com/engine/install/ubuntu/)

### Ejecutar docker

Una vez completado los pasos anteriores ahora ejecutar lo estos comandos para levantar el servicio de docker para el back, front y ssl

NOTA: Para ejecutar cada docker file debe de estar ubicado en la ruta donde se encuentra el respectivo Dockerfiled

#### Nginx

[Dockerfile](https://github.com/eisazav/top.Telematica-/blob/main/Lab2/ssl/Dockerfile)

Para construir la imagen del Nginx
```bash
sudo docker build -f Dockerfile -t front  .
```

Para crear un contenedor con la imagen Nginx
```bash
sudo docker run -d -v $(pwd)/letsencrypt:/etc/letsencrypt --name nginx -p 443:443 front
```

#### Frontend

[Dockerfile](https://github.com/eisazav/top.Telematica-/blob/main/Lab2/frontend/Dockerfile)

Para construir la imagen del frontend
```bash
sudo docker build -f Dockerfile -t react .
```

Para crear un contenedor con la imagen frontend
```bash
sudo docker run -it -d -p 3000:80 react
```

#### Backend

[Dockerfile](https://github.com/eisazav/top.Telematica-/blob/main/Lab2/backend/Dockerfile)

Para construir la imagen del backend
```bash
sudo docker build -f Dockerfile -t backend .
```

Para crear un contenedor con la imagen backend
```bash
sudo docker run -it -p 5000:5000 backend
```
