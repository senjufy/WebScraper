import scrapy
from ..items import ScrapeMovies


# This script scrapes title of movies from Kickass Torrent's recently added page.

class Movie(scrapy.Spider):
    name = 'movie'  # Name of the spider
    start_urls = [
        'https://katcr.to/new/'
        # List of any urls can be declared here. In case of this script declare only Kickass Torrent's link.
    ]

    def parse(self, response):
        items = ScrapeMovies()
        title = response.css('div a.cellMainLink::text').extract()

        yield {
            'MovieTitle': title
        }

        # Codes below generates a file with the data scraped to a .txt file.
        with open("moviesData.txt", "w") as file:
            file.write(str(title))

        # Run the script as such "scrapy crawl movie (the name of the spider)"
        # To generate data in a different file "scrapy crawl movie -o file.csv (.json etc for other formats)
