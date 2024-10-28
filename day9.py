programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

programming_dictionary["loop"]="repeats untill a condition is not satisfied"

print(programming_dictionary)

empty_dictionary={}

programming_dictionary["Bug"]="redefined value"
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key)

capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]