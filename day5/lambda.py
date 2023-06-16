# Hàm ẩn danh - lambda -> thường sử dụng 1 vài lần

# def sum(x, y): return x + y


# print(sum(4, 5))

# Thường kết hợp với map hoặc filter
# VD: có list 3, 4, 5 => muốn tạo list mới: [6, 8, 10]

l1 = [3, 4, 5]
l2 = []
for i in l1:
    l2.append(i*2)
print(l2)

new_l2 = list(map(lambda x: x*2, l1))
print(new_l2)

# VD: [6, 7, 8], mỗi giá trị x trong list -> y = 2x^3 + 3x -1

m_list = [6, 7, 8]
new_list = list(map(lambda x: 2*x**3 + 3*x - 1, m_list))
print(new_list)

# Kết hợp với filter -> lọc
# Có list vừa số vừa chữ -> lọc ra list chỉ chứa chữ  ???
# ['a','bc',1,2,3,[1,2,10],1.5, 2.5,"hello"]

l3 = ['a', 'bc', 1, 2, 3, [1, 2, 10], 1.5, 2.5, "hello"]
l3_new = list(filter(lambda x: isinstance(x,str), l3 ))
print(l3_new)

def ab(a = 1, b = 2):
    return a + b, a - b

print(type(ab(3, 4)))
# Về cơ bản, giống list nhưng ko thay đổi dc giá trị gồm sửa/xoá...
