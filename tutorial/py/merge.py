
# youtube.com/onlineaid

dic1 = {"name": "tony", "age": 25, "city": "New York"}
dic2 = {"name": "joni", "age": 25, "city": "Los Angeles"} 

# merge = dic1.copy()

# merge.update(dic2)
# print(merge)

merge = dic1 | dic2
print(merge)