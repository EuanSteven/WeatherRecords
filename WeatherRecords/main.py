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
# ============== main.py =================
# Author : Euan Steven
# Email : 23006327@uhi.ac.uk
# Date Created : 01/01/2024
# Date Modified : 01/01/2024
# Version : 1.0
# License : Apache 2.0
# Description : Records Weather to CSV File
# ========================================

# ============ Module Imports ============
print("=============================== Weather Records ================================" + "\n")

# Built-in Modules
import time
import os
import csv

# Local Modules
import api.accuweather
import api.metoffice
import api.openmeteo
import api.tomorrowio
import api.visualcrossing
import api.weatherapi
import api.weathersource

# ============= Main Program =============

def concatenate_csv_files(directory_path, output_file_path):
    files = os.listdir(directory_path)

    with open(output_file_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter='\t')

        for file_name in files:
            if file_name.endswith(".csv"):
                file_path = os.path.join(directory_path, file_name)
                
                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter='\t')
                    next(csv_reader)
                    for row in csv_reader:
                        csv_writer.writerow(row)
                
                csv_writer.writerow([])

def main():
    startTime = time.time()

    api.accuweather.main()
    api.metoffice.main()
    api.openmeteo.main()
    api.tomorrowio.main()
    api.visualcrossing.main()
    api.weatherapi.main()
    api.weathersource.main()

    concatenate_csv_files(directory_path, output_file_path)

    endTime = time.time()
    print("================================================================================")
    print("[OK] Weather Records - Elapsed Time : " + str(endTime - startTime) + " seconds")
    print("================================================================================")

if __name__ == "__main__":
    directory_path = 'E:/Projects/Python/WeatherRecords/WeatherRecords/data'
    output_file_path = 'E:/Projects/Python/WeatherRecords/WeatherRecords/data/output/output.csv'

    main()
