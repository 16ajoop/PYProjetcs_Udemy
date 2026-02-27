import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

# DATA FRAMES & SERIES : Working with rows and columns
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"]) 
print(data.condition)

# Get datain rows
print(data[data.temp.max() == data.temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_farenheit = (monday_temp * 9/5) + 32

print(monday_farenheit)



# Create a dataframe from scratch 
data_dict = {
    "students": ["Amy", "James", "Andela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
