from fastapi import FastAPI
from parsers import nyaasi

app = FastAPI()


@app.get("/search/")
def search(what: str):
    nyaa_engine = nyaasi.nyaasi()
    #fitgirl_engine = None   #Todo
    #TorrentGalaxy = None    #Todo

    nyaa_res = nyaa_engine.search(what)
    #fit_res = fitgirl_engine.search(what)
    #TorrentGalaxy_res = TorrentGalaxy.search(what)

    
    result = []

    result.append(nyaa_res)
   #result.append(fit_res)
    #result.append(TorrentGalaxy_res)

    

    return result