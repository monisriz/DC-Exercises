# Exercise 2: Nested Dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1
print("Email address of Ramit:")
print(ramit['email'])
print("\n")
# 2
print("First of Ramit's interests:")
print(ramit['interests'][0])
print("\n")
# 3
print("Email address of Jasmine:")
print(ramit['friends'][0]['email'])
print("\n")
# 4
print("Second of Jan's interests:")
print(ramit['friends'][1]['interests'][1])
