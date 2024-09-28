import urllib.request



from html.parser import HTMLParser
import re



class linuxtracker(object):
    """Class used by qBittorrent to search for torrents"""

    url = 'http://linuxtracker.org'
    name = 'Linux Tracker'
    
    supported_categories = { 'all' : 0, 'software': 0}

    class LinuxSearchParser(HTMLParser):
        
        def __init__(self, res, url):
            try:
                super().__init__()
            except:
                # See: http://stackoverflow.com/questions/9698614/
                HTMLParser.__init__(self)
            self.results = res
            self.engine_url = url
            self.curr = None
            self.strong_count = 0
            self.wait_for_data = True

        def handle_starttag(self, tag, attr):
            if tag == 'a':
                self.start_a(attr)

        def handle_endtag(self, tag):
            if tag == 'strong':
                self.end_strong()

        def start_a(self, attr):
            params = dict(attr)
            if 'href' in params and 'title' in params and \
                    "torrent-details" in params['href']:
                hit = {'desc_link': self.engine_url + '/' + params['href']}
                self.curr = hit
                self.wait_for_data = True
            elif 'href' in params and \
                    "magnet:?" in params['href']:
                self.curr['link'] = params['href']
                self.curr['engine_url'] = self.engine_url
                self.results.append(self.curr)
                self.curr = None
            elif 'href' in params and \
                    "peers" in params['href']:
                self.wait_for_data = True

        def end_strong(self):
            self.strong_count += 1
            self.wait_for_data = True

        def handle_data(self, data):
            if self.wait_for_data is True:
                
                if self.strong_count is 0 and self.curr:
                    
                    self.curr['name'] = data.strip()
                elif self.strong_count is 3 and self.curr:
        
                        if "," in data:
                            data = re.sub(",", '', data)
                        self.curr["size"] = data.strip()
                elif self.strong_count is 4 and self.curr:
                
                    try:
                        self.curr["seeds"] = int(data.strip())
                    except:
                        pass
                elif self.strong_count is 5 and self.curr:
                    
                    try:
                        self.curr["leech"] = int(data.strip())
                    except:
                        pass
                elif self.strong_count is 6:
                    
                    self.strong_count = 0
                self.wait_for_data = False

    def __init__(self):
        """class initialization"""

    def download_torrent(self, info):
        """Retrieve and save url as a temporary file."""


    def search(self, what, cat='all'):

        url = str("{0}/index.php?page=torrents"
                  "&active=1&order=5&by=2&search={1}").format(self.url, what)

        hits = []
        res = []
        page = 1
        parser = self.LinuxSearchParser(hits, self.url)
        while True:
            rres = urllib.request.urlopen(url + "&p={}".format(page))
            html_response = res.read()
            encoding = res.headers.get_content_charset('utf-8')
            decoded_html = html_response.decode(encoding)
            parser.feed(res)
            for each in hits:
                res.append(hits)

            if len(hits) < 15:
                break
            del hits[:]
            page += 1

        parser.close()
        return res