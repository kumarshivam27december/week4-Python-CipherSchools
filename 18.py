#  Importing random module
import random
  
# Defining list of phrases which will help to build a story
  
start_sentence = ["hi","hello","greating"]
audience=["everyone","everybody"]
time=["good morning","good afternoon","good evening","good noon"]
my_name=["this is","i am ",'my name is']
random_name=["Utkarsh","shivam","aman","rahul","jack"]
feelings=["i love","i like"]
subject=["coding","singing","dancing","playing cricket"]
ending=["thanks","thank you","regards"]
# Selecting an item from each list and concatenating them.
print(random.choice(start_sentence)+" "+random.choice(audience)+" "+
      random.choice(time)+" "+random.choice(my_name) +" "+
      random.choice(random_name)+" "+random.choice(feelings)+" "+
      random.choice(subject)+" "+random.choice(ending))