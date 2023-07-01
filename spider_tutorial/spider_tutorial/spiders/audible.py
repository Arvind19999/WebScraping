import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search/"]


# //ul[contains(@class,'bc-list')]/li/h3/a

# (//ul/li/div/div/div[contains(@class,'bc-row-responsive')])[1]

# //ul/li/div/div/div[contains(@class,'bc-row-responsive')]/div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'subtitle')]
    def parse(self, response):
        products = response.xpath("//ul/li/div/div/div[contains(@class,'bc-row-responsive')]")
        for product in products:
            title = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li/h3/a/text()").get()
            description = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'subtitle')]/text()").get()
            description = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'subtitle')]/span/text()").get()
            author = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'authorLabel')]/span/a/text()").getall()
            narrator = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'narratorLabel')]/span/a/text()").getall()
            seriesLabel = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'seriesLabel')]/span/a/text()").getall()
            runtimeLabel = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'runtimeLabel')]/span/text()").get()
            releaseDateLabel = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'releaseDateLabel')]/span/text()").get()
            languageLabel = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'languageLabel')]/span/text()").get()
            ratingsLabel = product.xpath(".//div[contains(@class,'bc-col-6')]/div/div/span/ul/li[contains(@class,'ratingsLabel')]/span[2]/text()").get()

            yield{
                "Title" : title,
                "Description" : description,
                "Author" : author,
                "Narrator" : narrator,
                "SeroiesLabel" : seriesLabel,
                "RunTimeLabel" : runtimeLabel,
                "ReleaseDateLabel" : releaseDateLabel,
                "LanguageLabel" : languageLabel,
                "RatingsLabel" : ratingsLabel 
            }
            
            pagination = response.xpath("//ul[contains(@class,'pagingElements')]")
            next_page_url = pagination.xpath("//ul[contains(@class,'pagingElements')]/li/span/a/@href").get() 

        if next_page_url:
            yield response.follow(url = next_page_url, callback = self.parse )