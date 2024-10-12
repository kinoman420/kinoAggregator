


from urllib.parse import urlencode, unquote
from urllib.request import Request, urlopen
import re
import json



class yts_mx(object):


    url = 'https://yts.mx/'
    api_url = 'https://yts.mx/api/v2/list_movies.json?'
    name = 'YTS.MX'
    supported_categories = {
        'all': '0',
        'movies': '1'
    }

    def __init__(self):
        """
         hello
        """

    def search(self, what, cat='all'):
       

        result = []
        search_url = self.api_url
        
        what = unquote(what)
        search_params = {'sort_by': 'title'}  

        
        quality_rstring = r'(?:quality=)?((?:2160|1440|1080|720|480|240)p|3D)'
        quality_re = re.search(quality_rstring, what)
        search_resolution = None
        if quality_re:
            search_resolution = quality_re.group(1)
            search_params['quality'] = search_resolution
            what = re.sub(quality_rstring, '', what).strip()
        
        codec_rstring = r'(?:\.?(?:x|h)(264|265))'
        codec_re = re.search(codec_rstring, what)
        search_codec = None
        if codec_re:
            search_codec = 'x' + codec_re.group(1)
            if 'quality' in search_params:
                search_params['quality'] += f'.{search_codec}'  
            what = re.sub(codec_rstring, '', what).strip()

        
        rating_rstring = r'(?:min(?:imum)?_)?rating=(\d)'
        rating_re = re.search(rating_rstring, what)
        min_rating = None
        if rating_re:
            min_rating = rating_re.groups()[-1]
            search_params['minimum_rating'] = {min_rating}
            what = re.sub(rating_rstring, '', what).strip()

        

        
        search_rstring = r'&page=\d+'
        what = re.sub(search_rstring, '', what).strip()

        
        if what:
            search_params['query_term'] = what
        search_url += urlencode(search_params)
        req = Request(url=search_url, headers={'User-Agent': 'Mozilla/5.0'})

        res = urlopen(req)
        html_response = res.read().decode('utf-8')
        api_result = json.loads(html_response)
        if api_result['status'] != 'ok':
            print(api_result['status'] + api_result['satus_message'])
            return

        prev_movie = None
        while api_result['data']['movie_count'] > api_result['data']['limit']*(api_result['data']['page_number']-1):
            for movie in api_result['data']['movies']:
                if not prev_movie or movie['id'] != prev_movie['id']:
                    prev_movie = movie
                else:
                    for torrent in prev_movie['torrents']:
                        if torrent in movie['torrents']:
                            movie['torrents'].remove(torrent)
                for torrent in movie['torrents']:
                    if search_codec and torrent['video_codec'] != search_codec:
                        continue
                    if search_resolution and torrent['quality'] != search_resolution:
                        continue
                    formatTorrent = {
                        'link': torrent['url'],
                        'name': f'{movie["title_long"]} [{torrent["quality"]}] [{torrent["video_codec"]}] [{torrent["type"]}] [{torrent["audio_channels"]}] [YTS.MX]',
                        'size': torrent['size'],
                        'seeds': str(torrent['seeds']),
                        'leech': str(torrent['peers']),
                        'engine_url': self.url,
                        'desc_link': movie['url'],
                    }
                    result.append(formatTorrent)
            nextpage_rstring = r'&(?:page=\d+)|$'
            search_url = re.sub(nextpage_rstring, f'&page={api_result["data"]["page_number"]+1}', search_url)
            req = Request(url=search_url, headers={'User-Agent': 'Mozilla/5.0'})

            res = urlopen(req)
            html_response = res.read().decode('utf-8')
            api_result = json.loads(html_response)
            return result
            

        