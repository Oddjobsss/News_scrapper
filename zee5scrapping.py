import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.zee5.com/news'

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all news cards
    news_cards = soup.find_all('div', class_='latestEpisodeCard')

    if news_cards:
        for card in news_cards:
            title = card.find('h3', class_='cardTitleMultiline')
            link_relative = card.find('a')['href'] if card.find('a') else None

            if title and link_relative:
                # Join the relative link with the base URL
                link = urljoin(url, link_relative)

                print("Title:", title.text.strip())
                print("Link:", link)
                print("---")
            else:
                print("Incomplete information for a news card.")
    else:
        print("No news cards found on the page.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
