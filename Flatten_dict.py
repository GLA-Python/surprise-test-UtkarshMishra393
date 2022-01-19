def flatten_dict(a, separator ='.', prefix =''):
    return { prefix + separator +   A if prefix else A : B
             for b, c in a.items()
             for A, B in flatten_dict(c, separator, b).items()
             } if isinstance(a, dict) else { prefix : a }
ini_dict = {'key':3,
            'foo': {'a':5, 'bar':{'baz':8}}}
print ("initial_dictionary", str(ini_dict))
print ("final_dictionary", str(flatten_dict(ini_dict)))
