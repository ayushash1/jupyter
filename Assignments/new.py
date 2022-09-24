# dictionary is nothing but key value pair

d1 = {}
print(type(d1))

d2 = {
    "harry": "burger",
    "rohan": "fish",
    "skillf": "roti",
    "shubham": {"b": "maggie", "l": "roti", "d": "chicken"}

}
# d2["ankit"] = "junk food"
# d2["salman khan"] = "kebab"
# del d2["salman khan"]
# print(d2)

d3 = d2.copy()
del d3["harry"]
print(d3)
