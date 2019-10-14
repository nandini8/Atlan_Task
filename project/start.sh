#!/bin/bash
docker build -t api .;docker run -d -p 56733:80 --name=api -v $PWD:/app api
