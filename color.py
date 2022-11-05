import requests

# def pallet_generator():
# 	url = "http://colormind.io/api/"
# 	data = {
# 		"model" : "default",
# 		"input" : [[44,43,44],[90,83,82],"N","N","N"]
# 	}

# 	response = requests.post(url, json=data)
# 	print(response.json())

# 	print()

# 	return response.json()

def color_api():
	url = "http://colormind.io/api/"
	data = {
		"model" : "default",
		"input" : ["N","N","N","N","N"]
	}

	response = requests.post(url, json=data)
	results  = response.json()
	color1 = results['result']
	color2 = results['result'][1]
	color3 = results['result'][2]
	color4 = results['result'][3]
	color5 = results['result'][4]

	i = 0
	for row in results['result']:
	


def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

	


	


	

