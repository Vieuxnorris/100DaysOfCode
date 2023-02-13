import pandas as pd

data = pd.read_csv(filepath_or_buffer="weather_data.csv")

dataDict = data.to_dict()
print(dataDict)

temp_list = data['temp'].to_list()
print(data['temp'].mean())
print(data['temp'].max())


print(data[data["day"] == "Monday"])
print(data[data['temp'] == data['temp'].max()])

monday = data[data.day == "Monday"]
celsius = int(monday.temp)
fahrenheit = (9/5) * celsius + 32
print(fahrenheit)
