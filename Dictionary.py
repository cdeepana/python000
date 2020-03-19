person = dict(Name = "chathura", Age = 25, Salary = 15000) # mutable
print(person)
print(person["Name"])
person["Name"] = "chathura deepana"  # change the name values
print(person["Name"])
person["Address"] = "Mirigama, Sri Lanka"  # add the attribute its ok
print(person)
del person["Salary"]  # delete the attribute
print(person)


# mutable ====>    list / dictionary                    (this types we can append values to same memory location. So there are mutable )
# im-mutable ==>  int / float/ string/ tuple            (when int float change another values it saves different location not the previous values space)

# x=10
# id(x)
# type(x)