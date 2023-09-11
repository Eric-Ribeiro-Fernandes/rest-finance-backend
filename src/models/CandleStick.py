import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin
import plotly.graph_objects as go
import cufflinks as cf 



class CandleStick(Resource):

    @cross_origin(supports_credentials=True)
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")
        
        
        df = _ticker.history( period= "3mo")
        df = df.drop(df.tail(1).index)
        
        cf.set_config_file(theme='white')
        
        # Criando figura quant
        qf = cf.QuantFig(df=df, title= "Preço nos últimos 3 meses", name = 'Ativo')
        qf.add_bollinger_bands()
        qf.add_rsi()        
        qf.add_volume()
        
            # Valores fixos representam dias úteis no ano
        qf.add_resistance(str(df[-200:-21][df[-200:-21]['Close'] == df[-200:-21]['Close'].max()].index[0]), on= 'close')
        qf.add_support(str(df[-200:-21][df[-200:-21]['Close'] == df[-200:-21]['Close'].min()].index[0]), on= 'low')  
        
        # Transforma em figura plotly
        qf_figure = qf.figure()
        
        
        return (qf_figure.to_json())