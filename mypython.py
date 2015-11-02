import random
from datetime import datetime

random.seed(datetime.now);

rand = ["0", "0", "0", "0"]
for i in range(1, 4):
	string = ""
	for j in range(0, 10):
		string += chr(random.randint(97, 122))
	rand[i] = string;

for i in range(1, 4):
	file1 = open("rand%d" % i, "w")
	file1.write(rand[i]);
	file1.close();

for i in range(1, 4):
	print rand[i]

int1 = random.randint(1, 42)
int2 = random.randint(1, 42)
print int1
print int2
print int1 + int2
