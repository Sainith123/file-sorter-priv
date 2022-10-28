import pyperclip
with open("sort.exe","rb") as o:

    pyperclip.copy(str(o.read()))