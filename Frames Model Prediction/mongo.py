from pymongo import MongoClient 
import base64
from bson import ObjectId

# Your mongoDB cluster/localhost connection URL
client = MongoClient('')

db = client['test']
collection = db['temp']

# Read the image as binary data
with open('photo.png', 'rb') as image_file:
    image_data = image_file.read()

# Convert binary data to base64
base64_image = base64.b64encode(image_data)

# Insert the image data into MongoDB

# retrieve the name from a document

# print all the fields in a document

# retrieval of image from MongoDB

# Convert the image data to binary

# Write the image data to a file
