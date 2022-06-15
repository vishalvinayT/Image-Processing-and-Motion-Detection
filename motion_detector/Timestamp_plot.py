from tkinter import BOTTOM
from turtle import color, left, right
from motion_detector import df
from bokeh.plotting import figure,output_file,show
x=df['Start']
y=df['Stop']
p=figure(x_axis_type='datetime',width=750,height=500)
p.title.text='Time Plot'
p.xaxis.axis_label='Time'
p.yaxis.axis_label='Motion'
p.quad(left=x,right=y,bottom=0,top=1,color='red',)
output_file('Plotting.html')
show(p)