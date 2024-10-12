from fastapi import FastAPI

from parsers import nyaasi,fitgirl,dodi, yts


app = FastAPI()


@app.get("/search/")
def search(what: str):
    nyaa_engine = nyaasi.nyaasi()
    fitgirl_engine = fitgirl.fitgirl_repacks()
    dodi_engine = dodi.dodi_repacks()
    yts_engine = yts.yts_mx()

    nyaa_res = nyaa_engine.search(what)
    fit_res = fitgirl_engine.search(what)
    dodi_res = dodi_engine.search(what)
    
    yts_res = yts_engine.search(what)
    
    result = []

    # result.append(nyaa_res)
    # result.append(fit_res)
    # result.append(dodi_res)
    result.append(yts_res)

    

    return result