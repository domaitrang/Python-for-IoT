# Điều khiển luồng trong vòng lặp: break và continue
# break: thoát khỏi vòng lặp hiện tại
# continue: bỏ qua vòng lặp hiện tại
# -> giống c/c++, java, php, javascript....

# VD: Tìm gia trị đầu tiên chia hết cho 3 và 5 trong đoạn [a, b] (a, b dương)

# "3, 4" => "3","4" -> int -> 3 , 4 => a, b 
# a, b = map(int, input("a, b: ").split(","))
# x = -1
# for i in range(a, b+1):
#     if(i % 3 == i % 5 == 0):
#         x = i
#         break

# if(x != -1):
#     print("Giá trị cần tìm là: ", x)
# else:
#     print("Không có giá trị cần tìm")

# Trong trường hợp có nhiều vòng lặp lồng nhau ?
# Loop 1
   # Nested Loop 2
       #break  ???

for i in range(1, 3):
    for j in range(1, 10):
        if(j % 5 == 0):
            break
        print(j, end = "\t")
    print()

#   1 2 3 4 
#   1 2 3 4


for i in range (1, 10):
    if(i == 5):
        continue
    print(i, end = "\t")


