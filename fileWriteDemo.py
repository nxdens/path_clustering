f = open("demofile3.txt", "w")
f.write(" ".join(("Woops! I have deleted the content!","\n")))
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read()) 