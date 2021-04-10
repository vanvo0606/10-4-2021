import random
import cmath


class PERSON(object):
    _age = None
    _name = None
    _gender = None
    def __init__(self, name=None, gender=None):
        self._age = random.randrange(17.25)
        if gender is None:
            self._gender = random.choices(['female', 'male'])
        if name is None:
            self._name = 'default Name'
            

class STUDENT(PERSON):
    _id = None
    _room = None
    _grade = None
    
    def __init__(self, number, grade, room):
        super()
        super().__init__()
        self._id = number
        self._grade = grade
        self._room = room
        
        
@property
def age(self):
    return super()._age


@property
def name(self):
    return super()._name


@property
def gender(self):
    return super()._gender

