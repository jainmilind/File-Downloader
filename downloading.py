import requests
def download(url , place):
    with open(place , 'wb') as f:
        response = requests.get(url, allow_redirects=True,stream=True)
        total_length = response.headers.get("content-length")
        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(100 * dl / total_length)
                #self.progressbar1.setvalue(done)
                print(done)
    # n = len(url)
    # k = '.png'
    # for i in range(n-1,-1,-1):
    #     if url[i] == '.':
    #         k = url[i:]
    #         break
