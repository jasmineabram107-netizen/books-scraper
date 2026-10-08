# Books Scraper

A Python web scraper that collects book data from [books.toscrape.com](http://books.toscrape.com), a website built for scraping practice.

## What it does

- Downloads the book listing page
- Extracts each book's **title**, **price**, **star rating**, and **detail page URL**
- Builds full URLs from relative links using `urljoin`
- Sends a browser User-Agent header with each request
- Saves all results to a CSV file that opens in Excel

## Sample output

See [books.csv](books.csv) for real results from the script (20 books).

## Tools used

- Python 3.10
- requests: downloading web pages
- BeautifulSoup (bs4): parsing HTML
- pandas: building the table and saving to CSV

## How to run

Install the libraries:

```
pip install requests beautifulsoup4 pandas
```

Run the script:

```
python first_scrapping.py
```

The results are saved to `books.csv` in the same folder.

## Planned improvements

- Scrape all 50 pages, not just the first
- Visit each book's detail page to collect its description
