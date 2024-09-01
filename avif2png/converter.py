from PIL import Image
import os
import pillow_avif

# Set the input and output directories
input_dir = 'input'
output_dir = 'output'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an AVIF image
    if filename.endswith('.avif'):
        # Open the AVIF image
        # 
        img = Image.open(os.path.join(input_dir, filename))
        png_filename = os.path.splitext(filename)[0] + '.png'
        img.save(os.path.join(output_dir, png_filename))
        
        print(f'Converted {filename} to {png_filename}')

# img = Image.open('input/image1_1.avif')
# img.save('output.png')
