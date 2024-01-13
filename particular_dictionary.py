# So Hey guys how's going on

# TOday we will learn about something new in dictionary

# So here is our list having dictionries
movies =[
  {"name" : "Rocket singh" , "Year" : 2010 , "Hero" : "ranbir kapoor"},
  {"name" : "bazaar" , "Year" : 2008 , "Hero" : "Harsh"},
  {"name" : "sujan patel" , "Year" : 2012 , "Hero" : "sujan"}
]

# Here we start process of getting all details about single movie 
for emplyee in movies:
  if emplyee["name"]=="sujan patel":
    print("Name:" , emplyee['name'])
    print("Year:", emplyee['Year'])
    print("hero:" , emplyee['Hero'])
