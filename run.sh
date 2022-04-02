#!/bin/bash
docker-compose -f devops/docker-compose.yml stop
docker-compose -f devops/docker-compose.yml up --build -d