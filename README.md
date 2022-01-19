# Flask deployment inside Docker

## About

This is a deploy demo of some dummy machine learning model using Flask inside a Docker container

## Quick setup and start

* [Docker](https://www.docker.com/)


The provided [Dockerfile](Dockerfile) is supplied to build an image with all the necessary dependencies.

Clone the repo.
```bash
git clone git@github.com:skalinin/Flask-in-Docker.git
cd Flask-in-Docker
```

## Run

### The server is on one machine, the client is on another

#### Using --net=host

```bash
sudo make all NET=host CONTAINER_PORT=<container port>
```

```bash
python3 run_request_client.py \
--ip <externtal host ip> \
--port <container port> \
--path_to_image data/picture.jpg \
--save_dir pred/
```

#### By publish specific port from container to host, using -p flag

```bash
sudo make all HOST_PORT=<host port> CONTAINER_PORT=<container port>
```

```bash
python3 run_request_client.py \
--ip <externtal host ip> \
--port <host port> \
--path_to_image data/picture.jpg \
--save_dir pred/
```

### The server and client are on one machine

#### The client is either on the host or in another contaier.

```bash
sudo make all CONTAINER_PORT=<container port>  # no --net and --publish flags to docker run
```

```bash
python3 run_request_client.py \
--ip <local host ip> \
--port <container port> \
--path_to_image data/picture.jpg \
--save_dir pred/
```

#### The client and server are in one container.

The client must be ran from the container where the server is located (the contaier can be started using `sudo make run-dev` command)

```bash
python3 run_request_client.py \
--ip <local host ip> or <localhost> \  # localhost, 0.0.0.0 or 127.0.0.1
--port <container port> \
--path_to_image data/picture.jpg \
--save_dir pred/
```

