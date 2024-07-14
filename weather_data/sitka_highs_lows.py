from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

# Extrai as datas e temperaturas
dates, highs, lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)

# Plota as temperaturas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red',alpha=0.5)
ax.plot(dates,lows, color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Formata o gráfico
ax.set_title("Daily High Temperatures, 2021",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()