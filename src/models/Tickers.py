from flask_restful import Resource
from services.SetoresTickers import SetoresTickers

class Tickers(Resource):
    
    
    def get(self):
        setoresTickers = SetoresTickers()
        return setoresTickers.get_tickers
