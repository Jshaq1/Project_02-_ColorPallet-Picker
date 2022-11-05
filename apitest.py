
import requests

url = "http://colormind.io/api/"
data = {
    "model": "default",
    "input": ["N", "N", "N", "N", "N"]
}
response = requests.post(url, json=data)
results = response.json()

colors = results['result']

generated_color = []
for row in colors:
    r, g, b = row
    generated_color.append([r,g,b])


print(generated_color)
    





    


# color = results['result'][0]
# r, g, b = color
# print(', '.join(str(color)))