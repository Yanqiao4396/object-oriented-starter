# define a class to represent a Dog entity
class Dog:

    # TODO: define the constructor for the Dog class
    def __init__(self, name, age, breed):

    # define a description method for the dog
    def description(self):
        return f"{self.name} is a {self.age} years old {self.breed}"

    # define an action method for the dog
    def action(self, action):
        return f"Hey, {self.name} {action}!"

    # TODO: define a __str__ method for the dog
    def __str__(self):


# display a message indicating the purpose of this script
print("Creating dog objects using a object-oriented approach!")
print()

# TODO: create an instance of the Dog class for Bosco

# TODO: create an instance of the Dog class for Faith

# display the textual details of the Bosco instance
# note that this only works if __str__ is available
print(bosco)
print()
print(f"The dog's name is: {bosco.name}")
print(f"The dog's age is: {bosco.age}")
print(f"The dog's breed is: {bosco.breed}")
print()

# TODO: call the description method for Bosco

# TODO: call the action method for Bosco
# make the specific action a "roll over"

# display the textual details of the Faith instance
# note that this only works if __str__ is available
print(faith)
print()
print(f"The dog's name is: {faith.name}")
print(f"The dog's age is: {faith.age}")
print(f"The dog's breed is: {faith.breed}")
print()

# TODO: use the description method for the Faith object

# TODO: use the action method for the Faith object
# make the specific action a "waive bye-bye"
