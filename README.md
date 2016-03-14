# Weird-ProtoBuf-Behavior

When using nested `oneof` fields, `WhichOneOf` returns None for the inner object. Could be from the bizarre way that it gets set.

Output of test.py:
```
name: "Matt"
interests {
  rating: 5
  sport: "quidditch"
}

name: "Mark"
interests {
  rating: 5
  progamming_language: "python"
}

name: "Bucky"
dog: true

name: "Mom"
children_and_pets {
  child {
    name: "Matt"
    interests {
      rating: 5
      sport: "quidditch"
    }
  }
}
children_and_pets {
  child {
    name: "Mark"
    interests {
      rating: 5
      progamming_language: "python"
    }
  }
}
children_and_pets {
  pet {
    name: "Bucky"
    dog: true
  }
}

Name: Matt 
Which Hobby: None
	programming_language: 
	sport: quidditch
Name: Mark 
Which Hobby: None
	programming_language: python
	sport: 
Name: Bucky 
Which Animal: None
	is a dog: True
	is a cat: False
```
