from flask import Flask
from flask_restful import Api
from Fruta import Frutas, Fruta

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(main)

@main.before_request
def cria_banco():
    banco.create_all()

api.add_resource(Frutas, '/frutas')
api.add_resource(Fruta, '/frutas/<string:fruta_id>')

if __name__ == '__main__' :
    from sql_alchemy import banco
    banco.init_app(main)
    main.run(debug=True)
