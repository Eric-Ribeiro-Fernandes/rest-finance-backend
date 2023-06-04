from flask_restful import Resource
from services.SetoresTickers import SetoresTickers

from flask_cors import CORS, cross_origin

class Tickers(Resource):
    
    @cross_origin(supports_credentials=True)
    def get(self):
        setoresTickers = SetoresTickers()
        return setoresTickers.get_tickers
