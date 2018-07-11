import requests

API_key = 'AIzaSyAIYQvQ91H5Xq2C-sh4xvJXWQ0sgLjy_3E'
cx = '007389025395420730419:n932aqs69xm'
query = 'concert'

URL = 'https://www.googleapis.com/customsearch/v1?key=' + API_key + '&cx=' + cx + '&q=' + query

#print(URL)

r = requests.get(URL)
print(r.content)
