import zipfile

# with zipfile.ZipFile('test.zip', 'w') as zip:
#     zip.write('text1.txt')
#     zip.write('text2.txt')


# with zipfile.ZipFile("test.zip","r")as zipfile:
#     file_list=zipfile.namelist()
#     print("content of the zipfile",file_list)
    
    
# file_to_extract = 'text2.txt'
# extraction_path = "C:/Users/python/Music"

# with zipfile.ZipFile('test.zip', 'r') as zipf:
#     if file_to_extract in zipf.namelist():
#         zipf.extract(file_to_extract, extraction_path)
#         print(f"'{file_to_extract}' has been extracted to '{extraction_path}'.")
#     else:
#         print(f"'{file_to_extract}' does not exist in the ZIP archive.")
        
file_to_extract = 'text1.txt'
extraction_path = "C:/Users/python/Music"

with zipfile.ZipFile('test.zip', 'r') as zipf:
    if file_to_extract in zipf.namelist():
        zipf.extract(file_to_extract, extraction_path)
        print(f"'{file_to_extract}' has been extracted to '{extraction_path}'.")
    else:
        print(f"'{file_to_extract}' does not exist in the ZIP archive.")