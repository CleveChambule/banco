class Cliente:

    def __init__(self, nome, sobrenome, bi):
        self.nome = nome
        self.sobrenome = sobrenome
        self.bi = bi

    def __str__(self):
        return "\nNome: {} \nSobrenome: {} \nBI: {}".format(self.nome,self.sobrenome,self.bi)