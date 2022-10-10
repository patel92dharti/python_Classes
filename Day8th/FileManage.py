file =open("Tops.txt","w")
file.write("New File has been created Now.")
file.close()
print("*"*30)
print("file written successfully")
print("*"*30)

file=open("Tops.txt","r")
print(file.read())
file.close()
print("File read Successfully")
print("*"*40)


file=open("Tops.txt","a")
file.write("Hello Word my name is Dharti patel")
file.close()
print("File append successfully")
print("*"*40)

file=open("Tops.txt","w+")
file.write("What is github? \nIt is a web-based Git repository. "
           "This hosting service has cloud-based storage. "
           "GitHub offers all distributed version control and source code")
print("Current File Position:",file.tell())
file.seek(0)
print(file.read())
file.close()
print("*"*40)


