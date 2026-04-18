def health(name,genotype,physical_injuries):
    print(f"my name is {name}")
    print(f"my genotype is {genotype}")
    print(f"i have a {physical_injuries}")
health ("adumati noah", "AA", "leg sparain")
 

def grade():
    score = int(input("enter score"))
    if score >= 70:
        print("grade A ")
    elif score >= 60:
        print("grade B  ")
    elif score >= 50:
        print("grade c")
    elif score >= 45:
        print("grade d")
    else:
        print("grade F")
grade()