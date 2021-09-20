# LISTS PROPERTIES
# - Ordered
# - Changeable
# - Allows Duplicate items

cars = ["audi", "ferrari", "rangerover"]

# LIST METHODS

# index
cars[0]                 # audi
# append
cars.append("Innova")   # ['audi', 'ferrari', 'rangerover', 'Innova']

# insert
cars.insert(0, "bmw")   # ['bmw', 'audi', 'ferrari', 'rangerover', 'Innova']

# pop
cars.pop()              # ['bmw', 'audi', 'ferrari', 'rangerover']

# pop with index 
cars.pop(1)             # ['bmw', 'ferrari', 'rangerover']

# reverse
cars.reverse()          # ['rangerover', 'ferrari', 'bmw']

# count 
cars.count("bmw")       # 1
cars.count("audi")      # 0

# clear
cars.clear()            # []
