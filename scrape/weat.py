from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2000, 1, 1)
end = datetime(2000, 12, 31)

bordeaux = Point(44.837788, -0.579180)

# Get daily data for 2018
data = Daily(bordeaux, start, end)
data = data.fetch()

data

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()



