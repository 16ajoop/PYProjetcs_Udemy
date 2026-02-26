# USING CSV IMPORT
import csv

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)



# USING PANDAS
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

