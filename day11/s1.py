#!/usr/bin/env python
# -*- coding:utf-8 -*-

# s = "i am %s,age %d."% ("staryjie",25)
# print(s)

# s = "i am %(n1)s,age %(n2)d."% {"n1": "staryjie","n2": 25}
# print(s)

# s = "i am %(n1)+10s,age %(n2)+10d."% {"n1": "staryjie","n2": 25}
# print(s)


# s = "i am {:#b} years old.".format(12)
# print(s)

tpl = "i am {}, age {}, {}".format("seven", 25, 'staryjie')
tp2 = "i am {}, age {}, {}".format(*["seven", 25, 'staryjie'])
tp3 = "i am {0}, age {1}, really {0}".format("seven", 25)
tp4 = "i am {0}, age {1}, really {0}".format(*["seven", 25])
tp5 = "i am {name}, age {age}, really {name}".format(name="seven", age=25)
tp6 = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 25})
tp7 = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
tp8 = "i am {:s}, age {:d}, money {:f}".format("seven", 25, 88888.1)
tp9 = "i am {:s}, age {:d}".format(*["seven", 25])
tp10 = "i am {name:s}, age {age:d}".format(name="seven", age=25)
tpl1 = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 25})
tpl2 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
tpl3 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
tpl4 = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
tpl5 = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(15,15,15,15,15.823,2)