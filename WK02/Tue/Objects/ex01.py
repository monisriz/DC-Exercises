# #1 Basics

class Person:

    def __init__(self, name, email, phone, friends=None, greet_count=0, unique_greet=None):
        self.name = name
        self.email = email
        self.phone = phone

        self.friends = friends
        if self.friends is None:
            self.friends = []

        self.greet_count = greet_count
        self.unique_greet = unique_greet
        if self.unique_greet is None:
            self.unique_greet = []


    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greet_count += 1
        if other_person.name not in self.unique_greet:
            self.unique_greet.append(str(other_person.name))

    def print_contact_info(self):
        """ from #2 Exercise - Make your own class """
        print(
        "{}'s email: {}, {}'s phone number: {}"
        .format(self.name, self.email, self.name, self.phone)
        )

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

    def num_unique_people_greeted(self):
        print("{} has greeted {} unique people.".format(self.name, len(self.unique_greet)))
        if self.greet_count == 0:
            print("{} has greeted no one.".format(self.name))


    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
paul = Person('Paul', 'paul@paulie.com', '123-456-7890')
monis = Person('Monis', 'monis@monis.com', '987-654-3210')
# sonny.greet(jordan)
# jordan.greet(sonny)
print("Sonny's contact info: {}, {}".format(sonny.email, sonny.phone))
print("Jordan's contact info: {}, {}".format(jordan.email, jordan.phone))
sonny.print_contact_info()
# sonny.friends.append(jordan)
# jordan.friends.append(sonny)
# print(len(sonny.friends))
# print(len(jordan.friends))


# print(len(jordan.friends))
# print(len(sonny.friends))

print("num of Sonny's friends: {}".format(sonny.num_friends()))
print("num of Jordan's friends: {}".format(jordan.num_friends()))
print("Sonny's greet count: {}".format(sonny.greet_count))
print("Jordan's greet count: {}".format(jordan.greet_count))

print(str(jordan))


sonny.greet(jordan)
jordan.greet(sonny)

sonny.greet(jordan)
jordan.greet(monis)

sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()

sonny.greet(paul)
sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()

# print("Jordan has {} friends.".format(len(jordan.friends)))
# print("Sonny has {} friends.".format(len(sonny.friends)))
jordan.add_friend(sonny)
sonny.add_friend(jordan)
jordan.add_friend(monis)
sonny.add_friend(paul)

if jordan.num_friends() == 0:
    print("Jordan doesn't have any friends.")
print("Jordan's friends:")
for i in range(jordan.num_friends()):
    print(jordan.friends[i].name)

if sonny.num_friends() == 0:
    print("Sonny doesn't have any friends.")
print("Sonny's friends:")
for i in range(sonny.num_friends()):
    print(sonny.friends[i].name)
