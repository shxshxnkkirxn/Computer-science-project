import requests
from bs4 import BeautifulSoup

# Get CSRF token from the signup page
signup_url = 'http://127.0.0.1:8000/signup/'
response = requests.get(signup_url)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

# Function to sign up a user
def signup_user(username, first_name, last_name, email, password):
    url = signup_url
    data = {
        'csrfmiddlewaretoken': csrf_token,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password 
    }
    response = requests.post(url, data=data)
    print(f'Status code for {username}: {response.status_code}')

# Generate usernames and sign up users
num_users = 8000
for i in range(1, num_users + 1):
    username = f'user{i}'
    first_name = f'First{i}'
    last_name = f'Last{i}'
    email = f'email{i}@abc.com'
    password = f'password{i}'
    signup_user(username, first_name, last_name, email, password)
