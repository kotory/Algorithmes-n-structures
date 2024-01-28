import requests
from pprint import pprint

username = input('Введите название репозитория:')
url = f'https://api.github.com/users/{username}'
data = requests.get(url).json()
user_data = {
    'company': data['company'],
    'created_at': data['created_at'],
    'email': data['email'],
    'id': data['id'],
    'name': data['name'],
    'url': data['url']
    }

pprint(user_data)
