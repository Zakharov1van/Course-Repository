family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 15),
  'son_young': ('Mark', 10)
}

ages_lst = []
for member in family:
    ages_lst.append(family[member][1])
max_age = max(ages_lst)
min_age = min(ages_lst)
print(f"The difference between oldest and youngest age in the family is {max_age - min_age} years")
