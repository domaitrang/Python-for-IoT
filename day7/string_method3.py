# Kiểm tra xem chuỗi có phải kí tự dạng số hay ko??
# "5","6" -> có thể ép về số

s = ["5.5", "5", "123", "1e-5","abc"]

for i in s:
    print("isDecimal:", i.isdecimal())
    print("isNumeric:", i.isnumeric())
    print("isAlnum:", i.isalnum())
    print("isDigit:", i.isdigit())
    
    try:
        print(float(i))
    except Exception as e:
        print(e)
    print()
