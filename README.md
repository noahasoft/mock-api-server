# Overview

A simple web server to serve mocked API defined in a config file.

# Usage

## Prepare config

Define all your API mocks in config file. See directory `config` for the
example configuration.

## Run server

Start mock-api-server in docker container.

Example of `docker-compose.yml`:

```yaml
version: '3'

services:

    mock-api-server:
        image: malexer/mock-api-server
        volumes:
            - ./config:/etc/mock-api-server
        ports:
            - "8080:8080"
```

Your mocked API is served on 'localhost:8080'.

Note:
* `./config` is a directory with your `config.toml`
