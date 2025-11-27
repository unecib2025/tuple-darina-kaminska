#1

hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")

counter = 0

for i in hashes:
    if i == "ffd222":
        counter+=1

print(f'Количество вхождений: {counter}')


#2

users = ("guest", "moderator", "admin", "root")

print(f'Индекс admin: {users.index('admin')}')


#3

key_params = ("AES", 256, "CBC")

algorithm, key_size, mode = key_params

print(f'Algorithm:{algorithm}\n Key size:{key_size}\n Mode:{mode}')


#4

log = ("login", "download", "upload", "logout")
print(log[-1])


#5

ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")

user_input = input()

if user_input in ips:
    print(f'Найдено: {ips.index(user_input)}')
else:
    print('Не найдено')


#6
name, role, status = input(), input(), input()

data = name, role, status


#7
access = ("read", "write", "execute")

new_value = input()
new_access = (access[0], new_value, access[2])

print(new_access)

#8

attempts = ("success", "fail", "fail", "success", "fail", "fail")

print(f'Количество успешных входов: {attempts.count('success')}\n Количество неуспешных входов: {attempts.count('fail')}')


#9

admins = ("root", "admin")
users = ("alex", "bob")

new_tuple = admins[0],admins[1],users[0],users[1]
print(new_tuple)

#10

logs = ("login", "upload", "download", "logout")

start, *middle, end = logs

print(f'Start: {start} \nMiddle: {middle} \nEnd: {end}')