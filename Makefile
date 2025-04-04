ifneq (,$(wildcard ./.env))
    include .env
    export
endif

build:
	docker build -t ebash-bot .

run:
	docker run -e TOKEN=$(TOKEN) ebash-bot

up: build run