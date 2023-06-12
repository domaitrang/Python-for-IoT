# Duyet danh sach

# Nhap 1 list tu ban phim
# "3,4,5" => "3","4","5" => 3, 4, 5 => [3, 4, 5]
m_list = list(map(int, input("Nhap day:").split(",")))

# In ra cac phan tu trong list do, cach nhau 1 tab
# Giong kieu for-each
for i in m_list:
    print(i, end ='\t')
print()

# Theo chi so
# for(int j = 0, j < len(m_list); j++) {....}

for j in range(0, len(m_list)):
    print(m_list[j], end="\t")
print()

# In ra tong cac so le trong list
