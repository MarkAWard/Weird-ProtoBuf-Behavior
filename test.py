from household_pb2 import Parent, Child, Pet

matt = Child()
matt.name = "Matt"
interest = matt.interests.add()
interest.rating = 5
interest.sport = "quidditch"

mark = Child()
mark.name = "Mark"
interest = mark.interests.add()
interest.rating = 5
interest.progamming_language = "python"

bucky = Pet()
bucky.name = "Bucky"
bucky.dog = True

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
            which_hobby = interest.WhichOneof('hobby')
            lang = interest.progamming_language
            sport = interest.sport
            print "Name: %s \nWhich Hobby: %s" %(being.name, which_hobby)
            print "\tprogramming_language: %s" %(lang)
            print "\tsport: %s" %(sport)
    if key == 'pet':
    	which_animal = being.WhichOneof('animal')
    	dog = being.dog
    	cat = being.cat
    	print "Name: %s \nWhich Animal: %s" %(being.name, which_animal)
    	print "\tis a dog: %s" %(dog)
    	print "\tis a cat: %s" %(cat)