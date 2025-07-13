notes=input().upper() # get input of the notes change it to upper case
seperate=notes.split("|") # apply split to split it by |
major_notes=[] # assign the empty list
for n in seperate :   
    major_notes.append(n[0]) #append the only first characters of list
# count the no of a,d,e,c,f,g
a_notes=major_notes.count("A")+major_notes.count("D")+major_notes.count("E")
c_notes=major_notes.count("C")+major_notes.count("F")+ major_notes.count("G")

if a_notes>c_notes:
    print("A-mol") # prints it is a a note
elif a_notes<c_notes:
    print("C-dur") # prints it is a c note
else:
    last_note = notes[-1]  # checks the last letter of note
    if last_note == "A" or last_note=="E" or  last_note =="D":
        print("A-mol") # depends on the last letter of the note it prints the note
    elif last_note == "C" or  last_note =="F" or  last_note =="G" :
        print("C-dur")