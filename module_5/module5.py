width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))
    
s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
print(s)   # Bob Dilan

s =  "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
print(s)  # 'Bob' Dilan

