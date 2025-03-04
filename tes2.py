list =	{  "A": "85",  "R": "2.2" }
nested_dict = {'dict1': {"A": "84",  "R": "2.2"},
               'dict2': {"A": "85",  "R": "3.2"},
               'dict3': {"A": "86",  "R": "5.2"},
               'dict4': {"A": "87",  "R": "4.2"}
               }
list = [nested_dict["dict1"], nested_dict["dict2"],nested_dict["dict1"], nested_dict["dict2"]]
#print(nested_dict)
#print(list)
for one in list:
    print(one)
    print('--')
    #print(type(one))
    if one["A"] == "84":
        print("84: ",one["R"])
    if one["A"] == "85":
        print("85: ",one["R"])
    if one["A"] == "86":
        print("86: ",one["R"])