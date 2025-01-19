
import urllib.request
from html.parser import HTMLParser






class nyaasi(object):

    url = 'https://nyaa.si'
    name = 'Nyaa.si'
 


    class NyaasiParser(HTMLParser):
        

        def __init__(self, res, url):

            try:
                super().__init__()
            except TypeError:
                HTMLParser.__init__(self)

            self.engine_url = url
        
            self.results = res
            self.curr = None
            self.td_counter = -1

        def handle_starttag(self, tag, attr):
            
            if tag == 'a':
                self.start_a(attr)

        def handle_endtag(self, tag):
            
            if tag == 'td':
                self.start_td()

        def start_a(self, attr):

            params = dict(attr)

            if 'title' in params and 'class' not in params \
                    and params['href'].startswith('/view/'):
                hit = {
                        'name': params['title'],
                        'desc_link': self.engine_url + params['href']}
                if not self.curr:
                    hit['engine_url'] = self.engine_url
                    self.curr = hit
            elif 'href' in params and self.curr:
            
                if not params['href'].startswith("magnet:?") and \
                        not params['href'].endswith(".torrent"):
                    return


                elif params['href'].startswith("magnet:?"):
                    self.curr['link'] = params['href']
                    self.td_counter += 1

        def start_td(self):
            
            
            if self.td_counter >= 0:
                self.td_counter += 1

            
            if self.td_counter >= 5:
                self.results.append(self.curr)
                self.curr = None
                self.td_counter = -1

        def handle_data(self, data):
         
            
            if self.td_counter > 0 and self.td_counter <= 5:
                
                if self.td_counter == 1:
                    self.curr['size'] = data.strip()
                
                elif self.td_counter == 3:
                    try:
                        self.curr['seeds'] = int(data.strip())
                    except ValueError:
                        self.curr['seeds'] = -1
                
                elif self.td_counter == 4:
                    try:
                        self.curr['leech'] = int(data.strip())
                    except ValueError:
                        self.curr['leech'] = -1

                else:
                    pass


    def search(self, what, cat='all'):
        
        what = what.replace(" ", '+')
        url = str("{0}/?f=0&s=seeders&o=desc&c=0_0&q={1}&s=seeders&o=desc"
                  .format(self.url, what))

        hits = []
        result = []
        page = 1
        parser = self.NyaasiParser(hits, self.url,)
        while page < 2:
           
           # https://stackoverflow.com/questions/42212800/httpresponse-to-string-python
            res = urllib.request.urlopen(url + "&p={}".format(page))
            html_response = res.read()
            encoding = res.headers.get_content_charset('utf-8')
            decoded_html = html_response.decode(encoding)

            parser.feed(decoded_html)
            for each in hits[:20]:
                result.append(each)

            if len(hits) < 75:
                break
            del hits[:]
            page += 1

        parser.close()
        return result