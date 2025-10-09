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

    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = "left"

    def __init__(self, title, pupils_count, group_leader):
        super().__init__(title, pupils_count, group_leader)


    def move(self):
        print('run fast')

class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('go slowly')

first_a = PrimaryGroup('1a',18,'mf' )
first_b = PrimaryGroup('1b',20,'td')
eleven_a = HighGroup('11a', 20, 'pp')
print(first_a.title)
print(first_b.title)
print(first_a.pupils)
first_a.study()
first_a.move()
eleven_a.move()
print(eleven_a.title)
print(eleven_a.pupils_count)