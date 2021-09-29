from math import floor

class FizzBuzzGenerator:
    """
    Generator class for FizzBuzz game

    start || The first number to start the count from;\n
    fizz || Custom Fizz;\n
    buzz || Custom Buzz.\n
    """

    def __init__(self, start, stop = None, step=1, fizz=3, buzz=5):
        self.start = start
        if fizz:
            self.iFizz = fizz
        if buzz:
            self.iBuzz = buzz
        if stop:
            self.stop = abs(start - stop)//step
        self.iFizzBuzz = fizz*buzz
        self.slider = self.get_rem(start)
        self.order = self.get_order(start)
        self.stock = []
        self.try_check = 0
        if stop:
            self.step = step if start < stop else step*-1
    

    def __iter__(self):
        return self


    def __next__(self):
        if self.slider >= self.iFizzBuzz:
            self.slider = 0 if self.step == 1 else self.slider-self.iFizzBuzz
            self.order += 1
        self.slider += 1*self.step
        if len(self.stock) < self.iFizzBuzz:
            self.stock.append(self.check_fizz_buzz(self.slider))
        if self.try_check == self.iFizzBuzz:
            self.try_check = 0

        self.try_check += 1
        ans = self.stock[self.try_check-1]
        if self.stop <= 0:
            raise StopIteration
        else:
            self.stop -= 1
        return ans+self.iFizzBuzz*self.order if isinstance(ans, int) else ans

    
    def __getitem__(self, args):
        
        if isinstance(args, int):
            return self.check_fizz_buzz(args+self.start-1)
        else:
            tmp_strt = args.start if args.start > self.start else self.start
            if args.step:
                return FizzBuzzGenerator(tmp_strt, stop=args.stop, step=args.step)
            else:
                return FizzBuzzGenerator(tmp_strt, stop=args.stop)


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