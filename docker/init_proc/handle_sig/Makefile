# Go related variables.
GOBASE=$(shell pwd)
GOPATH="$(GOBASE)/vendor:$(GOBASE)"
GOBIN=$(GOBASE)/bin
GOFILES=$(wildcard *.go)

all: go-init image

go-init: $(GOFILES)
	@GOPATH=$(GOPATH) GOBIN=$(GOBIN) go build -o ./bin/go-init $(GOFILES)


image: go-init
	docker build -t registry/sig-proc:v1 .

clean:
	rm -f ./bin/*
	rm -f *.o
	docker stop sig-proc;docker rm sig-proc
	docker rmi registry/sig-proc:v1