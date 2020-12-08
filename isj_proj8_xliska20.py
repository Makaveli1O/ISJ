#!/usr/bin/env python
def first_with_given_key(iterable, key=lambda x:x):
	"""
	Function dirst with given key generates only items in iterable that have unique key
	"""
	#extra array
	keys = [len(iterable)]
	#sort keys
	for item in iterable:
		if key(item) in keys:
			continue
		else:#if correct add key and generate
			keys.append(key(item))
			yield item

if __name__ == "__main__":
    print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))
