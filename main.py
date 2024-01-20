import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from PIL import ImageTk, Image
screen = Tk()
global raw_text
##########################################################################################
screen.title("PHẦN MỀM TÓM TẮT VĂN BẢN (T-A)")
screen.geometry("1000x500")
img_import = (Image.open(r"fira.png"))
resize = img_import.resize((130,130))
img = ImageTk.PhotoImage(resize)

images = Button(screen, text = '',image= img)
images.place(x=10,y=10)
def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

def TvsXL1():
		raw_text =text.get("1.0","end-1c")
		XL(raw_text)
def TvsXL2():
		Tk().withdraw() 
		filename = askopenfilename()
		fullText = []
		raw_text = open(filename, "r").read()
		XL(raw_text)
	# for para in raws_text.paragraphs:
	#  	fullText.append(para.text)
	# for line in fullText:
	#  	rawz_text += line
	# rawz_text = rawz_text.encode('utf8') 
	# raw_text = str(rawz_text)

def XL(raw_text):
	raw_text = raw_text.lower() #Biến đổi hết thành chữ thường
	raw_text = raw_text.replace(',', '')
	# raw_text = raw_text.replace('\n', ' ') #Đổi các ký tự xuống dòng thành chấm câu
	raw_text = raw_text.replace('"', '') #Đổi các ký tự " dòng thành ''
	raw_text = raw_text.strip() #Loại bỏ đi các khoảng trắng thừa
	

	# các từ ko nhẩt thiết phải xuất hiện trong câu
	stopWords = set(stopwords.words("english"))
	#tách các câu thành các từ
	words = word_tokenize(raw_text)

	freqTable = dict()
	for word in words:
	    word = word.lower()
	    #nếu có stopword bỏ qua
	    if word in stopWords:
	        continue
	    if word in freqTable:
	    	#Nếu không có thêm vào từ điển FreTable
	        freqTable[word] += 1
	    else:
	        freqTable[word] = 1
	# gọi lại các câu để sử dụng
	sentences = sent_tokenize(raw_text)
	sentenceValue = dict()
	#Dựa vào dữ liệu ở freqTable tính tổng điểm cho từng câu. Câu nào có nhiều từ lặp lại trong đoạn văn thì sẽ có điểm cao.
	for sentence in sentences:
	    for word, freq in freqTable.items():
	        if word in sentence.lower():
	            if sentence in sentenceValue:
	                sentenceValue[sentence] += freq
	            else:
	                sentenceValue[sentence] = freq
	#Đếm tổng số điểm của các câu
	sumValues = 0
	for sentence in sentenceValue:
	    sumValues += sentenceValue[sentence]

	average = int(sumValues / len(sentenceValue))
	sumary = ''
	# Lấy theo phần đông. Các câu có số điểm cao hơn điểm trung bình x 1.3 sẽ đc giữ lại.
	for sentence in sentences:
	    if (sentence in sentenceValue) and (sentenceValue[sentence]>(1.3 * average)):
	        sumary += " " + sentence
	# sumary = sumary.replace(',', '\n')  


	note = Label(screen, text = "Nhập tên file để lưu:")
	note.place(x = 825, y = 230)
	entry_filename = Entry(width = 16, font = ("Times New Roman",14))
	entry_filename.place(x = 825, y =255)
	def nhap():
		save_file_at_dir(r'D:/data/test',str(entry_filename.get())+".docx",sumary)
		notes = Label(screen, text = ("Save at: D:/data/test/"+str(entry_filename.get())+".docx"))
		notes.place(x=825, y =450)
	btn_note =Button(text = "Lưu File", width = 20, height = 1, command =nhap )
	btn_note.place(x =825 , y = 470 )
##########################################################################################
mon = Label(screen, text = " Môn học: Natural Language Processing".upper(), font = ("Times New Roman", 24))
hs = Label(screen, text = "Người thực hiện: Luyện Xuân Minh Đức", font = ("Times New Roman", 16))
gv = Label(screen, text = "Giáo viên hướng dẫn: Huỳnh Quang Đức", font = ("Times New Roman", 16))
dt = Label(screen, text = "ĐỀ TÀI: TÓM TẮT VĂN BẢN TIẾNG ANH ", font = ("Times New Roman", 20))
mon.place(x =200)
hs.place (x = 360, y = 110)
gv.place(x =360, y =80)
dt.place(x = 300 , y = 40)
text = Text(screen,height=21, width = 100)
text.insert(INSERT, "")
text.insert(END, "")
text.place(x =10, y = 155)
btn = Button(text = "Tìm file cần tóm tắt", width = 20, height = 1, command = TvsXL2)
btn.place(x = 825, y = 155)
btn = Button(text = "Tóm tắt", width = 20, height = 1, command = TvsXL1)
btn.place(x = 825, y = 190)
##########################################################################################
screen.mainloop()