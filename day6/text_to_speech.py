from gtts import gTTS
import os
import platform
tts = gTTS("Xin chào các thầy cô", lang="vi",slow=True)
tts.save("day6/out.mp3")

# Sau khi lưu xong có thể play luôn mp3
# Có thể viết code để chạy cho các hệ điều hành khác nhau
my_os = platform.system()
if(my_os == "Windows"):
    # play mp3
    pass
elif(my_os == "Darwin"):
    os.system("afplay " + "day6/out.mp3")
