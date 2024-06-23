import requests
from datetime import datetime
from day_37_creds import username, headers

pixela_endpoint = 'https://pixe.la/v1/users'

user_params ={
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

###Create User
# response = requests.post(url=pixela_endpoint,json=user_params)

# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",

}



today = datetime.now()
today_formated = today.strftime("%Y%m%d")

pixel_data ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "0.5"
 }

###Create Graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

publish_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"

# response = requests.post(url=publish_endpoint, json=pixel_data, headers=headers)

# print(response.text)

### Update a pixel

pixel_data_update_params = {
    "quantity": "0.75"
}

update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today_formated}"

response = requests.put(url=update_pixel_endpoint,json=pixel_data_update_params,headers=headers)

print(response.text)