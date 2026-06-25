
import math

def generate_textured_football(radius_x=28, radius_y=14):
    # Shading textures
    # Dark patches (Pentagons) use heavy blocks
    dark_patch = "██" 
    # Light patches (Hexagons) use lighter textures to create contrast
    light_patch = "░░"
    # Seamless spaces for the background
    background = "  "
    # Ball outline
    border = "::"

    output = []
    
    # Grid loop (Step by 1 for X, but we use double characters to fix terminal aspect ratio)
    for y in range(-radius_y, radius_y + 1):
        row = ""
        for x in range(-radius_x, radius_x + 1):
            # Normalize coordinates for a perfect circle calculation
            nx = x / radius_x
            ny = y / radius_y
            dist_sq = nx**2 + ny**2
            
            if dist_sq <= 1.0:
                # 3D spherical projection to warp the panels naturally around the edges
                z = math.sqrt(1.0 - dist_sq)
                longitude = math.atan2(nx, z)
                latitude = math.asin(ny)
                
                # Frequency multiplier to scale the size of the football panels
                # Adjusting these numbers changes how many patches fit on the ball
                patch_x = int((longitude + math.pi) * 3.8)
                patch_y = int((latitude + math.pi/2) * 3.2)
                
                # Checkered logic to separate the patches
                if (patch_x + patch_y) % 2 == 0:
                    row += dark_patch
                else:
                    row += light_patch
            else:
                # Smooth outer edge boundary
                if dist_sq <= 1.06:
                    row += border
                else:
                    row += background
        output.append(row)
        
    return "\n".join(output)

if __name__ == "__main__":
    print("\n" + "="*30 + " ASCII SOCCER BALL " + "="*30 + "\n")
    football = generate_textured_football(radius_x=24, radius_y=13)
    print(football)
    print("\n" + "="*71)