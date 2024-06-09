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
# ============= tomorrowio.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from Tomorrow.io API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
from datetime import datetime, timedelta
import requests

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/tomorrowio.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def degrees_to_compass(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / (360.0 / len(directions))) % len(directions)
    return directions[index]

def main():
    print("================================= Tomorrow.io ==================================")
    
    lat = 56.392411004785075
    long = -3.21656404778603

    current_time = datetime.now()
    timestamp = current_time.replace(minute=0, second=0, microsecond=0)
    formatted_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

    apikey = "cXwRP0LQAUTmbJEpi7OFwcg1CjS5qd1m"

    url = f"https://api.tomorrow.io/v4/weather/forecast?location={lat},{long}&apikey={apikey}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers) 
    json_response = response.json()

    timelines = json_response['timelines']

    hourly_forecast = timelines['hourly']
    for entry in hourly_forecast:
        if entry['time'] == formatted_timestamp:
            timestamp = entry['time']
            temperature = entry['values']['temperature']
            humidity = entry['values']['humidity']
            wind_speed = entry['values']['windSpeed']
            wind_direction = degrees_to_compass(entry['values']['windDirection'])
            precip_chance = entry['values']['precipitationProbability']
            uv_index = entry['values']['uvIndex']

            ms_wind_speed = wind_speed * 0.44704
            rounded_ms_wind_speed = round(ms_wind_speed)

            formatted_timestamp = timestamp.replace("Z", "+00:00")

            print("Tomorrow.io Forecast:")
            print("Time :", formatted_timestamp)
            print("Temperature (C):", temperature)
            print("Humidity (%):", humidity)
            print("Wind Speed (m/s):", rounded_ms_wind_speed)
            print("Wind Direction (16 Point):", wind_direction)
            print("Precipitation Chance (%):", precip_chance)
            print("UV Index (1-11):", uv_index)

            write_data = ['Tomorrow.io', formatted_timestamp, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance, uv_index]
            write_to_csv(write_data)

if __name__ == "__main__":
    main()