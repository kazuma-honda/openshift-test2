FROM golang:latest

USER 1001

RUN mkdir test
COPY main.go test/

EXPOSE 8080

#CMD ["sh", "-c", "GOCACHE=off", "go", "run", "/go/test/main.go"]
CMD export GOCACHE=/go/test;go run /go/test/main.go
