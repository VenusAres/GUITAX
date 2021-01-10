from tkinter import *
#จาก library tkinter * ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk # ttk is theme of tk
##--google trans
from googletrans import Translator
translator = Translator()
GUI = Tk()# สร้างหน้าต่างหลัก
GUI.geometry('500x300') # กว้างxสูง
GUI.title('CAlCULATE tax by FOLK')
#config--
FONT = ('Angsana New',15)
#label 1
L1=ttk.Label(GUI,text='ชื่อสินค้า',font=FONT,foreground='RED')
L1.pack()
#ช่องกรอก1
productName=StringVar()#เก้บข้อมูล
B1=ttk.Entry(GUI,textvariable=productName,font=FONT)
B1.pack(padx=10,pady=10)
#label 2
L2=ttk.Label(GUI,text='ราคา',font=FONT,foreground='GREEN')
L2.pack()
#ช่องกรอก2
productPrice=StringVar()#เก้บข้อมูล
B2=ttk.Entry(GUI,textvariable=productPrice,font=FONT)
B2.pack(padx=10,pady=10)
#label 3
L3=ttk.Label(GUI,text='จำนวน',font=FONT,foreground='BLUE')
L3.pack()
#ช่องกรอก3
productQuantity=StringVar()#เก้บข้อมูล
B3=ttk.Entry(GUI,textvariable=productQuantity,font=FONT)
B3.pack(padx=10,pady=10)
#label 4
L4=ttk.Label(GUI,text='ผลลัพท์',font=FONT,foreground='PINK')
L4.pack()
#function
def calculateTax(E1,E2,E3,Tax=0.07):
    
    price=int(E2)
    Quantity=int(E3)
    result=price*Quantity*Tax # สูตรคำนวน
    
    resultTax.set('ราคารวมทั้งหมด'+''+str(price*Quantity+result))
    resultproductName.set('ชื่อสินค้า'+' '+E1)
    resultproductPrice.set('ราคา'+' '+ E2)
    resultproductQuantity.set('จำนวน'+' '+E3)
    resultproductTax.set('VAT ราคา %.2f' %(result))
    
#ปุ่มคำนวน
B5=ttk.Button(GUI,text='ปุ่มคำนวน',command=lambda:calculateTax(productName.get(),productPrice.get(),productQuantity.get()))
B5.pack(padx=10,pady=10)
#ผลการคำนวน ชื่อสินค้า
resultproductName=StringVar()
L6=ttk.Label(GUI,textvariable=resultproductName,font=FONT,foreground='RED')
L6.pack()
#ผลการคำนวน ราคา
resultproductPrice=StringVar()
L7=ttk.Label(GUI,textvariable=resultproductPrice,font=FONT,foreground='RED')
L7.pack()
#ผลการคำนวน จำนวน
resultproductQuantity=StringVar()
L8=ttk.Label(GUI,textvariable=resultproductQuantity,font=FONT,foreground='RED')
L8.pack()
#สรุปtax แค่ภาษี
resultproductTax=StringVar()
L5=ttk.Label(GUI,textvariable=resultproductTax,font=FONT,foreground='RED')
L5.pack()
#สรุปtax
resultTax=StringVar()
L9=ttk.Label(GUI,textvariable=resultTax,font=FONT,foreground='RED')
L9.pack()
GUI.mainloop() #โปรแกรมรันตลอดจนกว่าจะติด (อยู่ล่างสุดเสมอ)



