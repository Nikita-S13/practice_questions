#wap to create a list of names and then remove names that contain 'a' or 'o' char
names=['Divya Srivastava','Shreya Dixit','Sonal Agnihotri','Simaran Mulani','Simmi']
names_without_a_or_o=[name for name in names if('a' not in name.lower() and 'o' not in name.lower())]
print(names_without_a_or_o)
