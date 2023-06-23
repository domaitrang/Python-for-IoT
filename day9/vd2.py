# Có list gồm 4 phần tử
try:
    m_list = [1,2,3,4]
    print(m_list[0]) #?? -> ném ra exception
except IndexError:
    print("Lỗi chỉ số index")
except:
    print("Có lỗi xảy ra")
finally:
    print("Kết thúc chương trình")

