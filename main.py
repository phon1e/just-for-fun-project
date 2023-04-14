from datetime import datetime
import requests

USERNAME = "phonie"
TOKEN = "hfjikdyh3jfh3jke"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",


}


# response = requests.post(url=pixela_endpoint, json=user_param)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name": " Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.today().strftime("%Y%m%d")
print(today)

graph_post = {
    "date": "20230406",
    "quantity": "9"
}

graph_post_endpt = graph_endpoint+ f"/{graph_config['id']}"

# response = requests.post(url=graph_post_endpt, json=graph_post, headers=headers)
# print(response.text)

graph_update = {
    "quantity": "2"
}

# response = requests.put(url=graph_post_endpt+"/20230406", json=graph_update, headers=headers)
# print(response.text)

response = requests.delete(url=graph_post_endpt+"/20230406", json=graph_update, headers=headers)
print(response.text)