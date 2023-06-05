import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin


class HistoricoCotacao(Resource):

    @cross_origin(supports_credentials=True)
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")
        
        return _ticker.history(period="3mo").rename(columns = {'Stock Splits': 'StocksSplits'} ).to_json(orient='table')
