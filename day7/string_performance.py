import time
from io import StringIO

s = "hello world"
tmp1 = ""
# Thời gian bắt đầu
t1 = time.time_ns()
for i in range(0, 10000):
    tmp1 = tmp1 + s
# Thời gian kết thúc
t2 = time.time_ns()
tt1 = t2 - t1
print("Chay het: ", tt1)

# StringBuffer
t3 = time.time_ns()
buff = StringIO("")

for i in range(0, 10000):
    buff.write(s)
tmp2 = buff.getvalue()
t4 = time.time_ns()

tt2 = t4 - t3
print("Chay het: ", tt2)

print(tt1/tt2)

# Ưu tiên sử dụng String buffer khi ứng dụng thao tác với chuỗi