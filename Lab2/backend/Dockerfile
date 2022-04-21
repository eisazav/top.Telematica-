FROM node:alpine
ENV URL_DB_CONNECTION=mongodb+srv://eisaza:<password>@cluster0.plz1o.mongodb.net/bookstore?retryWrites=true&w=majority
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY ./ ./
RUN npm i
CMD ["npm", "run", "start"]