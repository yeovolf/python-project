
# file = open('story.txt', 'a')
# file.write("we've provide you with the first chapter of Alice's Adventures in Wonderland to give you some sample test to work with. This is also the text used in the tests.")
def copy(file):
  with open('story.txt', 'r') as firstfile, open('story_copy.txt', 'w') as secondfile:
    for line in firstfile: 
         secondfile.write (line)
    
copy('file') 
