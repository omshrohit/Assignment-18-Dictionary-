# write a python program to get the key of lowest value from the dictionary.
sample_dict={
    'C':92,
    "Java":66,
    "Python":85
}
print("-----KEY OF THE SMALLEST VALUE IS------")
for key in sample_dict:
    if sample_dict[key]==min(sample_dict.values()):
        print(key)