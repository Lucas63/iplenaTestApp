import os

import requests

# Function to send image via POST request
def upload_sit_photo(base_url, image_file):
    url = f"{base_url}/ai/upload_sit"
    payload = {}
    files = [
        ('file[]', (image_file.name, image_file, f'image/{os.path.splitext(image_file.name[1])}'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()[0]


def upload_right_side_photo(base_url, image_file):
    url = f"{base_url}/ai/upload_right_side"
    payload = {}
    files = [
        ('file[]', (image_file.name, image_file, f'image/{os.path.splitext(image_file.name[1])}'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()

def upload_front_photo(base_url, image_file):
    url = f"{base_url}/ai/upload_front"
    payload = {}
    files = [
        ('file[]', (image_file.name, image_file, f'image/{os.path.splitext(image_file.name[1])}'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()[0]

def get_spine(base_url,
              side_photo_feature_points,
              side_photo_keypoints_3d_denormalized,
              front_photo_keypoints_2d):
    data = {
        "side_photo_feature_points": side_photo_feature_points,
        "side_photo_keypoints_3d_denormalized": side_photo_keypoints_3d_denormalized,
        "front_photo_keypoints_2d": front_photo_keypoints_2d
    }

    r = requests.post(f"{base_url}/ai/get_spine", json=data)
    print(f"{base_url}/ai/get_spine")

    try:
        response_dict = r.json()[0]
    except:
        response_dict = {}
    return response_dict



