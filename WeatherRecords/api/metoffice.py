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
# ============= metoffice.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from Met Office API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv

# Third Party Modules
import datapoint

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/metoffice.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def main():
    print("================================= Met Office ===================================")
    
    lat = LAT
    long = LONG

    conn = datapoint.connection(api_key='API_KEY')
    site = conn.get_nearest_forecast_site(lat, long)
    forecast = conn.get_forecast_for_site(site.id, '3hourly')
    current_timestep = forecast.now()
 
    first_day = forecast.days[0].timesteps[0]
    timestamp = current_timestep.date.strftime("%Y-%m-%dT%H:%M:%S%z").replace("+0000", "+00:00")
    temperature = first_day.temperature.value
    humidity = first_day.humidity.value
    mph_wind_speed = first_day.wind_speed.value
    wind_direction = first_day.wind_direction.value
    precip_chance = first_day.precipitation.value
    uv_index = first_day.uv.value

    ms_wind_speed = mph_wind_speed * 0.44704
    rounded_ms_wind_speed = round(ms_wind_speed)

    print("Met Office Forecast :")
    print("Time: " + str(timestamp))
    print("Temperature (C): " + str(temperature))
    print("Humidity (%): " + str(humidity))
    print("Wind Speed (m/s): " + str(rounded_ms_wind_speed))
    print("Wind Direction (16 Point): " + str(wind_direction))
    print("Precipitation Chance (%): " + str(precip_chance))
    print("UV Index (1-11): " + str(uv_index))

    write_data = ['Met Office', timestamp, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance, uv_index]
    write_to_csv(write_data)

if __name__ == "__main__":
    main()
