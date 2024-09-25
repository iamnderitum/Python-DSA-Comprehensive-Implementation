import time
import redis

redisObj = redis.Redis(host="localhost", port=6379, db=0)
pipeObj = redisObj.pipeline()

pipeObj.set("Name", "Moses")
pipeObj.set("Age", 35)
pipeObj.set("Family", 3)
pipeObj.set("Course", "Information Technology")

pipeObj.execute()

print("\n ----------------------- Original values")
print(f"Name: {redisObj.get('Name')}")
print(f"Age: {redisObj.get('Age')}")
print(f"Family: {redisObj.get('Family')}")


pipeObj.append("Name", "Wambui")
pipeObj.incr("Age")
pipeObj.execute()
print(f"Age: {redisObj.get('Age')}")