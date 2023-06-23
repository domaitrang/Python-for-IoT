class VanBan:
    def __init__(self, duong_dan, noi_dung):
        # f = open(duong_dan, "w+")
        self.__duong_dan = duong_dan
        self.__noi_dung  = list()
        self.__noi_dung.append(noi_dung)
        # Đọc nội dung và lưu vào thuộc tính 

    def chuan_hoa_van_ban(self):
        tmp = list()
        for line in self.__noi_dung:
            # Cat khoang trang dau cuoi.
            line = line.strip()
            # Cat khoang trang/tab o giua
            line = " ".join(line.split())
            # tem vao tmp
            tmp.append(line)
        self.__noi_dung = tmp
    
    def ghi_van_ban(self, noi_dung):
        self.__noi_dung.append(noi_dung)


    def viet_hoa_toan_bo(self):
        for i in range(0, len(self.__noi_dung)):
            self.__noi_dung[i] = self.__noi_dung[i].upper()
        

    def dem_so_tu(self):
        # The nao la 1 tu??  
        # xin chao toi    ten la Nguyen Van A.  
        count = 0
        for line in self.__noi_dung:
            count += len(line.split())
        return count
            

    def luu_van_ban(self):
        # Luu noi dung vao file
        f = open(self.__duong_dan, "w+")
        for line in self.__noi_dung:
            f.write(line+"\n")
        f.close()

    def in_ra_van_ban(self):
        for line in self.__noi_dung:
            print(line)


a = VanBan("/Users/nnt/Desktop/PythonIoT3/day9/file.txt","xin chao toi    ten la Nguyen Van A.  ")
a.ghi_van_ban("Xin chào, tôi là        Python")
a.in_ra_van_ban()
a.chuan_hoa_van_ban()
# a.in_ra_van_ban()
# a.viet_hoa_toan_bo()
# a.in_ra_van_ban()
c = a.dem_so_tu()
print("So tu la: ", c)

a.luu_van_ban()
