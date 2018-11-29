import requests

articles = requests.get('https://jsonplaceholder.typicode.com/posts')
values = articles.json()

print(values[2]['title'])

for i in range(len(values)):
    print('The News Title {} And the body {}'.format(values[i]['title'],values[i]['body']))

