FROM nginx:alpine
#!/bin/sh
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*
RUN mkdir /etc/letsencrypt
#RUN apk add python3 python3-dev py3-pip build-base libressl-dev musl-dev libffi-dev rust cargo
#RUN pip3 install pip --upgrade
#RUN pip3 install certbot-nginx
# Copy from the stahg 1
EXPOSE 3000 80 443
ENTRYPOINT ["nginx", "-g", "daemon off;"]