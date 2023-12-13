import json    #importing json module

# d={'a':1,'b':6,'c':'CLASS'} # create a dictionary or any type of data

# data=json.dumps(d)  #dumps converts the dict data to string type
# #json converts all files to a common file type using dumps and dump

# ## 'dumps' converts to string and 'dump' to a non type data

# print("type of data is ",type(data)) ##this will print the type of data

# with open('test.txt','w') as my_file: ## dumps uses json files
# 	my_file.write(data) ##writing

# with open('test.txt','r') as my_file:
# 	a=my_file.read()
# 	print("d = ",a)
# 	print("type after read ",type(a))
# 	d1=json.loads(a)
# 	print("type after loads",type(d1))

data1=[{1:'denu',2:'pinchu',3:'elizabeth',4:'denova'}]
my_file3=open('json.txt','w')

a1=json.dump(data1,my_file3)


my_file3=open('json.text','r')
#b=my_file3.read()
#print("type of b ",type(b))

b1=json.load(my_file3)

my_file3=open('json.txt','r')
print(my_file3.read())
my_file3.close()