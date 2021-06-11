import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        contents = list()
        for k in kwargs.keys():
            for i in range(kwargs[k]):
                contents.append(k)
        self.contents = contents

    def draw(self, draws):
        draws_list = list()
        if draws > len(self.contents):
            draws_list = self.contents
        else:
            draws_list = random.sample(self.contents, draws)
            for d in draws_list:
                self.contents.remove(d)
        return draws_list    
         


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Compute probability of observing exactly the expected balls"""
    N = num_experiments
    M = 0
    for n in range(N):
        hat_copy = copy.deepcopy(hat)
        result = list()
        draws = hat_copy.draw(num_balls_drawn)
        for ball in expected_balls.keys():
            result.append(expected_balls[ball] <= draws.count(ball))
        if all(result):
            M += 1
        else:
            M += 0            
    return M/N    


        
