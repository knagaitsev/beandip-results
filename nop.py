import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Create some sample data
x_values = [1000, 2000, 3000, 4000, 5000, 8000, 16000]
y_values = [
    [0.2090158531, 0.2568251629, 0.2559589702, 0.2304078208, 0.2318485994, 0.3851718884, 0.3838610003],
    [3.225889853, 2.944143277, 2.890934794, 2.756591557, 2.706776469, 2.665211373, 2.620885211],
    [0.7365843523, -0.4576441906, 0.0186774917, -0.01921843735, -0.06228334462, -0.09312507117, 0.03513903633],
    [8.427762187, 8.071897465, 8.388870576, 8.048823503, 7.901841534, 8.110673383, 7.765734778],
    [-2.871870001, -2.293079374, -1.90605789, -1.845426765, -1.925396692, -1.839554611, -1.966187157]
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
ax.set_title('% Overhead of Compiler Instrumentation vs. Baseline', fontsize=15)
ax.set_xlabel('Target poll interval (cycles)', fontsize=14)
ax.set_ylabel('Overhead Percentage', fontsize=14)

ax.tick_params(axis='both', labelsize=12)

# Set the y-axis to start at zero
# ax.set_ylim(bottom=0)

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))

ax.axhline(y=0, linestyle=':', color='grey')

# Show the plot
plt.show()
