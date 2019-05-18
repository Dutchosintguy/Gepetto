import requests
import base64

# Just use whatever you want api/AI wise
# just make sure to return a gender and an age

def ia_recon(image_path):
    face_api_data = base64.b64encode(open(str(image_path),'rb').read())
    face_api_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    api_key = ""
    api_secret = ""

    face_api_params = {
                'api_key': api_key,
                'api_secret': api_secret,
                'image_base64':face_api_data,
                'return_attributes': 'gender,age'
                }

    response = requests.post(face_api_url, data=face_api_params)

    r = response.json()["faces"][0]["attributes"]
    gender = r["gender"]["value"].lower()
    age = int(r["age"]["value"])

    return gender, age
