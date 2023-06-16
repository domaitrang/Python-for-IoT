day_so = [1, 4, 10, -4, 7, 8]

print(day_so)
# Sap xep tang dan
day_so.sort()
print(day_so)

# Sap xep giam dan
day_so1 = [1, 4, 10, -4, 7, 8, 20, 0, -5]

day_so1.sort(reverse=True)
print(day_so1)

# Sap xep danh sach lien he 
lien_he = ["Ba","Anh","An","Be"]
lien_he.sort()
print(lien_he)

# Danh sach 
my_list = [1,2,3,6,7,0,-1,4]

# Sap xep danh sach tren -> luu vao 1 list moi
new_list = my_list.copy()
new_list.sort()
print("List ban dau:", my_list )
print("List sau sap xep: ", new_list)