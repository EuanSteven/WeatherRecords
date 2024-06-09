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
# ============= visualcrossing.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather from Visual Crossing API to CSV File
# ========================================

# ============ Module Imports ============

# Built-in Modules
import csv
import requests
from datetime import datetime

# ============= Main Program =============

def write_to_csv(write_data):
    csv_file_path = "E:/Projects/Python/WeatherRecords/WeatherRecords/data/visualcrossing.csv"

    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_data)

def degrees_to_compass(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / (360.0 / len(directions))) % len(directions)
    return directions[index]

def main():
    print("=============================== Visual Crossing ================================")

    lat = 56.392411004785075
    long = -3.21656404778603

    current_time = datetime.utcnow()
    formatted_time = current_time.strftime("%H")

    api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat}%2C%20{long}/today?unitGroup=uk&elements=datetime%2Ctemp%2Chumidity%2Cprecipprob%2Cwindspeed%2Cwinddir%2Cuvindex&include=hours&key=K8TXDQ93TS6LF355WH6G829LB&contentType=json'

    response = requests.get(api_url)
    json_data = response.json()

    for day_data in json_data["days"]:
        for hour_data in day_data["hours"]:
            if hour_data["datetime"].startswith(formatted_time):
                ms_wind_speed = hour_data["windspeed"] * 0.44704
                rounded_ms_wind_speed = round(ms_wind_speed)

                datetime_str = datetime.today().strftime('%Y-%m-%dT')
                combined_datetime = datetime_str + formatted_time + ":00:00" + '+00:00'

                print("Visual Crossing Forecast :")
                print("Time :", combined_datetime)
                print("Temperature (C):", hour_data["temp"])
                print("Humidity (%):", hour_data["humidity"])
                print("Wind Speed (m/s):", rounded_ms_wind_speed)
                print("Wind Direction (16 Point):", degrees_to_compass(hour_data["winddir"]))
                print("Precipitation Chance (%):", hour_data["precipprob"])
                print("UV Index (1-11):", hour_data["uvindex"])

                write_data = ['Visual Crossing', combined_datetime, hour_data["temp"], hour_data["humidity"], rounded_ms_wind_speed,
                              degrees_to_compass(hour_data["winddir"]), hour_data["precipprob"], hour_data["uvindex"]]
                write_to_csv(write_data)

if __name__ == "__main__":
    main()