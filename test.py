from household_pb2 import Parent, Child, Pet

matt = Child()
matt.name = "Matt"
interest = matt.interests.add()
interest.rating = 5
interest.sport = "quidditch"
print matt

mark = Child()
mark.name = "Mark"
interest = mark.interests.add()
interest.rating = 5
interest.progamming_language = "python"
print mark

bucky = Pet()
bucky.name = "Bucky"
bucky.dog = True
print bucky

beings = [matt, mark, bucky]

mom = Parent()
mom.name = "Mom"
for being in beings:
    obj = mom.children_and_pets.add()
    eval("obj."+being.__class__.__name__.lower()).MergeFrom(being)
print mom

for obj in mom.children_and_pets:
    key = obj.WhichOneof('child_or_pet')
    being = getattr(obj, key)
    if key == 'child':
        for interest in being.interests:
            print interest.WhichOneof('hobby'), interest.progamming_language, interest.sport
    if key == 'pet':
    	print being.WhichOneof('animal'), being.dog, being.cat