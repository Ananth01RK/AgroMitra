import requests

test_file = open("F:\\tomoto deasease detection\\Project\\Tomoto diesease detection\\Data\\train\\Bacterial_spot\\0c09c121-e945-4b7e-acbf-dff4e0d01acb___GCREC_Bact.Sp 3379.jpg", 'rb')
r = requests.post('http://127.0.0.1:5000//recognisediesease', files={'file': test_file})

print(r.text)