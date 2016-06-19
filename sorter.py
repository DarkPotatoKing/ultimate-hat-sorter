import random

FILENAME = 'duohat.tsv'
participants = list()

skill_equivalent = dict()
experience_equivalent = dict()

experience_equivalent['< 1 year'] = 0
experience_equivalent['1-2 years'] = 1
experience_equivalent['3-5 years'] = 2
experience_equivalent['6-7 years'] = 3
experience_equivalent['> 7 years'] = 4

skill_equivalent['Beginner'] = 0
skill_equivalent['Intermediate'] = 1
skill_equivalent['Adept'] = 2
skill_equivalent['Expert'] = 3

def draft(x):
    groups = list()

    for i in x:
        if len(groups) == 0:
            groups = range(1,9)
            random.shuffle(groups)

        i.group = groups.pop()


class Participants(object):

    def __init__(self, arg):
        arg = [i.strip() for i in arg]
        self.timestamp = arg[0]
        self.name = arg[1].upper()
        self.age = int(arg[2])
        self.sex = arg[3]
        self.contact_number = arg[4]
        self.experience = arg[5]
        self.skill_level  = arg[6]
        self.teams = arg[7].replace(',', '/')
        self.estimated_skill = skill_equivalent[self.skill_level] * 25 + experience_equivalent[self.experience] * 5
        self.group = 0

    def __repr__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.group, self.name, str(self.age), self.sex, self.experience, self.skill_level, self.estimated_skill, self.teams)

    def __lt__(self, other):
        return self.estimated_skill < other.estimated_skill




with open(FILENAME, 'r') as f:
    participants = [i.strip().split('\t') for i in f.readlines()]

participants = [Participants(i) for i in participants]
participants.sort(reverse = True)

males = filter(lambda x: x.sex == 'M', participants)
females = filter(lambda x: x.sex == 'F', participants)

draft(males)
draft(females)

participants.sort(key = lambda x: x.name)
participants.sort(key = lambda x: x.age)
participants.sort()
participants.sort(key = lambda x: x.sex)
participants.sort(key = lambda x: x.group)

print ','.join(['Group', 'Name', 'Age', 'Sex', 'Playing Experience', 'Experience Level', 'Teams'])
for i in participants:
    print i