import json
from urllib.request import Request, urlopen
from urllib.parse import unquote


class fitgirl_repacks(object):
    url = 'https://fitgirl-repacks.site/'
    name = 'FitGirl Repacks'
    supported_categories = {'all': ''}

    def search(self, what, cat='all'):
        search_url = 'https://hydralinks.cloud/sources/fitgirl.json'

        req = Request(url=search_url, headers={'User-Agent': 'Mozilla/5.0'} )

        res = urlopen(req)
        html_response = res.read().decode('utf-8')
        response_json = json.loads(html_response)

        what = unquote(what)
        search_terms = what.lower().split()

        hits = []

        for result in response_json['downloads']:
            if any(term in result['title'].lower() for term in search_terms):
                res = {'link': self.download_link(result),
                       'name': result['title'],
                       'size': result['fileSize'],
                       'seeds': '-1',
                       'leech': '-1',
                       'engine_url': self.url,
                       'desc_link': '-1'}
                hits.append(res)
        return hits

    def download_link(self, result):
            return result['uris'][0]