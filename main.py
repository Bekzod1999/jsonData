# I have imorted everything which I need
import requests
import json
# I created new list and dictionary for writing in the data.json file
allResults = []
dictionary1 = {}
# I took all of username this link
url = 'https://randomuser.me/api'
# I got the data of 20 useres
for i in range(20):
    response = requests.get(url)
    jsonFile = response.json()
    allResults.append(jsonFile)
# I have written data of 20 users in the data.json file
dictionary1['result'] = allResults
jsonObject = json.dumps(dictionary1)
file = open('data.json', 'w')
file.write(jsonObject)
# I read data in the data.json file
json_data = open("data.json", 'r', encoding='utf-8')
data = json.load(json_data)
#  I began to do tasks
gender = []
f_name = []
l_name = []
location = []
ages = []
# I took key of data
data = data["result"]
k = len(data)
print(type(data))

# I collected everything data which I need
for i in range(k):
    gender.append(data[i]["results"][0]["gender"])
    f_name.append(data[i]["results"][0]["name"]["first"])
    l_name.append(data[i]["results"][0]["name"]["last"])
    location.append(data[i]["results"][0]["location"]["country"])
    ages.append(data[i]["results"][0]["dob"]["age"])

results_m = []
results_f = []

for i in range(k):
    result_m = {}
    result_f = {}
# I separated male data and female data then gathered all of data two lists
# First list(results_m) for male data, second list(results_f) for female data
    if gender[i] == "male":
        result_m["gender"] = gender[i]
        result_m["first"] = f_name[i]
        result_m["last"] = l_name[i]
        result_m["age"] = ages[i]
        result_m["country"] = location[i]
        results_m.append(result_m)
    else:
        result_f["gender"] = gender[i]
        result_f["first"] = f_name[i]
        result_f["last"] = l_name[i]
        result_f["age"] = ages[i]
        result_f["country"] = location[i]
        results_f.append(result_f)

# I created new two dictionaries
total_result_m = {}
total_result_f = {}
# I have provided their values
total_result_m["result"] = results_m
total_result_f["result"] = results_f

# I have written data of men in male.json file
jsonMaleObject = json.dumps(total_result_m)
jsonMale = open('male.json', 'w')
writeJsonForMale = jsonMale.write(jsonMaleObject)

# I have written data of women in female.json
jsonFemaleObject = json.dumps(total_result_f)
jsonFemale = open('female.json', 'w')
writeJsonForFemale = jsonFemale.write(jsonFemaleObject)