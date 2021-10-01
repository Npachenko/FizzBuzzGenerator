class FizzBuzzGenerator:
    """
    Generator class for FizzBuzz game

    start - The first number to start the count from;
    fizz - Custom Fizz;
    buzz - Custom Buzz.
    """

    def __init__(self, start, stop = None, step=1, fizz=3, buzz=5):

        self.start = start
        self.stop = stop if stop else None
        self.step = step
        self.fizz = fizz
        self.buzz = buzz    
        self.fizz_buzz = fizz*buzz
        self.first_check = False
        self.current = self.start
    

    def __iter__(self):

        return self


    def __next__(self):
        if self.first_check:
            if self. stop:
                if (self.step > 0  and self.current < self.stop) or (self.step < 0 and self.current > self.stop):
                    pass
                else:
                    raise StopIteration
            self.current += 1*self.step
        else:
            self.first_check = True
        
        return self.get_fizz_buzz(self.current)
    

    def __getitem__(self, args):
        
        if isinstance(args, int):
            return self.get_fizz_buzz(args+self.start)
        else:
            if args.start:
                tmp_strt = args.start + self.start
            else:
                tmp_strt = self.start
            
            if args.stop:
                tmp_stop = args.stop
                if self.stop:
                    if tmp_stop > self.stop:
                        tmp_stop = self.stop
                if args.stop < 0 and self.stop == None:
                    raise Exception("Can't subtract from infinity")
            else:
                tmp_stop = None

            if args.step:
                return FizzBuzzGenerator(tmp_strt, tmp_stop, step=args.step)
            else:
                return FizzBuzzGenerator(tmp_strt, stop=tmp_stop)
    

    def get_fizz_buzz(self, num):
        """
        Method for calculate actual FizzBuzz number

        num || Numer for calculation
        """
        if num % self.fizz_buzz == 0:
            return 'FizzBuzz'
        elif num % self.buzz == 0:
            return 'Buzz'
        elif num % self.fizz == 0:
            return 'Fizz'
        else:
            return num