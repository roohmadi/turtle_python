list =	{  "A": "85",  "R": "2.2" }
nested_dict = {'dict1': {"A": "85",  "R": "2.2"},
               'dict2': {"A": "84",  "R": "3.2"}}
list = [nested_dict["dict1"], nested_dict["dict2"]]
#print(nested_dict)
#print(list)
for one in list:
    print(one)
    print('--')
    #print(type(one))
    if one["A"] == "85":
        print(one["R"])