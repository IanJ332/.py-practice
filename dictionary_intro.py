# Key => Value
from requests import delete

capital ={
    "United States": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris",
    "Russia": "Mascow"
}

# .get() to get the value of the key
print(capital.get("United States"))

# .update() to update data
capital.update({"China": "Beijing"})
print(capital.get("China"))

# .pop() delete the key
capital.pop("China")
print(capital)

# .items() to get every keys
print(capital.items())

# .value() to get every value
print(capital.values())