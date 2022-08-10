import re

data = """
park 800905-1049118
"""

pat = re.compile("(\d{6}[-]\d{7}")
print(pat.sub("\g<1>-*******",data))
