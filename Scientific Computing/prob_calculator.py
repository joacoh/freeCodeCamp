import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, num in kwargs.items():
            for i in range(num):
                self.contents.append(key)
        print(self.contents)

    def draw(self, number):
        total_removed = []
        if (number>len(self.contents)):
            return self.contents
        for i in range(number):
            random_ball = random.randint(0,(len(self.contents)-1))
            total_removed.append(self.contents[random_ball])
            self.contents.remove(self.contents[random_ball])
        return total_removed
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_drawn = hat_copy.draw(num_balls_drawn)
        for color in colors_drawn:
            if (color in expected_copy):
                expected_copy[color]-=1
        if(all(x<=0 for x in expected_copy.values())):
            count += 1
    return (count/num_experiments)

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)