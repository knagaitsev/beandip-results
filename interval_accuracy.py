import matplotlib.pyplot as plt

# Create some sample data
x_values = [1000, 2000, 3000, 4000, 5000, 8000, 16000]
y_values = [
    [2057, 4178, 7421, 8738, 9334, 11322, 12647],
    [1551, 2783, 3997, 5044, 6225, 9886, 19602]
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
ax.set_title('Target poll interval vs. actual interval on RISC-V')
ax.set_xlabel('Target poll interval (cycles)')
ax.set_ylabel('Actual mean poll interval (cycles)')

# Set the y-axis to start at zero
ax.set_ylim(bottom=0)

# Show the plot
plt.show()
