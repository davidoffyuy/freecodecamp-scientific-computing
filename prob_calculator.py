import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for (k, v) in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        
        print("kwargs:", str(kwargs))
        print("contents:", str(self.contents))
            
    def draw(self, count):
        ret_val = []

        for i in range(count):
            if len(self.contents) > 0:
                del_ind = random.randrange(0, len(self.contents))
                del_val = self.contents[del_ind]
                self.contents.remove(del_val)
                ret_val.append(del_val)

        return ret_val

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    total_exp = 0

    for i in range(num_experiments):
        i_hat = copy.deepcopy(hat)
        hat_result = i_hat.draw(num_balls_drawn)
        result_histo = {}
        for j in hat_result:
            result_histo[j] = result_histo.get(j, 0) + 1
        isSuccess = True    
        for (k, v) in expected_balls.items():
            if result_histo.get(k, 0) < v:
                isSuccess = False
        if isSuccess is True:
            success += 1
        total_exp += 1
    return success / total_exp