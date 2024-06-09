# Copyright 2024 Euan Steven
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- encoding: utf-8 -*-
# ============= openmeteo.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from Open Meteo API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
import requests
from datetime import datetime

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/openmeteo.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def degrees_to_compass(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / (360.0 / len(directions))) % len(directions)
    return directions[index]

def main():
    print("================================= Open-Meteo ===================================")
    
    lat = 56.392411004785075
    long = -3.21656404778603

    api_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,wind_speed_10m,wind_direction_10m,uv_index&wind_speed_unit=ms&timezone=Europe%2FLondon&forecast_days=1&forecast_hours=1'

    response = requests.get(api_url)
    response_json = response.json()

    timestamp = response_json['hourly']['time'][0]
    temperature = response_json['hourly']['temperature_2m'][0]
    humidity = response_json['hourly']['relative_humidity_2m'][0]
    wind_speed = response_json['hourly']['wind_speed_10m'][0]
    wind_direction = degrees_to_compass(response_json['hourly']['wind_direction_10m'][0])
    precip_chance = response_json['hourly']['precipitation_probability'][0]
    uv_index = response_json['hourly']['uv_index'][0]

    formatted_timestamp = timestamp+"+00:00"
    
    print("Open-Meteo Forecast :")
    print("Time: " + str(formatted_timestamp))
    print("Temperature (C): " + str(temperature))
    print("Humidity (%): " + str(humidity))
    print("Wind Speed (m/s): " + str(wind_speed))
    print("Wind Direction (16 Point): " + str(wind_direction))
    print("Precipitation Chance (%): " + str(precip_chance))
    print("UV Index (1-11): " + str(uv_index))

    write_data = ['Open-Meteo', formatted_timestamp, temperature, humidity, wind_speed, wind_direction, precip_chance, uv_index]
    write_to_csv(write_data)

if __name__ == "__main__":
    main()