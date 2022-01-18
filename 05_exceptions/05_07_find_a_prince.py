# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

#custom expection
# raise exception if the first 100 charactersof book have Prince
#pathlib
#pathlib.Path().home() #'C:\\Users\\jsiu\\'
import os

file_path=os.path.dirname(__file__)
file_path_book=os.path.join(file_path,"books")

paths={os.path.join(file_path_book,'crime_and_punishment copy.txt'):"crime",
#'C:\\Users\\jsiu\\Documents\\codingnomads\\python-301-main_jsiu\\python-301-main\\05_exceptions\\books\\pride_and_prejudice.txt':"pride", 
os.path.join(file_path_book,'war_and_peace.txt'):"war"}
# put into a list

prob_dict=dict()

"""
# def args
def open_read(path_list):
    for key, value in path_list.items(): # without the asterisk means just gimme the tuple
        file=open(i, "r", encoding="utf-8")
        file_list=[]
        for j in file:
            file_line=file.readline()
            file_list.append(file_line)
        print(file_list)
open_read(paths)




    #how to know what encoding to us
    # how to simplify this?
"""
# global variable vs argument
#pass by object and pass by value

class PrinceError(Exception):
    pass

class ReadFiles:
    def open_read(path_list):
        for key, value in path_list.items(): # without the asterisk means just gimme the tuple
            prob_dict[f"{value}_file"]=open(key, "r", encoding="utf-8")
            prob_dict[f"{value}_file_list"]=[]
            for j in prob_dict[f"{value}_file"]:
                #prob_dict[f"{value}_file_line"]=prob_dict[f"{value}_file"].readline()
                prob_dict[f"{value}_file_line"]=prob_dict[f"{value}_file"].read()

                #prob_dict[f"{value}_file_list"].append(prob_dict[f"{value}_file_line"])
            #print(prob_dict[f"{value}_file_list"])
            file_snippet=prob_dict[f"{value}_file_line"][0:1000]
            print(type(file_snippet))
            if "prince" in file_snippet.lower():
                raise PrinceError("In first 1000 chracters have Prince")

            

ReadFiles.open_read(paths)



#read line and keep track of how many characters
#define dictionary within open read

