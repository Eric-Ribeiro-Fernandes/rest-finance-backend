from flask import Flask
from flask_restful import Resource, Api
from services.SetoresTickers import SetoresTickers
from models.Tickers import Tickers
from models.InfoAtivo import InfoAtivo
from models.HistoricoCotacao import HistoricoCotacao
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'
    
    
    
    

        
api.add_resource(Tickers, '/tickers')
api.add_resource(InfoAtivo, '/<string:ticker>')
api.add_resource(HistoricoCotacao, '/<string:ticker>/cotacao')

if __name__ == '__main__':
    app.run(debug=True)