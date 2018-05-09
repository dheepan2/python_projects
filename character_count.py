'''This program will count each characters appearance in the file passed'''
def char_count(file):
  dictionary={}
  with open(file,'r') as f:
    data=f.read()
    char_tuple=tuple(data)
    for entry in char_tuple:
      if entry not in dictionary.keys():
        dictionary[entry]=1
      else:
        dictionary[entry]+=1
  for k,v in dictionary.items():
    print ("character {} is : {} times".format(k,v))
    
char_count('readme.txt')
