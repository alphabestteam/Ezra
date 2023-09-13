from point import Point

if __name__ == "__main__":
    point1 = Point(4, 5)
    point2 = Point(4, 5)

    print(point1 == point2)
    print(point1, point2)
    print(point1 + point2)

    """ 
    The issue with this code is:
    1. that when you do the == it checks the 
    memory location of each object and they're not the same. however we don't 
    want to check the memory location of that objects, rather what's inside them.
    to do that we'll need to override the __eq__() method.
    
    2. when we're printing the objects, we're printing the location of the objects
    in the memory and not what's inside them. to fix that we'll need to override the 
    __str__() method.

    3. when we're trying to add the two objects we can't because by default the + operator
    is designed to add only integer values so we'll need to override th __add__() method. 
    """
