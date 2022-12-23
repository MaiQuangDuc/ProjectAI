import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from playsound import playsound
import tensorflow as tf
import numpy as np
from tensorflow import keras
from winsound import *
from tensorflow.keras.utils import load_img, img_to_array



#Load Model
new_model = tf.keras.models.load_model("C:\\Users\\maiqu\\OneDrive\\Desktop\\NhacCu.h5")

#Def GIAO DIEN
wd = Tk()
wd.title('VietNam Traditional Musical Instrument Recognition')
wd.geometry('650x433')
load = Image.open("C:\\Users\\maiqu\\OneDrive\\Desktop\\v1059-041c.jpg")
render = ImageTk.PhotoImage(load)
img = Label(wd, image=render)
img.place(x=0,y=0)
wd.resizable(width=False, height=False)


Label1=tk.Label(wd)
Label1['font'] = ("Time New Roman", 20)
Label1['bg'] = 'lavender'
Label1["justify"] = "center"
Label1["text"] = " NHẠC CỤ DÂN TỘC VIỆT NAM "
Label1.place(x=0,y=0,width=650,height=50)

frame = Frame(wd)
frame['bg'] = 'Black'
frame['bd'] = 5
frame.place(x=60, y =60, width = 200, height = 200)

#Def button import image
def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()
    

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 200 # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel_image = tk.Label(frame, image=img).pack()

    
#Def CLASSIFY ( nhận diện )

def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    result = new_model.predict(image_batch)
    global prediction, thongtinhaccu, loainhaccu 
    if round(result[0][0]) == 1:
        prediction = 'Cồng Chiêng'
    if round(result[0][1]) == 1:
        prediction = 'Đàn Bầu'
    if round(result[0][2]) == 1:
        prediction = 'Đàn Nhị'
    if round(result[0][3]) == 1:
        prediction = 'Đàn Tranh'
    if round(result[0][4]) == 1:
        prediction = 'Sáo Trúc' 
    if round(result[0][5]) == 1:
        prediction = 'T.Rưng'

    print("Đây là :", str(prediction).upper())
    
    d = {"Cồng Chiêng":"Cồng chiêng là nhạc cụ Châu Á thuộc bộ gõ, được làm bằng đồng thau, hình tròn như chiếc nón quai thao,đường kính khoảng từ 20 cm đến 60 cm, ở giữa có hoặc không có núm. Người ta dùng dùi gỗ có quấn vải mềm (hoặc dùng tay) để đánh cồng, chiêng. Cồng, chiêng càng to thì tiếng càng trầm, càng nhỏ thì tiếng càng cao. ",
    'Đàn Bầu':"Là một loại nhạc cụ truyền thống của người Việt, thanh âm phát ra nhờ sử dụng que hay miếng gảy vào dây. Dựa theo cấu tạo của hộp cộng hưởng, đàn bầu chia hai loại là đàn thân tre và đàn hộp gỗ.. Đàn bầu có mặt phổ biến ở các dàn nhạc cổ truyền dân tộc Việt Nam. Các nhạc sĩ Việt Nam đã biên soạn và chuyển soạn một số tác phẩm dạng concerto để nghệ sĩ sử dụng đàn bầu trình tấu cùng với dàn nhạc giao hưởng thính phòng như Vì Miền Nam, Ru con, Tình ca... ",
    "Đàn Nhị":"Là nhạc cụ thuộc bộ dây có cung vĩ, do đàn có 2 dây nên gọi là đàn nhị. uy phổ biến tên gọi 'đàn nhị', nhiều dân tộc tại Việt Nam còn gọi đàn bằng tên khác nhau. Người Kinh gọi là líu hay nhị líu (để phân biệt với 'nhị chính'), người Mường gọi là 'Cò ke', người miền Nam gọi là Đờn cò. Hình dáng, kích cỡ và nguyên liệu làm đàn nhị cũng khác nhau đôi chút tùy theo tộc người sử dụng nó",
    "Đàn Tranh":"còn được gọi là đàn thập lục hay đàn có trụ chắn, là nhạc cụ truyền thống của người phương Đông, có xuất xứ từ Trung Quốc. Đàn thuộc họ dây, chi gảy; ngoài ra họ đàn tranh có cả chi kéo và chi gõ. Loại 16 dây nên đàn còn có tên gọi là đàn Thập lục. Nay đã được tân tiến thành 21 - 25, 26 dây",
    "Sáo Trúc":"Nhìn chung sáo ngang thường làm bằng ống trúc, ống nứa hoặc ống rùng, thỉnh thoảng người ta tạo ra loại sáo bằng kim loại hoặc bằng gỗ đều sử dụng tốt. Về cơ bản, sáo ngang có 1 lỗ thổi nằm cùng hàng với 6 lỗ bấm. Mỗi loại sáo có tông riêng nên người diễn thường chọn loại sáo làm sao để phù hợp với bài bản. Một số sáo cải tiến được khoét thêm một số lỗ bấm phụ trên thân sáo, giúp việc diễn tấu các nốt thăng/giáng dễ dàng",
    'T.Rưng':"là loại nhạc cụ gõ phổ biến ở vùng Tây Nguyên, Việt Nam, đặc biệt là đối với dân tộc Gia Rai và Ba Na. Cái tên 't'rưng' xuất phát từ tiếng Gia Rai, lâu ngày trở nên quen thuộc với mọi người. Đàn t'rưng làm bằng một số ống tre lồ ô hay nứa ngộ có kích cỡ khác nhau. Đàn t'rưng chuyên nghiệp có khoảng 12 đến 16 ống xếp thành hàng trên giá đàn theo thứ tự đi dần lên từ ống lớn đến ống nhỏ, từ ống dài đến ống ngắn"}

    thongtinhaccu = tk.Message(wd, width= 330, bg= 'azure', justify= 'center', text= str(d[prediction]).upper(),relief=RAISED)
    thongtinhaccu.place(x = 280, y = 130)
    
    loainhaccu = tk.Label(wd, text = str(prediction).upper(), bg = '#F0F0F0',fg = 'sienna', font= ("", 24))
    loainhaccu.place(x= 380, y = 70)
    
