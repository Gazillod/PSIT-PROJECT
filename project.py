import csv
from IPython.core.display import HTML
from nvd3 import multiBarChart

"""The graph of THE SITUATION OF TRAFFIC ACCIDENT CAUSE OF THE ACCIDENT BY A PERSON AND ENVIRONMENT \
    CAUSES OF THE EQUIPMENT USED IN DRIVING ,WHOLE KINGDOM: 2006 - 2013 Program"""

def manage_data():
    """This function will take the data from csv file to data list"""
    data = []
    data = [row for row in csv.reader(open("accident_data.csv"))][1:]
    return data

def build_all_graph():
    """This function build the chart template and set the histogram graph with data
    then show about the situation of traffic accident in 2006-2013 and every cause"""
    chart = multiBarChart(width = 2040, height = 500, x_axis_format = None)    
    for collum_year in range(1, 9):
        xdata, ydata = [], []
        for i in manage_data():
            cause = ((i[0])[0:6])
            if cause != ' Cause' and cause != ' Other':
                xdata.append(i[0])
                ydata.append(int(i[collum_year]))
            else:
                pass
        chart.add_serie(name = 'THE SITUATION OF TRAFFIC ACCIDENT IN (case)' + str(2005 + collum_year), y = ydata, x = xdata)
    return chart

def build_conclude_graph():
    """This function build the chart template and set the histogram graph with data
    then show about the main cause of situation in 2006-2013 """
    chart = multiBarChart(width = 2040, height = 500, x_axis_format = None)    
    for collum_year in range(1, 9):
        xdata, ydata = [], []
        for i in manage_data():
            cause = ((i[0])[0:6])
            if cause == ' Cause' or cause == ' Other':
                xdata.append(i[0])
                ydata.append(int(i[collum_year]))
            else:
                pass
        chart.add_serie(name = 'THE SITUATION OF TRAFFIC ACCIDENT IN (case)' + str(2005 + collum_year), y = ydata, x = xdata)
    return chart

def build_each_graph(situation):
    """This function build the chart template and set the histogram graph with data
    then show about a cause of the accident that user want to know"""

    chart = multiBarChart(width = 2040, height = 500, x_axis_format = None)    
    for collum_year in range(1, 9):
        xdata, ydata = [], []
        for i in manage_data():
            cause = ((i[0])[0:len(situation[0])])
            if cause == situation[0]:
                xdata.append(i[0])
                ydata.append(int(i[collum_year]))
            else:
                pass
        chart.add_serie(name = 'THE SITUATION OF TRAFFIC ACCIDENT IN (Case)' + str(2005+collum_year), y = ydata, x = xdata)
    return chart

def interface():
    '''this function user must take your _input what do you want to know about grahp of accident'''
    print("THE SITUATION OF TRAFFIC ACCIDENT CAUSE OF THE ACCIDENT BY A PERSON AND ENVIRONMENT \
    CAUSES OF THE EQUIPMENT USED IN DRIVING ,WHOLE KINGDOM: 2006 - 2013")
    print('Which graph do you want to see'+'('+'1 all situation/ 2 conclude/ 3 each situation'+')') #ให้ผู้ใช้เลือกกราฟที่ต้องการให้แสดง
    ans = int(input())
    if ans == 1:
        return build_all_graph()
    if ans == 2:
        return build_conclude_graph()
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
        return build_each_graph(situation)

def build_graph(chart):
    """This function will get return of chart and convert to graph"""
    chart.buildhtml()
    HTML(chart.htmlcontent)
    return HTML(chart.htmlcontent)
build_graph(interface())
