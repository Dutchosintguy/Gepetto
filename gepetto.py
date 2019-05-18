# author : Yarienkiva
# version : 1.0
import requests
import base64, json, os
from PIL import Image
# import your face recon script instead of face_recon_azure
import face_recon_azure
# import random data generator
import skt
import uuid

# Get a new image from thispersondoesnotexist and save it
new_image = requests.get('https://thispersondoesnotexist.com/image', headers={"user-agent":"oui"})
uuid_image = str(uuid.uuid4())  + ".jpeg"
open('images/' + uuid_image, 'wb').write(new_image.content)

# Resize the image so the api doesn't time out
# not usefull with azure api
# resized_image = Image.open('images/tmp_image.jpeg').resize((400, 400), Image.ANTIALIAS)
# resized_image.save('images/tmp_image.jpeg')

try :
    # Get the age and gender then save the image with a unique id
    # make shure to return a gender:str and an age:int
    gender, age = face_recon_azure.ia_recon("images/"+ uuid_image)
    # I really don't want to generate minors
    if age > 18 :
        # Get random user data
        skt.faker_info(gender,age)
        # Show the new identity
        img = Image.open("images/" + uuid_image)
        img.show()
    else :
        print("Please don't use this on minors : I'm calling the loli police")
except :
    os.remove("images/" + uuid_image)
    print("API error : most likely a rate limit hit")
