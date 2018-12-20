"""
Processo de desenvolvimento feito sem refactor.
Torna o codigo uma bagunca.
"""


class Greeting():

    def greet(self, name):
        # varifica se eh uma lista
        if type(name) == list:
            # ajusta a lista para nomes que possuem virgula em seu interior
            names = []
            for i in name:
                aux = i.split(", ")
                for j in aux:
                    names.append(j)
            name = names
            # verifica nomes em maiusculo
            nomeMaiusculo = ""
            for person in name:
                if person.isupper():
                    nomeMaiusculo = person
                    name.remove(person)
            # lista com dois nomes
            if len(name) == 2:
                tmp = "Hello, " + name[0] + " and " + name[1] + "."
            else:
                # varios nomes em uma lista
                tmp = "Hello, "
                for i in xrange(len(name)):
                    if i < len(name) - 1:
                        tmp += name[i] + ", "
                    else:
                        tmp += "and " + name[i] + "."
            # adiciona parametro para nomes maiusculos
            if nomeMaiusculo != "":
                tmp += " AND HELLO " + nomeMaiusculo + "!"
            return tmp
        else:
            # Caso de string nula
            if name == None or len(name) == 0:
                return "Hello, my friend."
            # Caso de string toda maiuscula
            elif name.isupper():
                return "HELLO " + name + "!"
            # Caso de string com so um nome
            return "Hello, " + name + "."
