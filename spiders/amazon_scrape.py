import scrapy
from ..items import ScrapeItem


# This script scrapes title of books from amazon's recently added books page.

class AmazonSpider(scrapy.Spider):
    name = 'amazon'  # Name of the spider
    start_urls = [
        'https://www.amazon.ae/gp/new-releases/books/ref=zg_bsnr_books_home_all?pf_rd_p=189256b9-dc60-481d-9251-57301b69ff33&pf_rd_s=center-1&pf_rd_t=2201&pf_rd_i=home&pf_rd_m=A2KKU8J8O8784X&pf_rd_r=S08MKKGBBQCRMV97RBBW&pf_rd_r=S08MKKGBBQCRMV97RBBW&pf_rd_p=189256b9-dc60-481d-9251-57301b69ff33'
        # List of any urls can be declared here. In case of this script declare only amazon link.
    ]

    def parse(self, response):
        items = ScrapeItem()
        title = response.css('a div::text').extract()

        yield {
            'title': title

        }

        # Codes below generates a file with the data scraped to a .txt file.
        with open("newData.txt", "w") as file:
            file.write(str(title))

        # Run the script as such "scrapy crawl amazon (the name of the spider)"
        # To generate data in a different file "scrapy crawl amazon -o file.csv (.json etc for other formats)
