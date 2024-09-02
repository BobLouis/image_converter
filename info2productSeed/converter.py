import uuid
import json
from datetime import datetime

id = 0
img_type = 'png'
brand = 'trassardi'
category_id = '7b1cb5b8-0041-4fd8-a7a5-252f58bc36a9'

# Function to generate unique IDs using uuidv4
def generate_uuid():
    return str(uuid.uuid4())

# Function to create product objects with the desired format
def create_product_object(name, description):
    return {
        "id": generate_uuid(),  # Generate UUIDv4
        "title": name,
        "brandId": "7c93c391-924d-476e-9bb7-a668aa1282fb",
        "meta_description": "Beautifully designed web application template built with React and Bootstrap to create modern apps and speed up development",
        "keywords": "flatlogic, react templates",
        "meta_author": "Flatlogic LLC.",
        "meta_og_title": "Flatlogic - React, Vue, Angular and Bootstrap Templates and Admin Dashboard Themes",
        "meta_og_url": "https://flatlogic-ecommerce.herokuapp.com/",
        "meta_og_image": "https://flatlogic-ecommerce-backend.herokuapp.com/images/blogs/content_image_six.jpg",
        "meta_fb_id": "712557339116053",
        "meta_og_sitename": "Flatlogic",
        "post_twitter": "@flatlogic",
        "price": 3000,
        "discount": 0,
        "description": description,
        "rating": 4,
        "status": "in stock",
        "createdAt": "new Date()",
        "updatedAt": "new Date()"
    }

# Function to create category objects
def create_category_object(product_id):
    return {
        "createdAt": "new Date()",
        "updatedAt": "new Date()",
        "productId": f'"{product_id}"',
        "categoryId": f"'{category_id}'"
    }

# Function to create file objects
def create_file_object(product_id):
    global id  
    id += 1
    return {
        "belongsTo": "products",
        "belongsToColumn": "image",
        "belongsToId": f'"{product_id}"',
        "createdById": "null",
        "deletedAt": "null",
        "id": generate_uuid(),
        "name": f"image{id}_1.{img_type}",
        "privateUrl": f"https://raw.githubusercontent.com/BobLouis/juxin_{brand}/master/image/image{id}_1.{img_type}",
        "publicUrl": f"https://raw.githubusercontent.com/BobLouis/juxin_{brand}/master/image/image{id}_1.{img_type}",
        "sizeInBytes": 2012,
        "updatedById": "null",
        "createdAt": "new Date()",
        "updatedAt": "new Date()"
    }

# Read the input data from info.txt
with open('info.txt', 'r') as file:
    input_data = file.read()

# Split the data into items by 'id:' (ignoring the first empty split)
items = input_data.split('id:')[1:]

# Parse the items into a structured format
input_list = []
for item in items:
    try:
        id_part, rest = item.split('name:', 1)
        name_part, description_part = rest.split('description:', 1)
        name = name_part.strip().strip('"')
        description = description_part.strip().strip('"').replace('\n', ' ')
        
        input_list.append({
            'name': name,
            'description': description
        })
    except ValueError:
        print("Skipping malformed entry")

# Prepare the product, category, and file lists
product_list = []
category_list = []
file_list = []

for item in input_list:
    product = create_product_object(item['name'], item['description'])
    product_list.append(product)
    # Create corresponding category object
    category = create_category_object(product['id'])
    category_list.append(category)
    # Create corresponding file object
    file = create_file_object(product['id'])
    file_list.append(file)

# Save the product list in the desired format
with open('product.json', 'w') as product_file:
    product_file.write('[\n')
    for idx, product in enumerate(product_list):
        # Format each product object in the desired JavaScript-like format
        product_file.write('  {\n')
        product_file.write(f'    id: "{product["id"]}",\n')
        product_file.write(f'    title: "{product["title"]}",\n')
        product_file.write(f'    brandId: "{product["brandId"]}",\n')
        product_file.write(f'    meta_description: "{product["meta_description"]}",\n')
        product_file.write(f'    keywords: "{product["keywords"]}",\n')
        product_file.write(f'    meta_author: "{product["meta_author"]}",\n')
        product_file.write(f'    meta_og_title: "{product["meta_og_title"]}",\n')
        product_file.write(f'    meta_og_url: "{product["meta_og_url"]}",\n')
        product_file.write(f'    meta_og_image: "{product["meta_og_image"]}",\n')
        product_file.write(f'    meta_fb_id: "{product["meta_fb_id"]}",\n')
        product_file.write(f'    meta_og_sitename: "{product["meta_og_sitename"]}",\n')
        product_file.write(f'    post_twitter: "{product["post_twitter"]}",\n')
        product_file.write(f'    price: {product["price"]},\n')
        product_file.write(f'    discount: {product["discount"]},\n')
        product_file.write(f'    description: "{product["description"]}",\n')
        product_file.write(f'    rating: {product["rating"]},\n')
        product_file.write(f'    status: "{product["status"]}",\n')
        product_file.write(f'    createdAt: {product["createdAt"]},\n')
        product_file.write(f'    updatedAt: {product["updatedAt"]}\n')
        if idx < len(product_list) - 1:
            product_file.write('  },\n')
        else:
            product_file.write('  }\n')
    product_file.write(']\n')

# Save the category list in the desired format
with open('category.json', 'w') as category_file:
    category_file.write('[\n')
    for idx, category in enumerate(category_list):
        # Format each category object in the desired JavaScript-like format
        category_file.write('  {\n')
        category_file.write(f'    createdAt: {category["createdAt"]},\n')
        category_file.write(f'    updatedAt: {category["updatedAt"]},\n')
        category_file.write(f'    productId: {category["productId"]},\n')
        category_file.write(f'    categoryId: {category["categoryId"]}\n')
        if idx < len(category_list) - 1:
            category_file.write('  },\n')
        else:
            category_file.write('  }\n')
    category_file.write(']\n')

# Save the file list in the desired format
with open('file.json', 'w') as file_output:
    file_output.write('[\n')
    for idx, file in enumerate(file_list):
        # Format each file object in the desired JavaScript-like format
        file_output.write('  {\n')
        file_output.write(f'    belongsTo: "{file["belongsTo"]}",\n')
        file_output.write(f'    belongsToColumn: "{file["belongsToColumn"]}",\n')
        file_output.write(f'    belongsToId: {file["belongsToId"]},\n')
        file_output.write(f'    createdById: {file["createdById"]},\n')
        file_output.write(f'    deletedAt: {file["deletedAt"]},\n')
        file_output.write(f'    id: uuidv4(),\n')
        file_output.write(f'    name: "{file["name"]}",\n')
        file_output.write(f'    privateUrl: "{file["privateUrl"]}",\n')
        file_output.write(f'    publicUrl: "{file["publicUrl"]}",\n')
        file_output.write(f'    sizeInBytes: {file["sizeInBytes"]},\n')
        file_output.write(f'    updatedById: {file["updatedById"]},\n')
        file_output.write(f'    createdAt: {file["createdAt"]},\n')
        file_output.write(f'    updatedAt: {file["updatedAt"]}\n')
        if idx < len(file_list) - 1:
            file_output.write('  },\n')
        else:
            file_output.write('  }\n')
    file_output.write(']\n')

print("Output successfully generated in product.json, category.json, and file.json")
