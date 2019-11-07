# -*- coding: utf-8 -*-

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']]

d = [{attributes[index]:v for index,v in enumerate(value)} for value in values]
print(d)
