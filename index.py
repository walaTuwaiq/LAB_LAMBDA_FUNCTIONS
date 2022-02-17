
myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filterList = list(filter(lambda name: (name[0]=="K" and name[1] == "h") or (name[0] =="M" and name[1] == "o") , myList))
print(filterList)