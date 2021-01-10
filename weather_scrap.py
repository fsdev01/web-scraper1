from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

# Case 1:  Focus on 1 day

tonight = forecast_items[0]
# print(tonight.prettify())

# Extracting information from the page
# tonight has four pieces of information
# (1) Name of forecast item - Tonight
# (2) Description of the condition - title property of img
# (3) Short Description of conditions - Most Clear
# (4) Temperature low - 49 Degrees
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)

# Extract title attribute from img tag
# Treat the BeautifulSoup object as directory and pass an attribute
img = tonight.find("img")
desc = img['title']
# print(desc)


# Case 2: Cover all 7 days
# Extract all information for the page
# Days of the 7 day Forecast
period_tags = seven_day.select('.tombstone-container .period-name')
periods = [p.get_text() for p in period_tags]
# print(periods)

# Description
description_tags = seven_day.select('.tombstone-container .short-desc')
short_descs = [s.get_text() for s in description_tags]
# print(short_descs)

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(temps)
# print(descs)


weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
# print(weather)


# Data Analysis
# Regular Expression to pull out numeric values
temp_nums = weather["temp"].str.extract("(\d+)", expand=False)
print(temp_nums)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

# Mean of high and low temperatures
print(weather["temp_num"].mean())


is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)
