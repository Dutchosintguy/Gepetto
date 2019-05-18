import json
import requests

def ia_recon(image_path):
    f = open(image_path, "rb")
    face_api_data = f.read()
    f.close()

    # Request URL, this will depend on the server you chose when you created the
    face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'
    api_key = ""

    # Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
    face_api_headers = {
        'Content-type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': api_key,
    }

    # We need the gender and the age of the person
    face_api_params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender',
    }

    # REST Call
    response = requests.post(face_api_url, data=face_api_data, headers=face_api_headers, params=face_api_params)
    response_data = response.json()[0]["faceAttributes"]
    gender = str(response_data["gender"])
    age = int(response_data["age"])

    return gender, age
