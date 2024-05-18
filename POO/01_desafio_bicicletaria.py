class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('plim')
    
    def parar(self):
        print('parado')
        
    def correr(self):
        print('vrum')            
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join({f'{chave}={valor}' for chave, valor in self.__dict__.items()})}"
    
    
b1 = Bicicleta("vermelho","caloi", 2000, 500)
# b1.correr()
# print(b1.cor)
# print(b1.modelo)
# print(b1.ano)
# print(b1.valor)

b2 = Bicicleta("amarelo", "bmx", 2015, 1800)
# print(b2.cor)
# print(b2.modelo)
# print(b2.ano)
# print(b2.valor)


# Bicicleta.correr(b1)
# Bicicleta.parar(b1)
# Bicicleta.buzinar(b1)


