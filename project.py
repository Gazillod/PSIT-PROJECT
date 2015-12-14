def interface():
    '''this function user must take your _input what do you want to know about grahp of accident'''
    print("THE SITUATION OF TRAFFIC ACCIDENT CAUSE OF THE ACCIDENT BY A PERSON AND ENVIRONMENT \
    CAUSES OF THE EQUIPMENT USED IN DRIVING ,WHOLE KINGDOM: 2006 - 2013")
    print('which graph do you want to see'+'('+'all/conclude/each situation'+')') #ให้ผู้ใช้เลือกกราฟที่ต้องการให้แสดง
    ans = input()
interface()

import csv
from IPython.core.display import HTML
from nvd3 import multiBarChart
chart = multiBarChart(width=1024, height=600, x_axis_format=None) # กว่าง * ยาว  = 1024 พิกเซล * 600 พิกเซล
data = [] # กำหนดให้เก็บข้อมูลเป็นข้อมูลชนิด List
with open('accident_data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
for row in reader:
        data.append(row) # เพิ่มข้อมูลเข้าไปยัง data
del data[0] # ลบส่วนหัวออก
xdata = []
ydata = []
i = 0
while i < len(data):
    xdata.append(data[i][0]) # ชื่อ
    ydata.append(int(data[i][5])) # ข้อมูลจำนวน
    i+=1 # เพื่อค่าอีก 1
chart.add_serie(name="accident", y=ydata, x=xdata)
chart.buildhtml()
HTML(chart.htmlcontent)
