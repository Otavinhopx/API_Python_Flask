from sql_alchemy import banco



class FrutaModel(banco.Model):
    __tablename__ = 'fruta'
    
    fruta_id = banco.Column(banco.String, primary_key = True)
    nomeFruta = banco.Column(banco.String(20))
    corFruta = banco.Column(banco.String(20))
    precoFruta = banco.Column(banco.Float(precision = 2))
    
    def __init__(self, fruta_id, nomeFruta, corFruta, precoFruta):
        self.fruta_id = fruta_id
        self.nomeFruta = nomeFruta
        self.corFruta = corFruta
        self.precoFruta = precoFruta
        
    def transformaJson(self):
        return {
            'fruta_id' : self.fruta_id,
            'nomeFruta' : self.nomeFruta,
            'corFruta' : self.corFruta,
            'precoFruta' : self.precoFruta
        }