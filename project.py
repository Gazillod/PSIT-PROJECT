def interface():
    '''this function user must take your _input what do you want to know about grahp of accident'''
    print("THE SITUATION OF TRAFFIC ACCIDENT CAUSE OF THE ACCIDENT BY A PERSON AND ENVIRONMENT \
    CAUSES OF THE EQUIPMENT USED IN DRIVING ,WHOLE KINGDOM: 2006 - 2013")
    print('which graph do you want to see'+'('+'1 all situation/ 2 conclude/ 3 each situation'+')') #ให้ผู้ใช้เลือกกราฟที่ต้องการให้แสดง
    ans = int(input())
    if ans == 1:
    if ans == 2:
    if ans == 3:
        print('Please select which situation you want to know in this list')
        x = 1
        for i in manage_data():
            print x, i[0]
            x += 1
        num = int(input())
        data = []
        data = [row for row in csv.reader(open("accident_data.csv"))][num:num+1]
        situation = data[0]
    
import csv
from IPython.core.display import HTML
from nvd3 import multiBarChart

chart = multiBarChart(width=1024, height=600, x_axis_format=None) # กว่าง * ยาว  = 1024 พิกเซล * 600 พิกเซล
data = [] # กำหนดให้เก็บข้อมูลเป็นข้อมูลชนิด List

    chart = multiBarChart(width=2040, height=500, x_axis_format=None)    
    for collum_year in range(1,9):
        xdata, ydata = [], []
        for i in manage_data():
            cause = ((i[0])[0:6])
            if cause != ' Cause' and cause != ' Other':
                xdata.append(i[0])
                ydata.append(int(i[collum_year]))
            else:
                pass
        chart.add_serie(name= 'THE SITUATION OF TRAFFIC ACCIDENT IN'+str(2005+collum_year), y=ydata, x=xdata)
chart.add_serie(name="accident", y=ydata, x=xdata)
chart.buildhtml()
HTML(chart.htmlcontent)
