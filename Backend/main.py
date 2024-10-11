from fastapi import FastAPI

from parsers import nyaasi,fitgirl,dodi,linuxtracker,torrentgalaxy, rarbg


app = FastAPI()


@app.get("/search/")
def search(what: str):
    nyaa_engine = nyaasi.nyaasi()
    fitgirl_engine = fitgirl.fitgirl_repacks()
    dodi_engine = dodi.dodi_repacks()
    linux_engine = linuxtracker.linuxtracker()
    torrentgalaxy_engine = torrentgalaxy.torrentgalaxy()    #Todo
    rarbg_engine = rarbg.therarbg()

    # nyaa_res = nyaa_engine.search(what)
    # fit_res = fitgirl_engine.search(what)
    # dodi_res = dodi_engine.search(what)
    # linux_res = linux_engine.search(what)
    # TorrentGalaxy_res = torrentgalaxy_engine.search(what)
    rarbg_res = rarbg_engine.search((what))
    
    result = []

    # result.append(nyaa_res)
    # result.append(fit_res)
    # result.append(dodi_res)
    # result.append(linux_res)
    # result.append(TorrentGalaxy_res)
    result.append(rarbg_res)

    

    return result