# Books Scraper

A Python web scraper that collects data on all 1,000 books from [books.toscrape.com](http://books.toscrape.com), a website built for scraping practice.

## What it does

- Scrapes all 50 listing pages automatically (pagination)
- Extracts each book's **title**, **price**, **star rating**, and **detail page URL**
- Builds full URLs from relative links using `urljoin`
- Sends a browser User-Agent header with each request
- Waits 1 second between pages to avoid overloading the website
- Stops safely if a page is missing
- Saves all results to a CSV file that opens in Excel

## Sample output

See [books.csv](books.csv) for real results from the script (1,000 books).

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

It takes about a minute and shows progress for each page. The results are saved to `books.csv` in the same folder.

## Planned improvements

- Visit each book's detail page to collect its description
