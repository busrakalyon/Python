import scrapy


class BookSpider(scrapy.Spider):
    name = "books"
    sayfaSayisi = 0
    kitapSayisi = 1
    file = open("Çok Satanlar.txt", "a", encoding="utf-8")

    start_urls = [
        "https://kidega.com/cok-satanlar/"
    ]

    def parse(self, response):
        books_name = response.css("h3.book-name::text").extract()
        authors_name = response.css("span.manufacturer-name::text").extract()
        publishers = response.css("span.distributor-name::text").extract()
        fiyat_lira = response.css("div.urunListe_satisFiyat::text").extract()
        fiyat_krs = response.css("div.urunListe_satisFiyat span.d::text").extract()

        i = 0

        while (i < len(books_name)):
            self.file.write("\n*************************************\n" + str(self.kitapSayisi)+ "\n")
            self.file.write("Kitap : " + books_name[i])
            self.file.write("\nYazar : " + authors_name[i])
            self.file.write("\nYayınevi : " + publishers[i])
            self.file.write("\nFiyat : " + fiyat_lira[i] + fiyat_krs[i])

            self.kitapSayisi += 1
            i += 1
    
    
        next_url = response.css("a.paging::attr(href)").extract_first()
        next_url = "https://kidega.com" + next_url
        self.sayfaSayisi += 1

        if next_url is not None:
            yield scrapy.Request(url = next_url, callback = self.parse)
        
        else:
            self.file.close()

