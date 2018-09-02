#!/bin/bash

while ! nc -z influxdb 8086
do
    echo "."
    sleep 3;
done
python app.py