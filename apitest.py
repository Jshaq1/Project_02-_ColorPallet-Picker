
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

col = ', '.join(str(row) for row in generated_color)
print(col)
    

test = '[[24, 30, 28], [96, 130, 92], [188, 170, 141], [171, 149, 89], [46, 21, 18]]'
print(test.split(''))




    


# color = results['result'][0]
# r, g, b = color
# print(', '.join(str(color)))