import requests

def download(url, num_retries =2):
    # print("Dowload" + url)
    page = None
    try:
       response = requests.get(url)
       page = response.text
    except:
        print("error")

    return page

# page = download('http://www.google.com/')
# print(page)