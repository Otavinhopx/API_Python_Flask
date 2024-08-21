from flask import Flask
from flask_restful import Api
from Fruta import Frutas, Fruta

main = Flask(__name__)
api = Api(main)

api.add_resource(Frutas, '/frutas')
api.add_resource(Fruta, '/frutas/<string:fruta_id>')

if __name__ == '__main__' :
    main.run(debug=True)
