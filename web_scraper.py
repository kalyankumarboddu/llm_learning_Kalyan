import requests
from requests.exceptions import InvalidURL,MissingSchema
from bs4 import BeautifulSoup


def webpage_content(url,header):
    try:
        resp = requests.get(url=url, headers=header)
        resp.raise_for_status()
    except InvalidURL as e:
        print(f"{url} raised an exception")
        return None
    except MissingSchema as e:
        print(f"{url} raise missing schema exception")
        return None
    except Exception as e:
        print(f"{url} raised an general exception")
        return None
    
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.title.string if soup.title else "No-title"

    if soup.body:
        for decom in soup.body(["img","path","ellipse","input","span","nav","link","script","style"]):
            decom.decompose()
        text = soup.body.get_text()
    else:
        text = " "

    return(title + "\n" + text)[:2000]


def fetch_website_url(url,header):
    try:
        resp = requests.get(url=url, headers=header)
        resp.raise_for_status()
    except InvalidURL as e:
        print(f"{url} raised an exception")
        return None
    except MissingSchema as e:
        print(f"{url} raise missing schema exception")
        return None
    except Exception as e:
        print(f"{url} raised an general exception")
        return None
    
    soup = BeautifulSoup(resp.content, "html.parser")

    title = soup.title.string if soup.title else "No-title"
    
    url_links = [ele.get("href") for ele in soup.find_all('a')]

    return(title + "\n" + str(url_links))[:2000]