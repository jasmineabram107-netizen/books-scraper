import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36'
}

base_url = "http://books.toscrape.com/catalogue/"

books_data = []  # will store a dictionary for each book

# Scrape all 50 listing pages (20 books per page)
for page_number in range(1, 51):
    page_url = f"{base_url}page-{page_number}.html"
    response = requests.get(page_url, headers=headers)

    # Stop if the page doesn't exist
    if response.status_code != 200:
        print(f"Page {page_number} not found, stopping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # Title and link
        title_tag = book.find('h3').find('a')
        title = title_tag.get('title', 'No title')
        detail_relative_url = title_tag.get('href')

        # Build full detail URL
        detail_url = urljoin(page_url, detail_relative_url)

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

    print(f"Page {page_number}: total {len(books_data)} books so far")

    # Wait 1 second between pages to be polite to the website
    time.sleep(1)

print(f"Finished. Found {len(books_data)} books in total")

# Save results to a CSV file
df = pd.DataFrame(books_data)
df.to_csv('books.csv', index=False)
print("Saved results to books.csv")