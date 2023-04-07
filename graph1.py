import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [0, 1000, 5000, 10000, 20000, 40000]
y_values = [
    [1.14661775, 1.060571626, 0.8762191043, 0.7408254022, 0.3453435795, -0.1513553173],
    [3.493020836, 3.411394111, 3.350234873, 3.272015881, 3.12378268, 2.796719863],
    [-0.928088501, -0.5164112601, -0.439198961, -0.08769302767, 0.2177053493, 0.3564403376],
    [11.20650395, 11.0255124, 10.87133631, 10.67769941, 10.38293369, 10.01808202],
    [-1.156590331, -1.190178663, -1.301925667, -1.404762001, -1.570331464, -1.888753561]
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
ax.legend(loc='upper right', fontsize=13)

# Set the title and axis labels
ax.set_title('% Overhead of BEANDIP relative to Hardware Interrupts', fontsize=15)
ax.set_xlabel('Interrupts/second', fontsize=14)
ax.set_ylabel('Overhead Percentage', fontsize=14)

ax.tick_params(axis='both', labelsize=12)

# Set the y-axis to start at zero
# ax.set_ylim(bottom=0)

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

ax.axhline(y=0, linestyle=':', color='grey')

# Show the plot
plt.show()
