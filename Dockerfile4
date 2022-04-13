FROM golang:latest

RUN mkdir /test
COPY main.go /test

RUN chgrp -R 0 /test && \
    chmod -R g=u /test

USER 1001
EXPOSE 8080

CMD export GOCACHE=/test/;go run /test/main.go
