import matplotlib.pyplot as plt
import numpy as np

# create data for the bars
values = np.array([2858, 72, 64]) # example data

# create a figure and axis object
fig, ax = plt.subplots()

# create the bar graph
ax.bar(np.arange(len(values)), values, color='#5891ae')

# set the x-tick labels
labels = ['GPIO High\nto Interrupt', 'PLIC claim hit', 'PLIC claim miss'] # example labels
ax.set_xticks(np.arange(len(values)))
ax.set_xticklabels(labels, fontsize=16) # increase font size

# set the value labels above each bar
for i, v in enumerate(values):
    ax.text(i, v + 40, str(v), ha='center', fontsize=20) # increase font size

# add light vertical lines in the background
ax.grid(axis='y', alpha=0.3, linestyle='--')

ax.set_ylim([0, 3500])

# increase font size of axis labels and values
ax.tick_params(axis='both', labelsize=18) # increase font size

plt.subplots_adjust(top=0.85)

# display the graph
plt.show()
