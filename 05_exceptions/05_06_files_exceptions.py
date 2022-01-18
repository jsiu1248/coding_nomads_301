# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

#open war_peace and read and store in variable
#make copy of crime and overwrite with blank
#loop over three files and print only first character
#what is a traceback?

war_path = 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-301-main_jsiu\\python-301-main\\05_exceptions\\books\\crime_and_punishment copy.txt'
crime_path='C:\\Users\\jsiu\\Documents\\codingnomads\\python-301-main_jsiu\\python-301-main\\05_exceptions\\books\\pride_and_prejudice.txt'
pride_path='C:\\Users\\jsiu\\Documents\\codingnomads\\python-301-main_jsiu\\python-301-main\\05_exceptions\\books\\war_and_peace.txt'

war_file=open(war_path, "r", encoding="utf-8")
crime_file=open(crime_path, "r", encoding="utf-8")
pride_file=open(pride_path, "r", encoding="utf-8")

war_list=[]
for i in war_file:
    war_line=war_file.readline()
    war_list.append(war_line)

crime_list=[]
for j in crime_file:
    crime_line=crime_file.readline()
    crime_list.append(crime_line)

pride_list=[]
for k in pride_file:
    pride_line=pride_file.readline()
    pride_list.append(pride_line)

try:
    print(war_list[0][0])
    print(crime_list[0])
    print(pride_list[0][0])
except:
    print("One of them is empty")


#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?