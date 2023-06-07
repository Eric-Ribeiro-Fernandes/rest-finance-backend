import yfinance as web
from flask_restful import Resource
from flask_cors import  cross_origin
import plotly.graph_objects as go
import cufflinks as cf 



class CandleStick(Resource):

    @cross_origin(supports_credentials=True)
    def get(self, ticker):
        _ticker = web.Ticker(ticker + ".SA")
        
        
        df = _ticker.history( period= "2y")
        df = df.drop(df.tail(1).index)
        
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                       open=df['Open'], high=df['High'],
                       low=df['Low'], close=df['Close'] )], layout= go.Layout(plot_bgcolor="#332E33", paper_bgcolor = 'whitesmoke'))
        cf.set_config_file(theme='henanigans')
        qf = cf.QuantFig(df=df, title= "Preço nos últimos 2 anos", name = 'Ativo')
        qf.add_bollinger_bands()
        qf.add_volume()
        
        qf_figure = qf.figure()
        qf_figure.update_layout(plot_bgcolor="#332E33")
        qf_figure.update_layout(paper_bgcolor = '#332E33')
        
        
        
        
        
        fig.to_plotly_json()
        
        return (qf_figure.to_json())