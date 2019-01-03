class PreditorFizzBuzz():

    def predizPara(self, numeroASerPredito):
        if numeroASerPredito % 3 == 0 and numeroASerPredito % 5 == 0:
            return "FizzBuzz"
        elif numeroASerPredito % 3 == 0 or "3" in str(numeroASerPredito):
            return "Fizz"
        elif numeroASerPredito % 5 == 0 or "5" in str(numeroASerPredito):
            return "Buzz"
        else:
            return str(numeroASerPredito)
