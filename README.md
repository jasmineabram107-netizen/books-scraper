# Books Scraper

A Python web scraper that collects book data from [books.toscrape.com](http://books.toscrape.com), a website built for scraping practice.

## What it does

- Downloads the book listing page
- Extracts each book's **title**, **price**, **star rating**, and **detail page URL**
- Builds full URLs from relative links using `urljoin`
- Sends a browser User-Agent header with each request

## Tools used

- Python 3.10
- requests: downloading web pages
- BeautifulSoup (bs4): parsing HTML
- pandas: data handling

## How to run

Install the libraries:

```
pip install requests beautifulsoup4 pandas
```

Run the script:

```
python first_scrapping.py
```

## Planned improvements

- Save results to a CSV file
- Scrape all 50 pages, not just the first
- Visit each book's detail page to collect its description
