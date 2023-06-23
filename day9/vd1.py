# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("a/b = ", (a/b))
# except ZeroDivisionError:
#     print("Lỗi chia cho 0")
# except ValueError:
#     print("Nhập sai định dạng")
# except:
#     print("Có lỗi xảy ra!")


# VD1: Nhập a, b, tính đến khi nào, có được 1 kết qủa đầu tiên -> in ra màn hình.
while True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        print("a/b = ", (a/b))
        break
    except ZeroDivisionError:
        print("Lỗi chia cho 0")
    except ValueError:
        print("Nhập sai định dạng")
    except:
        print("Có lỗi xảy ra!")

