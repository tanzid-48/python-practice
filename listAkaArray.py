skills = ["Python", "JavaScript", "TypeScript", "MongoDB"]

print(skills[0])  
print(skills[-1]) 
print(len(skills))    


skills = ["Python", "JavaScript"]

skills.append("TypeScript")     # শেষে যোগ করে → ['Python', 'JavaScript', 'TypeScript']
skills.remove("JavaScript")     # নির্দিষ্ট ভ্যালু বাদ দেয় → ['Python', 'TypeScript']
skills.insert(0, "C++")         # নির্দিষ্ট index এ ঢোকায় → ['C++', 'Python', 'TypeScript']
skills.sort()                   # সাজায় (alphabetically)
print(skills)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])    # [20, 30] - index 1 থেকে 2 পর্যন্ত (3 বাদ)
print(numbers[:2])     # [10, 20] - শুরু থেকে index 1 পর্যন্ত
print(numbers[2:])     # [30, 40, 50] - index 2 থেকে শেষ পর্যন্ত



Skills = ['MERN','Next.js','TS','Fluter','Java']
print(Skills[0])
print(Skills[-1])
Skills.append('python')
print(len(Skills))
print(Skills)
