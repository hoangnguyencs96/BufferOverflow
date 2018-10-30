filename = "shellcode.txt"

file = open(filename,"r")

Shell = ""
Shell_length = 0;

for line in file:
	word = line.split(' ')
	for item in word:
		small_word = item.split('\t')
		for s in small_word:
			if len(s.strip()) == 2:
				Shell += "\\x"+s.strip();
				Shell_length +=1

print Shell

print "Shell Length: " + str(Shell_length)
