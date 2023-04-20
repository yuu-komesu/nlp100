text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans=map()
replaced_text = text.replace('.', '')
split_str = replaced_text.split()
n=[1, 5, 6, 7, 8, 9, 15, 16, 19]
i=1
for word in split_str:
    if i in n:
        word