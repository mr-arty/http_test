import requests
import settings

def search_f(search_q, pn_q):
    page = (pn_q - 1) * 10 + 1
    URL = 'https://www.googleapis.com/customsearch/v1'
    payload = {'key':settings.API_key, 'cx':settings.cx, 'q':search_q, 'start':page}

    r=requests.get(URL, params = payload)
    r=r.json()
    
    for names in r['items']:
        print(names['title'], names['link'])

print('Input search term(s): ')
search = str(input())
print('Input starting page: ')
pn = int(input())

while pn != 0:
    search_f(search, pn)
    print('Input page number: ')
    pn = int(input())
