# Importing necessary libraries for drawing
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Setting up the figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Drawing a generic MFD screen
ax.add_patch(Rectangle((10, 10), 80, 80, edgecolor='black', facecolor='none'))

# Adding a search bar at the top
ax.add_patch(Rectangle((20, 80), 60, 5, edgecolor='black', facecolor='lightgray'))
ax.text(22, 81, 'Search for a fish species...', va='center', ha='left', fontsize=8)

# Adding sections for fish information: photo, name, and details
# This represents a user having searched for "Tarakihi" and viewing the fish information
ax.add_patch(Rectangle((20, 50), 15, 10, edgecolor='black', facecolor='lightblue'))  # Photo placeholder
ax.text(20, 48, 'Tarakihi', fontsize=8, weight='bold')

# Adding details next to the photo
detail_text = "Nemadactylus macropterus\nSize: 30-50 cm\nWeight: 1-3 kg\nHabitat: Coastal NZ"
ax.text(37, 55, detail_text, va='top', ha='left', fontsize=8)

# Displaying buttons for navigation at the bottom
button_texts = ['Home', 'Back', 'Info', 'Log Catch']
for i, text in enumerate(button_texts):
    ax.add_patch(Rectangle((20 + i*15, 20), 10, 5, edgecolor='black', facecolor='lightblue'))
    ax.text(25 + i*15, 22.5, text, va='center', ha='center', fontsize=8)

# Setting up the plot
ax.set_aspect('equal', 'box')
ax.axis('off')
plt.title("Concept Sketch for Fish Encyclopedia Interface")
plt.show()
