import scrapy


class SpplashSkraperSpider(scrapy.Spider):
    name = "spplash_skraper"
    allowed_domains = ["www.adamchoi.co.uk"]
    start_urls = ["http://www.adamchoi.co.uk/"]
    
    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(3))
            all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
            all_matches[2]:mouse_click()
            assert(splash:wait(3))
            splash:set_viewport_full()
            return {splash:png(), splash:html()}
            end
    '''
    
    def start_requests(self):
        yield SplashRequest(url="https://www.adamchoi.co.uk/overs/detailed", callback=self.parse, 
                            endpoint='execute', args={'lua_source':self.script})
                            

    def parse(self, response):
        print(response.body)
