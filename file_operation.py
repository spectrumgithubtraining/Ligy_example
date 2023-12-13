f = open("demo.txt","r")          #opens file with name of "test.txt"

print(f.read())                         #reads the first two character of the file

print(f.read())                          #reads the entire file

print(f.readline())                      #read first line of the file

print(f.readline(3))                     #reads the first three chars of the file

print(f.readlines())                     #reads the entire lines of the file

print(f.readlines(3))                    #reads the third line of the file

f.close()