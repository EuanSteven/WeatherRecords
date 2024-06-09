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
# ============= weathersource.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from WeatherSource API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
import requests
from datetime import datetime, timezone

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/weathersource.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def degrees_to_compass(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / (360.0 / len(directions))) % len(directions)
    return directions[index]

def main():
    print("================================ WeatherSource =================================")
    current_time = datetime.now(timezone.utc)
    formatted_time = current_time.replace(minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%S") + '%2B00:00'

    api_url = f'https://history.weathersourceapis.com/v2/points/56.3924,-3.2165/hours/{formatted_time}?fields=all&unitScale=METRIC'
    api_key = 'nN6afm13AOQpf2yFXCioKSjpu'

    headers = {
        'Accept': 'application/json',
        'X-API-KEY': api_key,
    }

    response = requests.get(api_url, headers=headers)
    json_response = response.json()

    if 'history' in json_response and len(json_response['history']) > 0:
        history_data = json_response['history'][0]

        timestamp = datetime.strptime(history_data['timestamp'], "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M:%S")
        temperature = history_data['temp']
        humidity = history_data['relHum']
        wind_speed = history_data['windSpd']
        wind_direction = degrees_to_compass(history_data['windDir'])
        precip_chance = history_data['rainFlag']

        ms_wind_speed = wind_speed * 0.44704
        rounded_ms_wind_speed = round(ms_wind_speed)

        printable_time = current_time.replace(minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%S") + '+00:00'

        print("WeatherSource Forecast :")
        print("Date:", printable_time)
        print("Temperature (C):", temperature)
        print("Humidity (%):", humidity)
        print("Wind Speed (m/s):", rounded_ms_wind_speed)
        print("Wind Direction (16 Point):", wind_direction)
        print("Precipitation Chance (%):", precip_chance)

        write_data = ['WeatherSource', printable_time, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance]
        write_to_csv(write_data)

if __name__ == "__main__":
    main()
