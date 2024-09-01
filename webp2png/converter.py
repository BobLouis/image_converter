from PIL import Image
import os

# Set the input and output directories
input_dir = 'input'
output_dir = 'output'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a WebP image
    if filename.endswith('.webp'):
        # Open the WebP image
        webp_image = Image.open(os.path.join(input_dir, filename))
        
        # Convert the image to PNG format
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_image = webp_image.convert('RGB')
        png_image.save(os.path.join(output_dir, png_filename))
        
        # Close the image
        webp_image.close()
        
        print(f'Converted {filename} to {png_filename}')
