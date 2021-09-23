import json



file = open("C://Users//Nani Madhan//OneDrive//Desktop//nani.json", 'r')

json_file = file.read()

obj = json.loads(json_file)


print(str(obj['FirstName']))
print(str(obj['LastName']))
print(str(obj['Address']))



