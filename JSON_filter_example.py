import json
def search(filter_query, full_json):
    # Write code here
    json_obj = json.loads(full_json)
    all_res = json_obj["result"]
    results = list()
    if filter_query == "":
        return list(all_res)
    filter_query = filter_query.split("&")
    dictio = {}

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
    
    for entry in all_res:
        good = True
        for key, value in dictio.items():
            if entry.get(key) != value:
                good = False
                break
        if good is True:
            results.append(entry)
    return results

filter_query = "type=user&gender=M"
full_json = '{"result": [{ 	"name": "Robert McNally", 	"city": "Hawaii", 	"type": "user", "gender": "M"},{ 	"name": "Elizabeth Minelli", 	"city": "Hawaii", 	"type": "user", "gender": "F"}, { 	"name": "Friendly Neighborhood Coder", 	"city": "Trivandrum", 	"type": "page" },{ 	"name": "Coddy Official", 	"city": "Haifa", 	"type": "page" }]}'
print(search(filter_query, full_json))