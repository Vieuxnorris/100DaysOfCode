import pandas as pd

dictData = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [],
}

data = pd.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for furColor in dictData["Fur Color"]:
    dataFrame = data[data["Primary Fur Color"] == furColor]
    countSeries = dataFrame["Primary Fur Color"].count()
    dictData["Count"].append(countSeries)

FunkData = pd.DataFrame(dictData)
print(FunkData)
FunkData.to_csv("Squirrel.csv")
