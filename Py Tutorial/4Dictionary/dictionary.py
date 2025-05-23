d={
    'USA': {'zip':123456,'capital': 'Washington DC' },
    "India": {'zip':345678,'capital': 'Delhi'},
    "China": {'zip': 67890, 'capital': 'abcd'}

}
# print(d.get("USA"))
#
# for name,number in d.items() :
#     print(name,number)

for country, details in d.items():
    print(country, details['capital'])




