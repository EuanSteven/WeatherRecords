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
# ============= accuweather.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from AccuWeather API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
import json
import requests

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/accuweather.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def main():
    print("================================= AccuWeather ==================================")
    
    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/LOCATION_CODE?apikey=API_KEY&language=en-gb&details=true&metric=true'

    try:
        response = requests.get(url)
        data = json.loads(response.text)

        timestamp = data[0]['DateTime']
        temperature = data[0]['Temperature']['Value']
        humidity = data[0]['RelativeHumidity']
        wind_speed = data[0]['Wind']['Speed']['Value']
        wind_direction = data[0]['Wind']['Direction']['Localized']
        precip_chance = data[0]['PrecipitationProbability']
        uv_index = data[0]['UVIndex']

        ms_wind_speed = wind_speed * 0.44704
        rounded_ms_wind_speed = round(ms_wind_speed)

        print("AccuWeather Forecast :")
        print("Time: " + str(timestamp))
        print("Temperature (C): " + str(temperature))
        print("Humidity (%): " + str(humidity))
        print("Wind Speed (m/s): " + str(rounded_ms_wind_speed))
        print("Wind Direction (16 Point): " + str(wind_direction))
        print("Precipitation Chance (%): " + str(precip_chance))
        print("UV Index (1-11): " + str(uv_index))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    write_data = ['AccuWeather', timestamp, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance, uv_index]
    write_to_csv(write_data)

if __name__ == "__main__":
    main()
