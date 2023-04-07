import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [0, 1000, 5000, 10000, 20000, 40000]
y_values = [
    [0.0, 0.78369328, 3.796977308, 7.582139841, 15.49588381, 32.39532717],
    [0.0, 0.5143983658, 2.506887165, 4.950873926, 10.236731, 21.40132551],
    [0.0, 0.6121729887, 2.983724492, 6.060514179, 12.37438166, 25.14508973],
    [0.0, 0.3182275367, 1.550576419, 3.102954671, 6.332898638, 13.19582744],
    [0.0, 0.6532788942, 3.184475592, 6.364700248, 13.01015345, 27.20431449]
]
labels = ['BT', 'EP', 'MG', 'FT', 'LU']

order = [3, 1, 0, 2, 4]

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the color scheme
colors = ['#8B7D7B', '#6B8E23', '#CD5C5C', '#4682B4', '#DAA520', '#2F4F4F', '#D2691E', '#1E90FF']

# Iterate through each set of y values and plot the line
for i in order:
    ax.plot(x_values, y_values[i], color=colors[i], label=labels[i], marker='s')

# Set the legend
ax.legend(loc='upper left', fontsize=13)

# Set the title and axis labels
ax.set_title('Hit rate percentage of BEANDIP polls', fontsize=15)
ax.set_xlabel('Interrupts/second', fontsize=14)
ax.set_ylabel('Hit rate percentage', fontsize=14)

ax.tick_params(axis='both', labelsize=12)

# Set the y-axis to start at zero
ax.set_ylim(bottom=0)

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

# Show the plot
plt.show()
