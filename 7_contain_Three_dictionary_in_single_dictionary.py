# write a python program to create  three dictionaries,then create one dictionary that will contain the other three dictionaries.
dict1={1:"Rohit",2:"Av",3:"Rana",4:"vivek"}
dict2={5:"kamlesh",6:"Sonu"}
dict3={7:"Utkarsh",8:"Ranjit",9:"Niraj",10:True}

onedict1={"one":dict1,"two":dict2,"three":dict3}
print(type(onedict1))
