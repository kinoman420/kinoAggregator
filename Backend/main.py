from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from parsers import nyaasi,fitgirl,dodi, yts
from iam.endpoints import user


app = FastAPI()
app.include_router(user.user_router)

origins = [ "http://localhost:3000" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search/")
def search(what: str):
    nyaa_engine = nyaasi.nyaasi()
    #fitgirl_engine = fitgirl.fitgirl_repacks()
    #dodi_engine = dodi.dodi_repacks()
    #yts_engine = yts.yts_mx()

    nyaa_res = nyaa_engine.search(what)
    #fit_res = fitgirl_engine.search(what)
   # dodi_res = dodi_engine.search(what)
    
   # yts_res = yts_engine.search(what)
    
    result = []

    # result.append(nyaa_res)
    # result.append(fit_res)
    # result.append(dodi_res)
    result.append(nyaa_res)

    

    return result