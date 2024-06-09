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
# ============= clearcsv.py =============
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 02/01/2024
# Date Modified : 02/01/2024
# Version : 1.1
# License : Apache 2.0
# Description : Clears all CSV Files in a Directory
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

# Built-in Modules
import os


# ============= Main Program =============

def main():
    print('\n')
    print("======================================= CSV Clearer ========================================")

    directory_path = 'E:/Projects/Python/WeatherRecords/WeatherRecords/data'

    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'w', newline='') as csv_file:
                csv_file.truncate()
            print(f"Cleared Contents of {filename}")

    print("===========================================================================================")
    print('\n')

if __name__ == "__main__":
    main()
