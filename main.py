def flat_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

nested_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flat_sort(nested_array)
print(result) 

# this solution takes the inputed array, and transfers it into the list "arr", thus keeping the original array intact and not modified 
# the solution is a pure function, because the same input will always have the same result, and has no side effects 
# it is not a higher order function, because it does not accept a function as an argument, instead it takes an array, and it does not return a function
# I think it depends on the programer's familiarity with their language of choice, but I think functional programming would be the easiest way to tackle the problem
# the original data is immutable, and cannot be changed, on top of the use of pure functions, this makes everything predictable, and you can expect consistent results every time.



class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"


pod = Podracer(100, "damaged", 5000)
pod.repair()
print(pod.condition) 

new_pod = AnakinsPod(2, "perfect", 7000)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(3, "new", 8000)
target_pod = Podracer(5, "perfect", 6000)
third_pod.flame_jet(target_pod)
print(target_pod.condition) 




# each class encapsulates (bundles) data, and behaviors. AnakinsPod and SebulbasPod both inherit from the Podracer class. Abstraction, functions like repair and boost, Users of Podracer don't need to understand how these functions work to use them
# given the nature of the problem, OOP makes things easier, for example using inheritance so you don't have to repeat functions, and using encapsulation keeps everything bundled neatly together without needing to use up so much space / lines of code.



# I believe each coding paradigm has their own use cases in which they're the better solution, but generally I don't think one is "better" than the other.
# functional programming seems more appealing to me because it makes more sense and it's easier to see what's going on at first glance, OOP seems like there would be a lot of backtracking and constant checking on previously written code.
# OOP defintely requires more thinking power for me to understand what is going on. I think learning some real world use cases and seeing how the code benifits by using this can really help deepen the understanding of this concept.