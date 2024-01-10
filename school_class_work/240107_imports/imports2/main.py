from module_a import ma_1
print(ma_1)    # ma_1 var from module 0a

import module_a
print(dir(module_a))            #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ma_1', 'ma_2']
print(module_a.ma_2)            # ma_2 var from module 0a

# from pack2 import module_2
# print(module_2.m2_1)          # m2_1 var from module 2

# from pack2.module_2 import m2_1
# print(m2_1)                   # m2_1 var from module 2

# import pack2
# print (pack2.module_2.m2_1)     # AttributeError


# from pack1 import p1
# print(p1)                         # p1 var from pack1 __init__

import pack1
print(pack1.p1)                     # p1 var from pack1 __init__
print(pack1.m1_1)                   # m1_1 var from module 1