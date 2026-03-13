import requests

# Create a short URL
response = requests.post('http://127.0.0.1:5000/shorten', json={'url': 'https://google.com'})
print("Response:", response.json())
print("\nNow open the short_url in your browser!")
