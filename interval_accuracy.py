import matplotlib.pyplot as plt

# Create some sample data
x_values = [1000, 2000, 3000, 4000, 5000, 8000, 16000]
y_values = [
    [2057, 4178, 7421, 8738, 9334, 11322, 12647],
    [1551, 2783, 3997, 5044, 6225, 9886, 19602],
    [1984, 3471, 5235, 6322, 7853, 10504, 16273],
    [1643, 2437, 2909, 3061, 3208, 4350, 4636],
    [2534, 3644, 4279, 7277, 8179, 13499, 24914]
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
ax.set_title('Target poll interval vs. actual interval on RISC-V', fontsize=15)
ax.set_xlabel('Target poll interval (cycles)', fontsize=14)
ax.set_ylabel('Actual mean poll interval (cycles)', fontsize=14)

ax.tick_params(axis='both', labelsize=12)

# Set the y-axis to start at zero
ax.set_ylim(bottom=0)

# Show the plot
plt.show()
