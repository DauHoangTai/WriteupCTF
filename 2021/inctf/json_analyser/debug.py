import ujson
import json
import re
role = 'super\u0075ser","name":"admin'
print(len(role))
if "superuser" in role:
  role=role.replace("superuser","")
if " " in role:
  print("no hacking")
if len(role)> 30:
  print("invalid role")
data='"name":"user","role":"{0}"'.format(role)
no_hecking = re.search(r'"role":"(.*?)"',data).group(1)
if(no_hecking == None):
  print("bad data")
if no_hecking == "superuser":
  print("not hacking")
data = '{'+ data + '}'
try:
  user_data = ujson.loads(data)
except:
  print("bad_format")
print(f"{user_data['name']}:{user_data['role']}")


# super\u0075ser","name":"admin