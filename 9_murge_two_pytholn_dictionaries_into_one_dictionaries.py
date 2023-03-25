# write a python  program  to  murge two python dictionary into one dictionary.
dict1={1:1,2:4}
dict2={3:9,4:16}

# dict3=dict1.copy()


# for key,value in  dict2.items():
#     dict3[key]=value
# print(dict3)

'''
# using unpacking operator

dict3={**dict1,**dict2}
print(dict3)

'''
# using the murge operator
dict3=dict1 | dict2
print(dict3)