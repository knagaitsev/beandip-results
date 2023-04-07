import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [0, 1000, 5000, 10000, 20000, 40000]
y_values = [
    [86932162000, 87032443400, 87320625200, 87627421800, 88164198800, 89215762200],
    [87928941600, 87955484800, 88085745200, 88276588000, 88468668200, 89080729400]
]
labels = ['BT (Hardware Ints.)', 'BT (BEANDIP)']

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the color scheme
colors = ['#a3c1ad', '#ffd6ba', '#ffe6e6', '#c2c2d6', '#f5b7b1', '#d2b4de']

# Iterate through each set of y values and plot the line
for i, y_values_i in enumerate(y_values):
    ax.plot(x_values, y_values_i, color=colors[i], label=labels[i], marker='s')

# Set the legend
ax.legend(loc='lower right', fontsize=13)

# Set the title and axis labels
ax.set_title('Runtime of BT, Hardware Ints. vs BEANDIP', fontsize=15)
ax.set_xlabel('Interrupts/second', fontsize=14)
ax.set_ylabel('Runtime', fontsize=14)

ax.tick_params(axis='both', labelsize=12)

# Set the y-axis to start at zero
# ax.set_ylim(bottom=0)

# ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

# ax.axhline(y=0, linestyle=':', color='grey')

# Show the plot
plt.show()
