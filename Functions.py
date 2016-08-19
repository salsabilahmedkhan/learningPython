# Modify this function to return a list of strings as defined above
def list_benefits():

    mylist = []
    mylist.append("More organized code")
    mylist.append("More readable code")
    mylist.append("Easier code reuse")
    mylist.append("Allowing programmers to share and connect code together")
    return mylist
# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(info):
    return info+" is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print build_sentence(benefit)

name_the_benefits_of_functions()
