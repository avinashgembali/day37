import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "walking graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)

# POSTING A PIXEL
post_pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
# date = datetime.now()
date = datetime(year=2024, month=8, day=28)
# print(date.strftime("%Y%m%d"))
pixel_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("how many kilometer did you walk")
}

post_pixel_response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=graph_header)

# UPDATING A PIXEL
update_pixel_endpoint = f"{post_pixel_endpoint}/{date.strftime("%Y%m%d")}"

update_pixel_params = {
    "quantity": "4.2"
}

update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=graph_header)

# DELETING A PIXEL
delete_pixel_endpoint = f"{post_pixel_endpoint}/{date.strftime("%Y%m%d")}"

delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=graph_header)
