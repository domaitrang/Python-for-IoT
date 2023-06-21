# Theo huong đối tượng
# Các thuộc tính và các phương thức có liên quan đc đóng gói trong 1 class để tiện
# cho việc quản lý

class hcn():
    def __init__(self, chieu_dai, chieu_rong):
        if(chieu_dai <= 0 or chieu_rong <= 0):
            raise Exception("Kích thước cạnh phải dương")
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def tinh_dien_tich(self):
        return (self.chieu_dai * self.chieu_rong)
    
    def to_string(self):
        return f"hcn[chieu_dai={self.chieu_dai}, chieu_rong={self.chieu_rong}]"


hcn1 = hcn(1, 2)
hcn2 = hcn(3, 4)
print(hcn1.to_string(), "Dien tich:", hcn1.tinh_dien_tich())
print(hcn2.to_string(), "Dien tich:", hcn2.tinh_dien_tich())

# Tao 10 hinh chu nhat, voi canh tu ban phim -> in ra hinh co chu vi lon nhat

hcn_list = list()

for i in range(10):
    c_dai, c_rong = map(float, input("Nhap canh: ").split(","))
    tmp = hcn(c_dai, c_rong)
    hcn_list.append(tmp)

cv_max = 0
hcn_max = None
for item in hcn_list:
    if(item.tinh_chu_vi() > cv_max):
        cv_max = item.tinh_chu_vi()
        hcn_max = item

print("Hinh co chu vi lon nhat la: ")
print(hcn_max.to_string(), "Chu vi:",  cv_max)
