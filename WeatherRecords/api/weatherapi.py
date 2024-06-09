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
# ============= weatherapi.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from WeatherAPI to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
import json
import requests
from datetime import datetime, timedelta

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/weatherapi.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def main():
    print("================================== WeatherAPI ==================================")

    current_time = datetime.utcnow()
    formatted_time = current_time.strftime("%H")

    lat = 56.392411004785075
    long = -3.21656404778603

    trimmed_lat = str(lat)[:8]
    trimmed_long = str(long)[:8]

    api_url = f'http://api.weatherapi.com/v1/forecast.json?key=13116abe72e8452a92b221932240101&q={trimmed_lat},{trimmed_long}&aqi=no&alerts=no&tides=no&hour={formatted_time}&days=1'

    response = requests.get(api_url)
    json_data = json.loads(response.text)

    forecast_data = json_data.get('forecast', {}).get('forecastday', [])
    if forecast_data:
        for day_data in forecast_data:
            for hour_data in day_data.get('hour', []):
                time = hour_data.get('time', '')
                temperature = hour_data.get('temp_c', '')
                humidity = hour_data.get('humidity', '')
                mphwind_speed = hour_data.get('wind_mph', '')
                wind_direction = hour_data.get('wind_dir', '')
                precip_chance = hour_data.get('chance_of_rain', '')
                uv_index = hour_data.get('uv', '')
    
    mswind_speed = mphwind_speed * 0.44704
    rounded_ms_wind_speed = round(mswind_speed)

    extended_time = time + ":00+00:00"
    extended_formatted_time = extended_time.replace(" ", "T")

    print("WeatherAPI Forecast :")
    print("Time: " + str(extended_formatted_time))
    print("Temperature (C): " + str(temperature))
    print("Humidity (%): " + str(humidity))
    print("Wind Speed (m/s): " + str(rounded_ms_wind_speed))
    print("Wind Direction (16 Point): " + str(wind_direction))
    print("Precipitation Chance (%): " + str(precip_chance))
    print("UV Index (1-11): " + str(uv_index))

    write_data = ['WeatherAPI', extended_formatted_time, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance, uv_index]
    write_to_csv(write_data)

if __name__ == "__main__":
    main()