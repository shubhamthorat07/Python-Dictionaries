d = {"Movie" : "Titanic", "Genre" : "Romance", "Hours": "210mins", "Budget": "$200m"}
print(d)




d["Actor"] = "Leonardo Di Caprio"
print(d)




d["Actress"] = "Kate Winslet"
print(d)





print(d["Movie"])
print(d["Budget"])




print(d.get("Genre"))
print(d.get("Movie"))




for x in d:
	print(x)



for key in d:
	print(key,d[key])


print(d.keys())

print(d.values())

print(d.items())


r = d.pop("Genre")
print(d)
print(d,r)




r1 = d.popitem()
print(d)



d.clear()
print(d)