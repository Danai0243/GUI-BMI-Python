from tkinter import *

root = Tk()
root.title('โปรแกรมคำนวณ BMI')
root.option_add("*Font", "consolas 20")
tv_bmi = StringVar()
Label(root, text="weight (kg.)").grid(row=0, column=0, sticky="s", padx=10)
Label(root, text="height (cm.)").grid(row=1, column=0, sticky="s", padx=10)
lbl_bmi = Label(root, textvariable=tv_bmi)
lbl_bmi.grid(row=3, columnspan=2, sticky="news")
data = Label(root, text="")
data.grid(row=4, columnspan=2, sticky="news")

# ใน on_drag จะประกอบไปด้วย การรับค่า w และค่า h ที่เราได้จากเลื่อน Scale โดยใช้ w.get() และ h.get() มาคำนวณโดยใช้สูตร
# น้ำหนัก (กิโลกรัม) / [ส่วนสูง (เมตร)]² w / (h/100)² แล้วเราก็จะได้ค่าBMIออกมา


def on_drag(e):
    bmi = w.get() / (h.get() / 100) ** 2
    tv_bmi.set(f'BMI = {bmi:.2f}')
    color_zone = ""
    if bmi > 30:
        color_zone = "red"
        data["text"] = "โรคอ้วนอันตราย"
    elif bmi >= 25:
        color_zone = "orange"
        data["text"] = "โรคอ้วน"
    elif bmi >= 23:
        color_zone = "yellow"
        data["text"] = "อ้วน"
    elif bmi >= 18.5:
        color_zone = "green"
        data["text"] = "สมส่วน"
    else:
        color_zone = "red"
        data["text"] = "น้ำหนักต่ำกว่าเกณฑ์"
    lbl_bmi["bg"] = color_zone


# น้ำหนัก
w = Scale(root, from_=1, to=150, orient=HORIZONTAL, length=200, width=30)
w.set(75)
w.grid(row=0, column=1)
w.bind('<B1-Motion>', on_drag)
w.bind('<Button-1>', on_drag)

# ส่วนสูง
h = Scale(root, from_=1, to=250, orient=HORIZONTAL, length=200, width=30)
h.set(125)
h.grid(row=1, column=1)
h.bind('<B1-Motion>', on_drag)
h.bind('<Button-1>', on_drag)


root.mainloop()
