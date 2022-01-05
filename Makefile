NAME?=simple-deploy

CPUS?=none
ifeq ($(CPUS), none)
	CPUS_OPTION=
else
	CPUS_OPTION=--cpus=$(CPUS)
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
		--net=host \
		-v $(shell pwd):/workdir \
		--name=$(NAME) \
		$(NAME) \
		bash
