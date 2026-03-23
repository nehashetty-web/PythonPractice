

import json

place={"city":"hyderabad","location":"south"}

json_place=json.dumps(place)
print(json_place)

file=open("place.json","w")
json.dump(place,file)
file.close()

file=open("place.json","r")
data=json.load(file)
file.close()

print(data["location"])