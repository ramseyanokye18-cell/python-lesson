'''
# file handling and classes
myfile= open("file1.txt", "w")
myfile.write("I am a student\n")
myfile.write("I am learning python\n")
myfile.write("I am enjoying it\n")    
myfile.close()
#myfile= open("notes.txt", "r")
with open("FILE1.txt") as f:
try:
    with open("FILE1.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("Finished trying to read the file.")  
'''
with open("new_file.txt", "w") as f:
    f.write("I am a boy.\n")
    f.write("I am 18.\n")
    f.write("I am tall\n")
with open("new_file.txt", "r") as f:
   print(f.read())   

with open("C:\\Users\\Ramsey Anokye\\OneDrive\\Desktop\\file1.txt") as f:
   print(f.read())
   

 

 



   