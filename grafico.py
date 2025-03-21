import numpy as np
import matplotlib.pyplot as plt


# Data for the 2D bar graphs (population data for the years 1970, 1980, 1990, 2000, and 2020)
under_18_population = [13267610, 12401400, 9344252, 8156572, 7720883]  # Under 18 population for the years
total_population = [53821850, 56433880, 56719240, 56942110, 59449530]  # Total population for the years

# Years to plot (1970, 1980, 1990, 2000, 2020)
years = ["1970", "1980", "1990", "2000", "2020"]

# Set the bar width and positions (numerical values for plotting)
x = np.arange(len(years))  # Numeric positions for years (0 to 4)

# Set the bar width
width = 0.4

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting the second 2D bar graph (Population under 18 for each year)
ax.bar3d(x, np.zeros_like(x), np.zeros_like(x), width, width, under_18_population, color='g', label='Population under 18')

# Plotting the first 2D bar graph (Total population for each year)
ax.bar3d(x + 1.5 * width, np.ones_like(x), np.zeros_like(x), width, width, total_population, color='b', label='Total Population')

# Setting labels for the axes
ax.set_xlabel('Year')
ax.set_ylabel('Category (0: Under 18, 1: Total Population)')
ax.set_zlabel('Population')

# Set ticks and labels for the x-axis (using year names)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=10)  # Use year names for labels on x-axis

# Add a legend
ax.legend()

# Show the plot
plt.show()