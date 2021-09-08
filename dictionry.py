# dictionry in python

students = {"name": "sameer","age": "20", "DOB": "19-August-1999"}
print(students["name"])
print(students.keys())
print(students.values())
print(students.items())
print(students.get("email", "not found"))
print(students.pop("name"))
print(students);

for i in students.items():
     print(i)



students = {1:{"name": "sameer","age": "20", "DOB": "19-August-1999"},
2:{"name": "sameer","age": "20", "DOB": "19-August-1999"},
3:{"name": "sameer","age": "20", "DOB": "19-August-1999"}}

print(students[1]);