def close() : 
    thongtinhaccu.destroy()
    loainhaccu.destroy()

def play(): 
    if prediction == 'Cồng Chiêng':
        playsound('C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\Cồng Chiêng.mp3')
    if prediction == 'Đàn Bầu':
        playsound('C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\Đàn bầu.mp3')
    if prediction == 'Đàn Nhị':
        playsound('C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\Đàn nhị.mp3')
    if prediction == 'Đàn Tranh':
        playsound('C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\Đàn tranh.mp3')
    if prediction == 'Sáo Trúc':
        playsound("C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\Sáo Trúc.mp3")
    if prediction == 'T.Rưng':
        playsound("C:\\Users\\maiqu\\OneDrive\\Desktop\\Sound\\T'Rưng.mp3")



#INFORMATION:
Label2=tk.Label(wd)
Label2['font'] = ("Time New Roman", 14)
Label2["fg"] = "black"
Label2["justify"] = "right"
Label2["text"] = "ĐÂY LÀ :"
Label2.place(x=280,y=80,width=100,height=25)


#Def button
Button_1=tk.Button(wd)
Button_1["bg"] = "cornsilk"
Button_1['font'] = ("Time New Roman", 10)
Button_1["fg"] = "#ff1944"
Button_1["justify"] = "center"
Button_1["text"] = "THÊM ẢNH"
Button_1.place(x=80,y=280,width=118,height=30)
Button_1["command"] = load_img 


#Button classify
Button_2=tk.Button(wd)
Button_2["bg"] = "cyan"
Button_1['font'] = ("Time New Roman", 10)
Button_2["fg"] = "#000000"
Button_2["justify"] = "center"
Button_2["text"] = "NHẬN DIỆN"
Button_2.place(x=80,y=320,width=116,height=30)
Button_2["command"] = classify


#Def button play
Button_2=tk.Button(wd)
Button_2["bg"] = "cornsilk"
Button_2['font'] = ("Time New Roman", 10)
Button_2["fg"] = "#ff1944"
Button_2["justify"] = "center"
Button_2["text"] = "NGHE NHẠC"
Button_2.place(x=80,y=360,width=118,height=30)
Button_2["command"] = play
    

#Def button close
Button_2=tk.Button(wd)
Button_2["bg"] = "cyan"
Button_2['font'] = ("Time New Roman", 10)
Button_2["fg"] = "#000000"
Button_2["justify"] = "center"
Button_2["text"] = "LÀM MỚI"
Button_2.place(x=80,y=400,width=118,height=30)
Button_2["command"] = close

wd.mainloop()