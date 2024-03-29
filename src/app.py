from flask import Flask
from flask_restful import Resource, Api
from services.SetoresTickers import SetoresTickers
from models.Tickers import Tickers
from models.InfoAtivo import InfoAtivo
from models.HistoricoCotacaoDia import HistoricoCotacaoDia
from models.HistoricoCotacaoBovespa import HistoricoCotacaoBovespa
from models.Dividendos import Dividendos
from flask_cors import CORS, cross_origin

from models.CandleStick import CandleStick


app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'
    
    
    
    

        
api.add_resource(Tickers, '/tickers')
api.add_resource(InfoAtivo, '/<string:ticker>')
api.add_resource(CandleStick, '/<string:ticker>/cotacao')
api.add_resource(Dividendos, '/<string:ticker>/dividendos')
api.add_resource(HistoricoCotacaoBovespa, '/bovespa')
api.add_resource(HistoricoCotacaoDia, '/<string:ticker>/dia')


if __name__ == '__main__':
    app.run(debug=True)