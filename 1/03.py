text ="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans=list()
replaced_text = text.replace(',', '')
replaced_text = replaced_text.replace('.', '')
split_str = replaced_text.split()
print(type(split_str))
ans= [len(i) for i in split_str]
print(ans)


