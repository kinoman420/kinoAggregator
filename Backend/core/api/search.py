from fastapi import APIRouter
from services.search_service import SearchService

router = APIRouter()

@router.get("/search/")
def search(what: str):
    search_service = SearchService()
    result = search_service.global_search(what)
    return result

@router.get("/searchmovie/")
def search_movie(what: str):
    search_service = SearchService()
    result = search_service.search_movie(what)
    return result

@router.get("/game/")
def search_game(what: str):
    search_service = SearchService()
    result = search_service.search_game(what)
    return result

@router.get("/anime/")
def search_anime(what: str):
    search_service = SearchService()
    result = search_service.search_anime(what)
    return result