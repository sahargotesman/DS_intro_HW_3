#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Sahar Gotesman 206014300

##Q1

def read_line(n,file):
    try:
        fhand = open(file,'r')
        if not isinstance(n, int):
            return "invalid input detected"
        count= 0
        for line in fhand:
            count = count + 1
            if count == n:
                return line
        if n > count:
            return "line"+" "+str(n)+" "+"doesn't exist"
    except:
        return "file not found"
    fhand.close()
  
#### Tests   
#print(read_line(4,"/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex3_text.txt"))
#print(read_line(9,"/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex3_text.txt"))
#print(read_line(29,"/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex3_text.txt"))
#print(read_line("c","/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex3_text.txt"))
#print(read_line(9,"/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex4_text.txt"))



##Q2

def longest_words(file):
  try:
    long_W_list=[]
    fhand= open(file,'r')
    fhand= fhand.read()
    fhand= fhand.replace('.', ' ')
    fhand= fhand.replace('-', ' ')
    fhand= fhand.replace(',', ' ')
    line= fhand.split()
    line = sorted(line, key=len, reverse = True)
    long_W_list = line[0:5]
    return long_W_list
  except:
    return "file not found"
  fhand.close()

####Tests
# print(longest_words("/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex3_text.txt"))
# print(longest_words("/Users/il016140/Documents/OneDrive - Ariel University/Year 3/semester b/introw- Data sience/Tasks- spyder/assignment3/DS_Intro_HW_3/ex4_text.txt"))
# print(longest_words("ddd"))
# print(longest_words(4))




