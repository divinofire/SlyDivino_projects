def numerifyKeysOf(dictionary):
	new_dict = {}
	i = 0
	for key in dictionary:
		new_dict.update({i: dictionary[key]})
		i += 1
	return new_dict