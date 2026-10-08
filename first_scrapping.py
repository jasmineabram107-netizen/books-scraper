import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36'
}

base_url = "http://books.toscrape.com/"

# Scrape the listing page (first page, 20 books)
listing_url = base_url
response = requests.get(listing_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

books_data = []  # will store a dictionary for each book
books = soup.find_all('article', class_='product_pod')

for book in books:
    # Title and link
    title_tag = book.find('h3').find('a')
    title = title_tag.get('title', 'No title')
    detail_relative_url = title_tag.get('href')

    # Build full detail URL
    detail_url = urljoin(base_url, detail_relative_url)

    # Price
    price_tag = book.find('p', class_='price_color')
    price = price_tag.text if price_tag else 'No price'

    # Rating (class names: One, Two, Three, Four, Five)
    rating_tag = book.find('p', class_='star-rating')
    rating = rating_tag.get('class')[1] if rating_tag else 'Unknown'

    # Save basic info - description will be added later
    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Detail_URL': detail_url,
        'Description': None  # placeholder
    })

print(f"Found {len(books_data)} books on the first page")

# Save results to a CSV file
df = pd.DataFrame(books_data)
df.to_csv('books.csv', index=False)
print("Saved results to books.csv")