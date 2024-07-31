import json

#The function receives a first string with the filters and a second one in JSON format
def search(filter_query, full_json):

    #Transform the JSON string into a Python dict
    json_obj = json.loads(full_json)

    #Get the list of values stored in the result variable
    all_res = json_obj["result"]

    #Create an empty list to store the final values filtered
    results = list()

    #If there are no filters, it should return all the values
    if filter_query == "":
        return list(all_res)
    
    #Split the filter query to create a list where each item is a specific filter
    filter_query = filter_query.split("&")
    dictio = {}

    #For each item is created a sublist with two items (key and value, e.g. [["city"], ["Hawaii"]])
    #Transform the main list in a dictionary
    if len(filter_query) > 1:
        for i in range(len(filter_query)):
            filter_query[i] = filter_query[i].split("=")
        for lst in filter_query:
            key = lst[0]
            dictio[key] = lst[1]
    else:
        filter_query = filter_query[0].split("=")
        key = filter_query[0]
        dictio[key] = filter_query[1]
    
    #Check entry by entry if the keys shared with the dictionary have the same values
    for entry in all_res:
        good = True
        for key, value in dictio.items():
            if entry.get(key) != value:
                good = False
                break
        if good is True:
            results.append(entry)
    return results

#Example of input
filter_query = "type=user&gender=M"
full_json = '''{"result": [{ 	"name": "Robert McNally", "city": "Hawaii", 	"type": "user", "gender": "M"},
{ 	"name": "Elizabeth Minelli", 	"city": "Hawaii", 	"type": "user", "gender": "F"}, 
{ 	"name": "Friendly Neighborhood Coder", 	"city": "Trivandrum", 	"type": "page" },
{ 	"name": "Coddy Official", 	"city": "Haifa", 	"type": "page" }]}'''

print(search(filter_query, full_json)) 
#Should print [{'name': 'Robert McNally', 'city': 'Hawaii', 'type': 'user', 'gender': 'M'}]
#As it's the only entry that meets the filters (type = user, gender = M)