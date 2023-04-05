import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [1000, 2000, 3000, 4000, 5000, 8000, 16000]
y_values = [
    [0.2090158531, 0.2568251629, 0.2559589702, 0.2304078208, 0.2318485994, 0.3851718884, 0.3838610003],
    [3.225889853, 2.944143277, 2.890934794, 2.756591557, 2.706776469, 2.665211373, 2.620885211]
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
ax.set_title('% Overhead of Compiler Instrumentation Alone')
ax.set_xlabel('Target poll interval (cycles)')
ax.set_ylabel('Overhead Percentage')

# Set the y-axis to start at zero
ax.set_ylim(bottom=0)

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

# Show the plot
plt.show()
