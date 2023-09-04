from pathlib import Path
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    quotesCount = 1

    file = open("quotes.txt", "a", encoding="utf-8")

    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            self.file.write("********************************************\n" + str(self.quotesCount) + ".\n")
            self.file.write("Alinti : " + text + "\n")
            self.file.write("Alinti sahibi : " + author + "\n")
            self.file.write("Etiket : " + str(tags) + "\n")
            self.quotesCount += 1

        next_url = response.css("li.next a::attr(href)").extract_first()

        if next_url is not None:
            next_url = "https://quotes.toscrape.com" + next_url
            yield scrapy.Request(url = next_url, callback = self.parse)

        else:
            self.file.close()