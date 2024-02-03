import matplotlib.pyplot as plt
import numpy as np

# Data
classes = ['X-A', 'X-B', 'X-C']
physics = [90, 89, 95]
chemistry = [87, 95, 82]
biology = [92, 85, 77]

# Calculate average percentage for each class
average_percentage = np.mean([physics, chemistry, biology], axis=0)

# Bar positions
bar_positions = np.arange(len(classes))

# Bar width
bar_width = 0.2

# Plotting the bar chart
fig, ax = plt.subplots()
bar1 = ax.bar(bar_positions - bar_width, physics, width=bar_width, color='blue', label='Physics')
bar2 = ax.bar(bar_positions, chemistry, width=bar_width, color='red', label='Chemistry')
bar3 = ax.bar(bar_positions + bar_width, biology, width=bar_width, color='green', label='Biology')

# Add average percentage as text on top of each bar
for i, value in enumerate(average_percentage):
    ax.text(bar_positions[i] - 0.1, value + 1, f'{value:.2f}', ha='center', va='bottom')

# Title and labels
ax.set_title('Performance in PCB Group')
ax.set_xlabel('Class')
ax.set_ylabel('Percentage')

# Set x-axis ticks and labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(classes)

# Show legends
ax.legend()

# Display the plot
plt.show()
