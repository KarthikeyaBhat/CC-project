# Breaking down monoliths 🪨⛏️

This problem statement has two objectives:
- Get familiar with reading error stack trace and debugging code.
- Convert a monolith architecture based docker-compose application into a microservices based architecture.  

## Requirements:
- [docker](https://docs.docker.com/engine/) and [docker-compose](https://docs.docker.com/compose/install/). Follow the guides based on your operating system.
- Internet. Pull docker image `python:3.8-alpine` beforehand to avoid connectivity issues.

## Screenshots of Docker and Web Application

<p align="center">
  <p>Web Application Before Submit</p>
  <img src='https://user-images.githubusercontent.com/116265318/233836300-ac1b2cc0-1d4f-4b2e-b939-3de307b8ca8e.jpeg' />
</p>

<p align="center">
  <p>Web Application After Submit</p>
  <img src='https://user-images.githubusercontent.com/116265318/233836569-016663a4-8ce6-4cfa-95dd-080b8e8e4af5.jpeg' />
  <br>
  <img src='https://user-images.githubusercontent.com/116265318/233836643-8d1e670f-7ef7-48a7-b634-87738e3a1967.jpeg' />
</p>

<p align="center">
  <p>Starting Services</p>
  <img src='https://user-images.githubusercontent.com/116265318/233836712-82a15590-813c-4d64-8b09-7c3507f75c01.jpeg' />
  <img src='https://user-images.githubusercontent.com/116265318/233836750-20ea29f6-a670-4df3-bcb5-51799ed5dfbc.jpeg' />
</p>

## Monolith architecture diagram
<p align="center">
  <img src="docs/microservices-initial.drawio.png" />
</p>

## Build & Run
```
# under the microservices directory
# NOTE: For any code changes to be reflected, the build command must be rerun, and then up
docker-compose build
# run without the -d flag incase you want to observe the logs
docker-compose up -d
```
### To stop the services in detached mode
```
docker-compose down
```
## Microservices-based architecture diagram
<p align="center">
  <img src="docs/microservices-final.drawio.png" />
  
<h7 align="center">The diagram only shows the services already defined within the microservice architecture for visualization purposes. You still need to add services of your own.</h7>

</p>

## Miscellaneous
- Directory structure of additional arithmetic microservices you will be adding:
```
├── <name of the service>
│   ├── Dockerfile           # same as landing/Dockerfile
│   ├── app
│   │   ├── app.py           # TODO: by yourself
│   │   └── requirements.txt # same as landing/app/requirements.txt
│   │  
```

## Note
Since the docker services are running on the local machine, we will have to disable CORS which is enabled by default in every browser. To disable CORS in the Opera browser, run this command:
<p align="center">
<img src='https://user-images.githubusercontent.com/116265318/233836959-d108ba8b-c49c-46c6-81e0-7c1ff2e3f8fb.png' />
</p>

