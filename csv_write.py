import csv

users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]

with open('homework.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=users[0], delimiter=';')   
    writer.writeheader()
    writer.writerow(users)


#      import csv

# people = [
# #     {"name": "Tom", "age": 10, "city": "Moscow"},
# #     {"name": "Mark", "age": 5, "city": "Khabarovsk"},
# #     {"name": "Pam", "age": 7, "city": "Sahalin"}
# ]
# with open('people.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=people[0])
#     writer.writeheader()
#     writer.writerows(people)