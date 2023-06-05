import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin


class HistoricoCotacaoBovespa(Resource):

    @cross_origin(supports_credentials=True)
    def get(self):
        _ticker = web.Ticker('^BVSP')
        
        return _ticker.history(period="3mo").rename(columns = {'Stock Splits': 'StocksSplits'} ).to_json(orient='table')
