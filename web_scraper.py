import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.info("Test INFO logging started")

def fetch_website_contents(url):

    # url = "https://realpython.com/python-requests/"
    headers = {
        "User-Agents": "Kalyan Chrome Browser"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        #Requests will raise this error if response between 400 and 600
        logging.error("HTTP error occurred: {}".format(http_err))
    else:
        logging.info("Response success for the URL: {}".format(url))

    return response.content

    # logging.info("Response to Text")
    # print(response.text)

    # logging.info("Response to JSON")
    # print(response.json())

    # logging.info("Response to Bytes")
    # print(response.content)




def website_scraper(resp_content):
    resp = resp_content

    soup = BeautifulSoup(resp, "html.parser")
    # print(soup.prettify())

    # print([ele.get_text().strip() for ele in soup.find_all("p")])

    # print([ele.get_text().strip() for ele in soup.find_all("p",class_="is-small has-text-grey")])

    title = soup.find("title").get_text().strip()

    href_attr_list = [ele["href"] for ele in soup.find_all("a")]
    return title + " " + str([link for link in href_attr_list if link])
