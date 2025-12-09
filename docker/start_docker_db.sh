#!/bin/sh
docker run --name salts-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secretredteampw -d mysql:8.0.43
