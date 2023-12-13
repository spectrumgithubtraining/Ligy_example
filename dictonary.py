y =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=y["model"]
print(x)
#Upadte
y["year"]=2000
print(y)
#Adding
y["Milage"]=3000
print(y)
del y['Milage']
print(y)

d_1 = {'A': 15, 'B': 10, 'C' : 12 }  
d_2 = {'E': 18,'B': 20,'D' : 16 }  
d_1.update(d_2)  
print('Updated dictionary:')  
print(d_2)  
print(d_1.items())


#One or More Field
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using {**dict1, **dict2, **dict3}
concatenated_dict1 = {**dic1, **dic2, **dic3}

# Method 2: Using update() method
concatenated_dict2 = dic1.copy()
concatenated_dict2.update(dic2)
concatenated_dict2.update(dic3)

# Display the concatenated dictionaries
print("Concatenated Dictionary (Method 1):", concatenated_dict1)
print("Concatenated Dictionary (Method 2):", concatenated_dict2)
