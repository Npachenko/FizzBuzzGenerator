from math import floor

class FizzBuzzGenerator:
    """
    Generator class for FizzBuzz game

    start || The first number to start the count from;\n
    iFizz || Custom Fizz;\n
    iBuzz || Custom Buzz.\n
    """

    def __init__(self, start, iFizz=3, iBuzz=5):
        if iFizz:
            self.iFizz = iFizz
        if iBuzz:
            self.iBuzz = iBuzz
        self.iFizzBuzz = iFizz*iBuzz
        self.slider = self.get_rem(start)
        self.order = self.get_order(start)
        self.stock = []
        self.try_check = 0
    
    
    def __iter__(self):
        return self


    def __next__(self):
        if self.slider == self.iFizzBuzz:
            self.slider = 0
            self.order += 1
        self.slider += 1
        if self.try_check < self.iFizzBuzz:
            self.stock.append(self.check_fizz_buzz(self.slider))
            self.try_check += 1
        else:
            self.try_check = 1
        ind = self.try_check-1

        return self.stock[ind]+self.iFizzBuzz*self.order if isinstance(self.stock[ind], int) else self.stock[ind]


    def get_rem(self, start):
        """
        Method for define remains of cycle

        start || The first number to start the count from.
        """
        return (start%self.iFizzBuzz)-1


    def get_order(self, start):
        """
        Method for define order of сycle

        start || The first number to start the count from.
        """
        return floor(start/self.iFizzBuzz)
    

    def check_fizz_buzz(self, num):
        """
        Method for calculate actual FizzBuzzNumber

        num || Numer for calculation
        """
        return 'FizzBuzz' if num%self.iFizzBuzz==0 else \
            'Fizz' if num%self.iFizz==0 else \
                'Buzz' if num%self.iBuzz==0 else num