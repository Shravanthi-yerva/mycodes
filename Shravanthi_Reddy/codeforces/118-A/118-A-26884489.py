s=input()
s=s.lower()
vowel ="aeiouy"
temp=""
for i in s:
	if i not in vowel:
		temp = temp + "." + i

print(temp)