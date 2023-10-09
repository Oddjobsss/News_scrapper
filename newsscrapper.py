from requests_html import HTMLSession
from urllib.parse import urljoin

session = HTMLSession()

r = session.get('https://zeenews.india.com/latest-news')

# Render the JavaScript on the page
r.html.render(sleep=1, timeout=30)

# Use requests_html's HTML parsing capabilities
for li_tag in r.html.find('li'):
    article_tag = li_tag.find('div.article-tag', first=True)
    news_desc = li_tag.find('div.news_description', first=True)

    # Check if both elements are found
    if article_tag and news_desc:
        tag = article_tag.text.strip()
        title = news_desc.find('h2', first=True).text.strip()
        
        # Extract the relative link
        relative_link = news_desc.find('a', first=True).attrs['href']

        # Join the relative link with the base URL
        link = urljoin(r.url, relative_link)

        print(f"Tag: {tag}\nTitle: {title}\nLink: {link}\n---")
    else:
        pass
