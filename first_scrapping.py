import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36'
    }
base_url = "http://books.toscrape.com/"
#SCRAPE THE LOSTING PAGE(first page 20 books)
listing_url = base_url
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(listing_url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')

books_data = [] #will store the dictionary for each book
books =soup.find_all('article', class_ = 'product_pod')

for book in books:
    title_tag = book.find('h3').find('a')
    title = title_tag.get('title', 'no title')
    detail_relative_url = title_tag.get('href') # e.g., "catalogue/a-light-in-the-attic_1000/index.html"
     
     #Build full detail URL(some links start with "../../")
    if(detail_relative_url.startwith('catalogue/')):
        detail_url = "http://book.toscrape.com" + detail_relative_url
    else:
        detail_url = "http://book.toscrape.com/catalogue/"+detail_relative_url.split('/'[-2]) 
        + '/' + detail_relative_url.split('/')[-1]
    
    # price
    price_tag = book.find('p', class_='price_color')
    price = price_tag.text if price_tag else 'No price'

    #Rating
    rating_tag = book.find('p', class_= 'star_rating')
    rating = rating_tag.get('class')[1] if(rating_tag) else "Unknown"

    #Append Basic info - we'll add description later

    books_data.append({
        'Title': title,
        'Price':price,
        'Rating':rating,
        'Detail_URL':detail_url,
        'Description':None #placeholder      
    })

    print(f"Found {len(books_data)} books on the first page.")

# find all articles that contain a book (most robust than h3)


titles = []
prices = []
ratings = []

for book in books:
    # title
    title_tag = book.find('h3').find('a')
    titles.append(title_tag.get('title', 'No title'))

    #price
    price_tag = book.find('p', class_ = "price_color")
    prices.append(price_tag.text if price_tag else "No price")

    #Rating (class names: One, Two, Three, Four, Five)
    rating_tag = book.find('p', class_ = 'star-rating')
    rating_class = rating_tag.get('class')[1] if rating_tag else 'Unknown'
    ratings.append(rating_class)

    #append basic info -we;ll add describe later
    books_data.append({
        'Title':title,
        'Price':price,
        'Rating':rating,
        'Detail URL':detail_url,
        'Description':None #placeholder
    })

print(f"Found {len(books_data)} books on the first page")