import requests
from bs4 import BeautifulSoup
import pandas as pd
# User-Agent and Accept-Language headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Accept-Language': 'en-us,en;q=0.5'
}

comments = []

for i in range(1, 10):
    # Construct the URL for the current page
    # https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/p/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&fm=organic&ppt=dynamic&ppn=dynamic&ssid=smencraz9c0000001725339457583
    url = "https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/product-reviews/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&lid=LSTMOBGQFX672GDDQAQSSIAM2&marketplace=FLIPKART&page="+str(i)

    # Send a GET request to the page
    page = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract Comments
    cmt = soup.find_all('div', class_='ZmyHeo')
    for c in cmt:
        comment_text = c.div.div.get_text(strip=True)
        comments.append(comment_text)
print(comments)
    


