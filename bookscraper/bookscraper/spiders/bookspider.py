import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["thephonebook.bt.com"]
    start_urls = [
            "https://www.thephonebook.bt.com/Business/BusinessSearch/?BusinessSearchType=bus&BusinessSearchTerm=Computer+Services%2C+Network+and+Maintenance&BusinessTypeFound=true&Location=Wellingborough++%28Northamptonshire%29&LocationFound=true"]

    def parse(self, response):
        businesses = response.css('div.mb-3.border.border-dark')

        for business in businesses:
            name = business.css('span.black.medium.pr-4::text').get()
            phone_number = business.css("a.no-hover[href^='tel']::text").get()
            address = business.css('div.description::text').get()
            website = business.css('a.no-hover[data-ref="website"]::attr(href)').get()


            # Check if phone number is None
            if phone_number is not None:
                phone_number = phone_number.strip()  # Strip whitespace

            yield {
                'name': name.strip() if name else None,
                'phone_number': phone_number,
                'Address': address,
                'Website': website,
            }
