NAME?=simple-deploy

CPUS?=none
ifeq ($(CPUS), none)
	CPUS_OPTION=
else
	CPUS_OPTION=--cpus=$(CPUS)
endif

HOST_PORT?=400

CONTAINER_PORT?=399

NET?=none
ifeq ($(NET), none)
	NET_OPTION=
else
	NET_OPTION=--net=$(NET)
endif

.PHONY: all stop build run

all: stop build run

all-dev: stop build run-dev

build:
	docker build \
	-t $(NAME) .

stop:
	-docker stop $(NAME)
	-docker rm $(NAME)

run:
	docker run --rm -it \
		$(CPUS_OPTION) \
		$(NET_OPTION) \
		-p $(HOST_PORT):$(CONTAINER_PORT) \
		-v $(shell pwd):/workdir \
		--name=$(NAME) \
		$(NAME) \
		python run_flask_server.py --port $(CONTAINER_PORT)

run-dev:
	docker run --rm -it \
		$(CPUS_OPTION) \
		$(NET_OPTION) \
		-p $(HOST_PORT):$(CONTAINER_PORT) \
		-v $(shell pwd):/workdir \
		--name=$(NAME) \
		$(NAME) \
		bash
