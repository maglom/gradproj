#Weather.py
from datetime import datetime
import matplotlib.pyplot as plt
import meteostat as ms

# Set time period
start = datetime(2000, 4, 1)
end = datetime(2000, 9, 30)

bordeaux = ms.Point(44.837788, -0.579180)

# Get daily data for 2018
data = ms.Monthly(bordeaux, start, end)
data = data.fetch()

data

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()


df = data.iloc[:,:4]

df
df = df.stack().reset_index()
df = df.T
df



