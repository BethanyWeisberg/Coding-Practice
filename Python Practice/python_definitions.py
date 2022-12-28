python_definitions = {
    'tuple': 'collection of ordered and unchangeable items',
    'dictionary': 'collection of key-value pairs',
    'list': 'used to store multiple items in a single variable',
    'variable': 'symbolic reference of an object',
    'if statement': 'conditional execution',
}

for key,value in python_definitions.items():
    if key == 'list':
        print(f'A {key} is {value}.')
    else:
        print(f'A {key} is a {value}.')
 
python_definitions['for loop'] = 'used for iterating over a sequence'
python_definitions['set'] = 'used to store unique items in a single variable'
python_definitions['items()'] = 'used to return a list of key-value pairs'
python_definitions['f string'] = 'literal string which contains expressions inside braces that are replaced by values in the output'
python_definitions['nesting'] = 'a list or dictionary that contains additional list or dictionary'

for name in python_definitions.keys():
    print(name)
