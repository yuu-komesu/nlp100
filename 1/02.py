import re
str1="パトカー"
str2="タクシー"
split_str2 = re.split('(.)', str2)
split_str2 = split_str2[1::2]
n=0
ansstr=""
for i in str1:
	ansstr += i
	ansstr += split_str2[n]
	n+=1

print(ansstr)