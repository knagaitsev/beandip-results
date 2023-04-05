import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [0, 1000, 5000, 10000, 20000, 40000]
y_values = [
    [0.0, 0.78369328, 3.796977308, 7.582139841, 15.49588381, 32.39532717],
    [0.0, 0.5143983658, 2.506887165, 4.950873926, 10.236731, 21.40132551]
]
labels = ['BT', 'EP']

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the color scheme
colors = ['#a3c1ad', '#d6d5e6', '#ffd6ba', '#ffe6e6', '#c2c2d6', '#f5b7b1', '#d2b4de']

# Iterate through each set of y values and plot the line
for i, y_values_i in enumerate(y_values):
    ax.plot(x_values, y_values_i, color=colors[i], label=labels[i], marker='s')

# Set the legend
ax.legend(loc='lower right')

# Set the title and axis labels
ax.set_title('Hit rate percentage of BEANDIP polls')
ax.set_xlabel('Interrupts/second')
ax.set_ylabel('Hit rate percentage')

# Set the y-axis to start at zero
ax.set_ylim(bottom=0)

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

# Show the plot
plt.show()
