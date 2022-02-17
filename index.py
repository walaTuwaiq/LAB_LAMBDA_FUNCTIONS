
myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filterList = list(filter(lambda name: name.startswith("Kh") or name.startswith("Mo") , myList))
print(filterList)