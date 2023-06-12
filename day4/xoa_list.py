# Xoá phần tử thì làm thế nào ??

# Xoá theo giá trị
hoa_qua = ['cam','tao','le','xoai','tao']
print(hoa_qua)
# Chi xoa phan tu dau tien duoc tim thay
hoa_qua.remove('tao')
hoa_qua.remove('tao')
# Nen kiem tra, dam bao phan tu can xoa co trong list
print(hoa_qua)


# Xoa theo chi so index, dung pop
ip_list = ['192.168.1.1','192.168.1.2','192.168.1.3']
print(ip_list)
ip_list.pop(0)
# Mac dinh xoa phan tu cuoi cung
ip_list.pop()
print(ip_list)

# Xoa theo del
pc_list = ["PC1","PC2","PC3"]
print(pc_list)
del pc_list[1]
print(pc_list)
