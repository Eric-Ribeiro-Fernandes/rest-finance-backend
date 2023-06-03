import yfinance as web
from flask_restful import Resource

class InfoAtivo(Resource):
    
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")
        return _ticker.info
