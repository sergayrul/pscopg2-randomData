import psycopg2
import random as rd
from datas import logins, domains, professions, countries, pswd_symbols, streets

#num = rd.randint(0, 10)
#print(num)

password = input("Password for Database: ")
connection = psycopg2.connect(
    database = 'citizens',
    user = 'postgres',
    password = password,
    host = 'localhost',
    port = '5432')

cursor = connection.cursor()

password = []
emails = []
phone_numbers = []
addresses = []
followers = tuple(rd.randint(1,1000000) for i in range(5000))
#print(followers)

for name in logins:
    email = name + str(domains[rd.randint(0, len (domains)-1)])
    emails.append(email)
#print(emails)

for i in range(5000):
    pswrd = ''
    for p in range(rd.randint(8, 15)):
        pswrd += pswd_symbols[rd.randint(0, len (pswd_symbols)-1)]
    password.append(pswrd)

# print(password)

codes = ('75','55','77','70','50','99')

for i in range(5000):
    number = '+996' + codes[rd.randint(0, len(codes)-1)] + str(rd.randint(0, 9)) + str(rd.randint(111111, 999999))
    phone_numbers.append(number)
#print(phone_numbers)

for i in range(5000):
    address = streets[rd.randint(0, len (streets)-1)] + " " + str(rd.randint(0, 500))
    addresses.append(address)

# print(address)
# print(len(addresses))

cursor.execute("""create table users (user_id serial primary key, login varchar(20) not null, password varchar(100) not null, email varchar(100) not null, phone_number varchar(20) not null, country varchar(50) not null, address varchar(50) not null, profession varchar(50) not null, followers int not null)""")

query = '''insert into users (login, password, email, phone_number, country, address, profession, followers) values'''

for _ in range(10000):
    query += f"""(
        '{logins[rd.randint(0, len(logins)-1)]}',
        '{password[rd.randint(0, len(password)-1)]}',
        '{emails[rd.randint(0, len(emails)-1)]}',
        '{phone_numbers[rd.randint(0, len(phone_numbers)-1)]}',
        '{countries[rd.randint(0, len(countries)-1)]}',
        '{addresses[rd.randint(0, len(addresses)-1)]}',
        '{professions[rd.randint(0, len(professions)-1)]}',
        '{followers[rd.randint(0, len(followers)-1)]}'
    ),"""

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
connection.commit()

cursor.close()
connection.close()