import re
p =re.compile('[a-z]+')
m=p.finditer('Life is too short')
print(m)