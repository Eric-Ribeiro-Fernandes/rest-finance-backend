import yfinance as web
from flask_restful import Resource

class HistoricoCotacao(Resource):
    
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")
        
        return _ticker.history(period="3mo").to_json()
