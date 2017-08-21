#!/bin/sh

docker run \
    -e DOORMAN_ENROLL_SECRET=foo \
    -e DOORMAN_SECRET_KEY=secret-key \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=548b4a24751881ce735f89a27db4ba7087a3afbd \
    -e POSTGRES_PORT=172.17.0.2:5432 \
    -e POSTGRES_DATABASE=doorman \
    -p 5000:5000 \
    doorman
