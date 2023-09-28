from pymongo import MongoClient 
import base64
from bson import ObjectId

client = MongoClient('')

db = client['test']
collection = db['temp']

# Read the image as binary data
with open('photo.png', 'rb') as image_file:
    image_data = image_file.read()

# Convert binary data to base64
base64_image = base64.b64encode(image_data)

# Insert the image data into MongoDB
insert_id = collection.insert_one({"name": "Naimish", "image": base64_image})
print(insert_id.inserted_id)

# # retrieve the name from a document
# retrieved_name = collection.find_one({"_id": ObjectId("64d21be959ea5968d3b601bf")})
# print(retrieved_name)

# # print all the fields in a document
# for key in retrieved_name:
#     print(key)






# # retrieval of image from MongoDB
# retrieved_image = collection.find_one({"_id": ObjectId('64d21ec219b95645ff88422b')})

# # Convert the image data to binary
# retrieved_image = base64.b64decode(retrieved_image['image'])

# # Write the image data to a file
# with open('retrieved_image.png', 'wb') as image_file:
#     image_file.write(retrieved_image)
