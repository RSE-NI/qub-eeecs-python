
people = {
    "Name": "George",
    "Age" : 34,
    "House_no": 1,
    "Street": "Acacia Avenue"
}

try:
    #  get the value from the name key
    print (people["Name"])

    #  get the value from a non-existent key
    print (people["luhiuhdfidhufiuhdf"])

except KeyError as e:
    #  handle key error specifically
    print (e, "No such key")

finally:
    print("Keys/values are:\n")
    for key,value in people.items():
        print(key, value)
