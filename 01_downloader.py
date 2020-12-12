import requests 

base_url = 'https://galileoguzman.com/data/articles_data_homeproject.csv'

response = requests.get(base_url)
response.raise_for_status() #termina el programa si no encuentra status 200

response_content = response.content
filename = 'dataset/articles_data_homeproject.csv'

with open(filename, 'wb') as csv_file:
    csv_file.write(response_content)

print('File downloaded')