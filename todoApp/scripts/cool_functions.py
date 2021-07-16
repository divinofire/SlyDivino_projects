def numerifyKeysOf(dictionary):
	new_dict = {}
	i = 0
	for key in dictionary:
		new_dict.update({i: dictionary[key]})
		i += 1
	return new_dict

def dict_from_list(my_list):
	new_dict = {}
	key = 0
	for item in my_list:
		new_dict.update({key: item})
		key += 1
	return new_dict

def list_from_dict(my_dict):
	new_list = []
	for key in my_dict:
		new_list.append(my_dict[key])

#testing dict_from_list

# my_list = {"take out the trash", "go for shopping", "finish client 40's code"}
# my_dict = dict_from_list(my_list)

# print(my_list)
# print(my_dict)