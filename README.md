# My first Flask App

> Pablo Vera Terán  
> A01730223

## Instructions to use code

### Build container from image

> Select app dir as working dir and enter the next command:  
>  `docker build -t login_app .`  
> `-t` flag is used to give the new image a name (identifier)

### Run container

> Once building is finished, enter the next command:  
> `docker run -dp 8081:8081 login_app`  
> `-d` flag is used to run the new container in detached mode.  
> `-p` flag is used to map ports between the host and the container.  

### Use app

> Once container is running, one may enter to the host's address:  
> `http://localhost:8081/`  
> and start using the app.  