from math import pi


class hinh_tron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def chu_vi(self):
        return self.ban_kinh * 2 * pi

    def dien_tich(self):
        return self.ban_kinh ** 2 * pi


class hinh_tru(hinh_tron):
    def __init__(self,chieu_cao, ban_kinh):
        super().__init__(ban_kinh)
        self.chieu_cao = chieu_cao
    
    def the_tich(self):
        return super().dien_tich() * self.chieu_cao

ht1 = hinh_tru(2, 1)
print("The tich hinh tru: ", ht1.the_tich())

ht1.dien_tich() # -> sai về bản chất -> thực tế là tính cho đáy
ht1.chu_vi() # -> ko hợp lý -> mặc dù vẫn chạy