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
