str="パタトクカシーー"
ansstr=""
n=0
for i in str:
	if n==0:
		ansstr=ansstr + i
		n=1
	else:
		n=0
print(ansstr)