from flask_restful import Resource, reqparse
from models.Fruta import FrutaModel

#Simulação de banco de dados

frutas = [
    {
        'fruta_id' : 'laranja',
        'nomeFruta' : 'laranja',
        'corFruta' : 'laranja',
        'precoFruta' : 4.20
    },
    {
        'fruta_id' : 'morango',
        'nomeFruta' : 'morango',
        'corFruta' : 'vermelha',
        'precoFruta' : 6.20
    },
    {
        'fruta_id' : 'maça',
        'nomeFruta' : 'maça',
        'corFruta' : 'vermelha',
        'precoFruta' : 1.20
    }
] 

#Classe

class Frutas(Resource):
    def get(self):
        return{'frutas' : frutas}
    
class Fruta(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nomeFruta')
    argumentos.add_argument('corFruta')
    argumentos.add_argument('precoFruta', type=float)
    
    def findfruta(fruta_id):
         for fruta in frutas :
            if fruta['fruta_id'] == fruta_id :
                return fruta
         return None
    
    def get(self, fruta_id):
        fruta = Fruta.findfruta
        if fruta :
            return fruta
        return {'message' : 'Fruta Not found'}, 404
    
    def post(self, fruta_id) :
        
        dados = Fruta.argumentos.parse_args()
        novaFruta = FrutaModel(fruta_id, **dados)
        frutaJson = novaFruta.transformaJson()
        frutas.append(frutaJson)
        
        return frutaJson, 201
    
    def put(self, fruta_id):
        
        dados = Fruta.argumentos.parse_args()
        novaFruta = FrutaModel(fruta_id, **dados)
        frutaJson = novaFruta.transformaJson()
        fruta = Fruta.findfruta(fruta_id)
        
        if fruta :
            fruta.update(frutaJson)
            return frutaJson, 200
            
        return {'message' : 'Fruta not found to update'}, 404
    
    def delete(self, fruta_id):
        global frutas
        frutas = [fruta for fruta in frutas if fruta['fruta_id'] != fruta_id]
        return {'message' : 'Fruta deleted'}, 200