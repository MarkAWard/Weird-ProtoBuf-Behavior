from household_pb2 import Parent, Child, Pet

matt = Child()
matt.name = "Matt"
interest = matt.interests.add()
interest.rating = 5
interest.sport = "quidditch"

matt_clone = Child()
matt_clone.MergeFrom(matt)
interest = matt_clone.interests[0]
which_hobby = interest.WhichOneof('hobby')
sport = interest.sport

print matt_clone
print "Which Hobby: %s" %(which_hobby)
print "Sport: %s\n" %(sport)


mark = Child()
mark.name = "Mark"
interest = mark.interests.add()
interest.rating = 5
interest.progamming_language = "python"

mark_clone = Child()
mark_clone.ParseFromString(mark.SerializeToString())
interest = mark_clone.interests[0]
which_hobby = interest.WhichOneof('hobby')
sport = interest.sport

print mark_clone
print "Which Hobby: %s" %(which_hobby)
print "Sport: %s\n" %(sport)