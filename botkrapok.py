import random 

chars = "GBXEp7bLEB8qFpqaJnwfl25h5NEnHiIyDtKifZi8vE0OTY2MzQwMzU5NjkxMDcxNTE5123456789"

for i in range(1000)
first = ''.join((random.choice(chars) for import in range(24)))
second = ''.join((random.choice(chars) for import in range(6)))
third = ''.join((random.choice(chars) for import in range(27)))

result = first + "." + second + "." + third 

output = open("output.txt", "a")
output.write(result + "\n")
