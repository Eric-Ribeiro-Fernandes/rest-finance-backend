import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin


class InfoAtivo(Resource):
    
    @cross_origin(supports_credentials=True)
    def get(self, ticker):
        _ticker = self.busca_ticker(ticker)

        # resposta = {}
        # for chave in _ticker.basic_info.keys():
        #     resposta[chave] = _ticker.basic_info[chave]
        return _ticker

    def busca_ticker(self, ticker):
        sa =  web.Ticker(ticker + ".SA").basic_info

        chaves = [chave for chave in sa.keys() if chave != 'marketCap']

        resposta = {}
        for chave in chaves:
            resposta[chave] = sa[chave]

        return resposta