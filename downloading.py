import requests
def download(url,place):
    r = requests.get(url, allow_redirects=True)
    n = len(url)
    k = '.png'
    for i in range(n-1,-1,-1):
        if url[i] == '.':
            k = url[i:]
            break
    with open (place + k, 'wb') as file:
        file.write(r.content)