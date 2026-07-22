student = {
    "name": "Tanzid",
    "university": "Pundra University",
    "cgpa": 3.80,
    "is_active": True
}

print(student["name"])        # Tanzid
print(student["cgpa"])        # 3.8

print(student.get("name"))    # Tanzid
print(student.get("phone"))   # None (key নেই, কিন্তু error হবে না)

student["semester"] = 7          # নতুন key যোগ
student["cgpa"] = 3.90            # আগের value আপডেট

del student["is_active"]

print(student.items())

profile = {
    "name": "Tanzid",
    "university": "Pundra University",
    "semester": 7,
    "skills": ["MERN", "Next.js", "TypeScript"]
}

print(profile.get("name"))
print(profile.get("skills"))
profile["cgpa"]=3.85
print(profile.items())