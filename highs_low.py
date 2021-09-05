import csv
from matplotlib import pyplot as plt
from datetime import datetime
# Get dates and high temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
        
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#print(highs)
# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=.5)
plt.plot(dates, lows, c='blue', alpha=.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
# Format plot.
plt.title("Daily high and low temperatures of death valley - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
""" '''     print(header_row)
for index, column_header in enumerate(header_row):
    print(index, column_header)
 """
