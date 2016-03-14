# Weird-ProtoBuf-Behavior

Originally, I believed there was in issue having nested `oneof` fields in a message that caused `WhichOneOf` to return `None` for the inner message when checking which field is set. Turns out that the issue is not the nesting of messages with `oneof` fields but rather how that inner message gets initialized. 

When initializing a message within another message, you cannot use simple assignment of a pre-initailzed object to a nested message. This would throw an error like `AttributeError: Assignment not allowed to composite field "nested_message" in protocol message object.` You would have to assign to each field in that nested message, but a better way is to use one of the provided instance methods to initialize that nested message from an object you may alredy have such as `MergeFrom` or `ParseFromString`. `MergeFrom` is nice as you can hand it a protobuf instance and will set the attributes of the object it was called from, and you **almost** have identically functioning objects. `ParseFromString` sets the current objects attributes from a serialized protobuf that you might get from `SerializeToString`.

So what did I mean by "you **almost** have identically functioning objects"? Well this all started from my pains with `WhichOneOf` returning `None` when I was positive that one of the fields was certianly set. And you guessed it, when I initialized with `MergeFrom` the `WhichOneOf` would return `None`. Well at least sometimes it would and in other examples it actually worked as expected... #confused

So I cooked up some examples to show what's going on:

Output of `test1.py` and `test2.py` are the same and both use `MergeFrom` to set a nested message that contains a `oneof`:
```
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

Here's the output of `test3.py` and we get the expected result when using `ParseFromString`:
```
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
Which Hobby: sport
	programming_language: 
	sport: quidditch
Name: Mark 
Which Hobby: progamming_language
	programming_language: python
	sport: 
Name: Bucky 
Which Animal: dog
	is a dog: True
	is a cat: False
```

Then I created another test that did away with the nesting of messages and just intialized new objects from exisiting ones, testing both of the initializers and sure enough when using `ParseFromString` I got the desired behavior. Here's the output for `test4.py`: 
```
name: "Matt"
interests {
  rating: 5
  sport: "quidditch"
}

Which Hobby: None
Sport: quidditch

name: "Mark"
interests {
  rating: 5
  progamming_language: "python"
}

Which Hobby: progamming_language
Sport: 
```
