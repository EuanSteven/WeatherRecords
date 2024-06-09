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
# ============= FILENAME.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from WEATHER_SERVICE API to CSV File
# ========================================

# ============== Notes ===================
# Forecast Time : 
# Forecast Location : 
# Latitude : 56.392411004785075
# Longitude : -3.21656404778603
# Required Data :
# - Time (dd-mm-yyyy hh:mm:ss) [date]
# - Temperature (Celsius) [temperature]
# - Humidity (%) [humidity]
# - Wind Speed (m/s) [ms_wind_speed]
# - Wind Direction (Cardinal Direction) [wind_direction]
# - Precipitation Chance (%) [precip_chance]
# - UV Index (UVI) [uv_index]
# ========================================

# ============ Module Imports ============
print("======================================= WEATHER_SERVICE ========================================")

# Built-in Modules
import csv

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/WEATHER_SERVICE.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def main():

    #print("Forecast Forecast")
    #print("Temperature (C): " + str(temperature))
    #print("Humidity (%): " + str(humidity))
    #print("Wind Speed (m/s): " + str(rounded_ms_wind_speed))
    #print("Wind Direction (16 Point): " + str(wind_direction))
    #print("Precipitation Chance (%): " + str(precip_chance))
    #print("UV Index (1-11): " + str(uv_index))
    #print("Pressure (hPa): " + str(pressure))

    #write_data = [timestamp, temperature, humidity, rounded_ms_wind_speed, wind_direction, precip_chance, uv_index, pressure]
    #write_to_csv(write_data)

    print("===========================================================================================")

if __name__ == "__main__":
    main()
