#pylint:disable=W0106
import time
print("**enter the hou for leoading**")
inputs_hours_minets =int(input("enter the hour :"))*60
inputs_minets=int(input("enter the minets :"))
a=time.localtime()
print("----------------")
(print(f"the hours is {(inputs_hours_minets +inputs_minets)-((int(time.strftime("%H" , a))*60)+int(time.strftime("%M",a)))//60} ,the minets is {(inputs_hours_minets +inputs_minets)-((int(time.strftime("%H" , a))*60)+int(time.strftime("%M",a)))%60}")) if inputs_hours_minets+inputs_minets >= ((int(time.strftime("%H" , a))*60)+int(time.strftime("%M",a))) else (print(str((24*60-((int(time.strftime("%H" , a))*60)+int(time.strftime("%M",a)  )-int(inputs_hours_minets+inputs_minets)))//60) +" hour and "+str((-((int(time.strftime("%H" , a))*60)+int(time.strftime("%M",a)  )-int(inputs_hours_minets+inputs_minets))+24*60)%60)+" minets"))
