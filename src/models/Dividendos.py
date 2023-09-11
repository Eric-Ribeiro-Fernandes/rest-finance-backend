import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin
import json


class Dividendos(Resource):
    
    @cross_origin(supports_credentials=True)
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")

        resposta = {}

        resposta['Data'] = _ticker.dividends.index.astype(int).to_list()
        resposta['Dividendos'] = _ticker.dividends.to_list()

        # return json.dumps(resposta)
        return _ticker.dividends.to_json(orient='table')