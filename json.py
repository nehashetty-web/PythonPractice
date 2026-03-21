import json
student = {
    "name": "Neha",
    "marks": 95,
    "course": "Python"
}
json_student=json.dumps(student)
print(json_student)
json.dump(student,student.json)
json.load(student.json)
