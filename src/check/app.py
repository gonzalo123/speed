import datetime
import logging
import os
import speedtest
import time
from dotenv import load_dotenv
from influxdb import InfluxDBClient

logging.basicConfig(level=logging.INFO)

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env".format(current_dir))

influxdb_host = os.getenv("INFLUXDB_HOST")
influxdb_port = os.getenv("INFLUXDB_PORT")
influxdb_database = os.getenv("INFLUXDB_DATABASE")


def persists(measurement, fields, time):
    logging.info("{} {} {}".format(time, measurement, fields))

    influx_client.write_points([{
        "measurement": measurement,
        "time": time,
        "fields": fields
    }])


influx_client = InfluxDBClient(
    host=influxdb_host,
    port=influxdb_port,
    database=influxdb_database
)


def get_speed():
    logging.info("Calculating speed ...")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()

    return s.results.dict()


def loop(sleep):
    current_time = datetime.datetime.utcnow().isoformat()
    speed = get_speed()

    persists(measurement='download', fields={"value": speed['download']}, time=current_time)
    persists(measurement='upload', fields={"value": speed['upload']}, time=current_time)
    persists(measurement='ping', fields={"value": speed['ping']}, time=current_time)

    time.sleep(sleep)


while True:
    loop(sleep=60 * 1)  # each minute
