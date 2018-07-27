#!/usr/bin/python
#-*- coding: utf-8 -*-

def prettyFloats(obj, precision=4):
    if isinstance(obj, float):
        return round(obj, precision)
    elif isinstance(obj, dict):
        return dict((k, prettyFloats(v, precision)) for k, v in obj.iteritems())
    elif isinstance(obj, list):
        # return map(prettyFloats, obj, [precision]*len(obj))
        return [prettyFloats(item, precision) for item in obj]
    elif isinstance(obj, tuple):
        # return tuple(map(prettyFloats, obj, [precision]*len(obj)))
        return tuple([prettyFloats(item, precision) for item in obj])
    return obj

if __name__ == '__main__':
    a = [0.33333333333333333333, 0.9999999999999, 0.1]
    b = { 'a': 0.333333333, 'b': 0.445444444, 'c': 0.293 }
    c = ({'a': 0.333333333, 'b': 0.445444444, 'c': 0.293}, {'a': 0.333333333, 'b': 0.445444444, 'c': 0.1})
    a2 = prettyFloats(a,5)
    b2 = prettyFloats(b)
    c2 = prettyFloats(c,2)
    print a2
    print b2
    print c2
    import json
    print json.dumps(a2)
    print json.dumps(b2)
    print json.dumps(c2)
