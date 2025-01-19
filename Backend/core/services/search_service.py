from parsers import nyaasi, fitgirl, dodi, yts

class SearchService:
    def __init__(self):
        self.nyaa_engine = nyaasi.nyaasi()
        self.fitgirl_engine = fitgirl.fitgirl_repacks()
        self.dodi_engine = dodi.dodi_repacks()
        self.yts_engine = yts.yts_mx()

    def global_search(self, what: str):
        nyaa_res = self.nyaa_engine.search(what)
        fit_res = self.fitgirl_engine.search(what)
        dodi_res = self.dodi_engine.search(what)
        yts_res = self.yts_engine.search(what)

        result = []
        result.append(nyaa_res)
        result.append(fit_res)
        result.append(dodi_res)
        result.append(yts_res)

        return result

    def search_movie(self, what: str):
        yts_res = self.yts_engine.search(what)
        return [yts_res]

    def search_game(self, what: str):
        fit_res = self.fitgirl_engine.search(what)
        dodi_res = self.dodi_engine.search(what)
        return [fit_res, dodi_res]

    def search_anime(self, what: str):
        nyaa_res = self.nyaa_engine.search(what)
        return [nyaa_res]