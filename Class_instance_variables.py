class Dog:

    kind = "German Shepherd"  # Class variable

    """Creating the instance of the class"""
    def __init__(self, dog_name):  # Instance of the class
        self.dog_name = dog_name  # Instance variable


"""Creating the objects for the class"""
Dog3 = Dog("Pupa")  # Object of the class
Dog4 = Dog("Yellow")  # Object of the class

""" Debugging process to check if the result will be the same as declared above when executed."""
assert Dog3.kind == "German Shepherd"
assert Dog4.kind == "German Shepherd"

"""Running the script"""
if __name__ == '__main__':
    print(Dog3.kind)
    print(Dog3.dog_name)
    print(Dog4.kind)
    print(Dog4.dog_name)


"""................................................................................................................."""


class DogWithShareData:

    """This is a class example with a "bad choice" of Class variable, "mutable objects" such as "lists" and
    "dictionaries" are not to be used as class variables because just this "single list" would be shared by all Dog
    instances. """

    target_list = []  # Class variable

    """Creating the instance of the class"""
    def __init__(self, dog_name):  # Instance of the class - declaring all that what we want our class object to have.
        self.dog_name = dog_name  # Instance variable

    """Creating the method for the class"""
    def add_to_list(self, add_data):  # Method of the class
        self.target_list.append(add_data)  # Function that the method will perform when called.


"""Creating the objects of the class"""
Dog1 = DogWithShareData('Funfun')  # Creating object of the class, and declaring "Funfun" as the first dog name.
Dog2 = DogWithShareData('Dudu')  # Creating object of the class, declaring "Dudu" as the second dog name

"""Calling the method of the class to add the data (e.g "roll over") to the list"""
Dog1.add_to_list(add_data='roll over')  # Adding data to the "target_list" - just to show more details on how this works
Dog2.add_to_list("play dead")  # Same as above, adding data to the end of the list

"""Debugging process to check if the result will be the same as above when executed."""
assert Dog1.target_list == ['roll over', 'play dead']  # Unexpectedly shared by all dogs within the class
assert Dog2.target_list == ['roll over', 'play dead']  # Unexpectedly shared by all dogs within the class


"""Running the script"""
if __name__ == '__main__':
    print(Dog1.target_list)
    print(Dog2.target_list)
    print(Dog1.dog_name)
    print(Dog2.dog_name)


"""................................................................................................................."""


class DogCorrectClassDesign:

    """This is a class example of good choice of using instance variable instead of Class variable for "mutable
    objects" such as "lists" and "dictionaries" as this list will not be shared by all Dog instances but only with
    the instance it was assigned to."""

    """Creating the instance of the class"""
    def __init__(self, dog_name):  # Instance of the class with self, dog_name as 1st and 2nd positional arguments
        self.dog_name = dog_name  # Instance variable
        self.target_list = []  # Instance variable, declared as empty list & not part of instance positional arguments

    """Creating the method for the class"""
    def add_data_to_list(self,
                         data_to_be_added):  # Method of the class with self, data_to_be_added as positional arguments
        self.target_list.append(data_to_be_added)  # Function that the method will perform when called.
        """Here this method above is declared to add data to the end of the target list"""


"""Object of the class"""
Dog5 = DogCorrectClassDesign("Purple")
Dog6 = DogCorrectClassDesign("Red")

"""Calling the method of the class to add the data to the list"""
Dog5.add_data_to_list('roll over')
Dog6.add_data_to_list('play dead')

"""Debugging process to check if the result will be the same as above when executed."""
assert Dog5.target_list == ["roll over"]
assert Dog6.target_list == ["play dead"]


"""Running the script"""
if __name__ == '__main__':
    print(Dog5.target_list)
    print(Dog6.target_list)
    print(Dog5.dog_name)
    print(Dog6.dog_name)
