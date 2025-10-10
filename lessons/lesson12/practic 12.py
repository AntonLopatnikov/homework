from abc import abstractmethod

class Group:
    pupils = True
    scholl_name = 42
    director = "marivanna"

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader



    def study(self):
        print('sit down and read')

    @abstractmethod
    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = "left"

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room


    def move(self):
        print('run fast')

class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('go slowly')

class MediumGroup(Group):
    max_age = 15
    min_age = 10


first_a = PrimaryGroup('1a', 15, 'sd', 112)
first_a.class_room = 100000
print(first_a.class_room)