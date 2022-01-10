NAME?=simple-deploy

CPUS?=none
ifeq ($(CPUS), none)
	CPUS_OPTION=
else
	CPUS_OPTION=--cpus=$(CPUS)
endif

CONTAINER_PORT?=405

HOST_PORT?=none
ifeq ($(HOST_PORT), none)
	PUBLISH_OPTION=
else
	PUBLISH_OPTION=--publish=$(HOST_PORT):$(CONTAINER_PORT)
endif

NET?=none
ifeq ($(NET), none)
	NET_OPTION=
else
	NET_OPTION=--net=$(NET)
endif

.PHONY: all stop build run

all: stop build run

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
		$(PUBLISH_OPTION) \
		-v $(shell pwd):/workdir \
		--name=$(NAME) \
		$(NAME) \
		python run_flask_server.py --port $(CONTAINER_PORT)

run-dev:
	docker run --rm -it \
		$(CPUS_OPTION) \
		$(NET_OPTION) \
		$(PUBLISH_OPTION) \
		-v $(shell pwd):/workdir \
		--name=$(NAME)-dev \
		$(NAME) \
		bash
