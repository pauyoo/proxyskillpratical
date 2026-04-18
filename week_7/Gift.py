## Functions 

def occupation(name, place_of_work, job):
    print(f"My name is {name}")
    print(f"I work in a {place_of_work}")
    print(f"I am a {job} by profession")

occupation("Gift", "hospital", "cardiologist")


## Using the input 
def work(name, place_of_work, job):
    print(f"My name is {name}")
    print(f"I work in a {place_of_work}")
    print(f"I am a {job} by profession")

work(input("Your name"), input("Your place of work"), input("Your job"))