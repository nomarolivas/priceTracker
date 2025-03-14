import requests
from bs4 import BeautifulSoup

URL= "https://www.grailed.com/listings/75937177-yeezy-season-yeezy-season-6-glacier-work-jacket" \
""

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

def get_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Need to find price element (Not working)
    price_tag = soup.find("span", {"class": "price-class"})
    if price_tag:
        price = float(price_tag.text.replace("$", "").replace(",", ""))
        return price
    return None

# Test
print(get_price())