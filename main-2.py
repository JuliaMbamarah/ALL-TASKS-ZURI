class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob = Student("Peter", 34, "UI/UX", 23.4)

def change_name(self, name):
    self.name = name
    print(self.name)

def change_age(self, age):
    self.age = age
    print(self.age)

def change_tracks(self, tracks):
    self.name = tracks
    print(self.tracks)

def change_score(self, score):
    self.score = score
    print(self.score)
# Expected methods
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)