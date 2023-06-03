import json
import os


class SetoresTickers():
    def __init__(self):
        self._load_tickers_cache()
        
    def _load_tickers_cache(self) -> None:
        ''' Carrega tickers de cache'''
        with open( os.getcwd() + "/src/assets/cache/setor_tickers.json",'r') as file:
            tickers = json.loads(file.read())
            self._tickers = tickers
            
    @property
    def get_tickers(self) -> dict:
        return self._tickers
            
            