class Calculator():

    def add(self, input):
        # Nenhum numero na string de entrada
        if len(input) == 0:
            return 0
        # trata a string e transforma em uma lista de numeros
        numeros = map(int, input.split(","))
        return sum(numeros)
