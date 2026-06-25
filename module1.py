import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_bangladesh_flag():
    # Official proportions: width=10, height=6
    width = 10
    height = 6
    
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 1. Draw the bottle green background
    # Official hex color approximation for Bangladesh green is #006a4e
    green_bg = patches.Rectangle((0, 0), width, height, color='#006a4e')
    ax.add_patch(green_bg)
    
    # 2. Draw the red circle
    # Radius is 1/5 of the length (10 / 5 = 2)
    # Center is at 9/20 of the length (4.5) and 1/2 of the height (3.0)
    radius = 2
    center_x = 4.5
    center_y = 3.0
    
    # Official hex color approximation for Bangladesh red is #f42a41
    red_circle = patches.Circle((center_x, center_y), radius, color='#f42a41')
    ax.add_patch(red_circle)
    
    # Clean up the plot display
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide grid lines and axes
    
    # Display the flag
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_bangladesh_flag()