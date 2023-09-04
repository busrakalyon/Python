import scrapy


class WordSpider(scrapy.Spider):
    name = "words"
    kelime_sayisi = 1
    file = open("A2.txt", "a", encoding="utf-8")

    start_urls = [
        "https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"
    ]

    def parse(self, response):
        kelimeler = None