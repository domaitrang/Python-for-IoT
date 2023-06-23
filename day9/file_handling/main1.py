path_file = "day9/file_handling/note.txt"
try:
    # Mở file
    f = open(path_file, "r+")
    # Ghi nội dung vào file ??
    # f.write("Hello world\n")
    # f.write("Welcome to Python\n")
    # Đọc nội dung trong file.
    # Một số TH cần kiểm tra file có dc quyền đọc ghi hay ko? readable, writeable?
    # Doc cac dong va luu vao list
    # print(f.readlines())
    # Doc tung dong
    for line in f:
        print(line)

except FileNotFoundError:
    print("File không tồn tại")
except:
    print("Có lỗi xảy ra")
finally:
    f.close()
