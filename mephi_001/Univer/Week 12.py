class Binom:
    def __init__(self, n):
        self.n = n
        self.cur_k = 0
        self.cur_coefficient = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_k <= self.n:
            result = self.cur_coefficient
            self.cur_k += 1
            self.cur_coefficient = self.cur_coefficient * (self.n - self.cur_k + 1) // self.cur_k
            return result
        else:
            #raise StopIteration  # завершение
            self.cur_k = 0
            self.cur_coefficient = 1
            result = self.cur_coefficient
            self.cur_k += 1
            self.cur_coefficient = self.cur_coefficient * (self.n - self.cur_k + 1) // self.cur_k
            return result


# bin_iter = Binom(int(input()))
bin_iter = Binom(5)
for i in bin_iter:
    print(i)

