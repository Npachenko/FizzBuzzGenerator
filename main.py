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
    
    def __iter__(self):
        return self

    def __next__(self):
        i = self.slider
        if self.slider == self.iFizzBuzz:
            self.slider = 0
            self.order += 1
        self.slider += 1
        return 'FizzBuzz' if i%self.iFizzBuzz==0 else \
            'Fizz' if i%self.iFizz==0 else \
                'Buzz' if i%self.iBuzz==0 else \
                    i+(self.order*self.iFizzBuzz)

    def get_rem(self, start):
        """
        Method for define remains of cycle

        start || The first number to start the count from.
        """
        return (start%self.iFizzBuzz)

    def get_order(self, start):
        """
        Method for define order of сycle

        start || The first number to start the count from.
        """
        return floor(start/self.iFizzBuzz)