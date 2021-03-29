from datetime import datetime, time, timedelta

import sys, os

# print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
# print('path =', pathname)
# print('full path =', os.path.abspath(pathname)) 



def workedHours(matrixHours):
    
    names=[i[0] for i in matrixHours]
    # print('here print names', names)
    hours=[i[1:] for i in matrixHours]
    # print('Here print hours', hours)


    splitedHours = list()
    for x in range(len(hours)):
        sep=hours[x][0].split(',')
        splitedHours.append(sep)

    # print(splitedHours) 
    
    days1 = ["MO","TU", "WE", "TH", "FR"]
    days2 = ["SA", "SU"]

    # print(len(splitedHours))

    workingDayEachPerson=[]
    workingWeekendEachPerson=[]

    for j in range(len(splitedHours)):
        workingDay=[]
        weekend=[]
        for k in range(len(splitedHours[j])):
            
            for dia in days1:
                if splitedHours[j][k].startswith(dia):
                    if """\n""" in splitedHours[j][k]:
                        workingDay.append(splitedHours[j][k][2:-1])
                    else:
                        workingDay.append(splitedHours[j][k][2:])
                    
            
            for dia in days2:
                if splitedHours[j][k].startswith(dia):
                    if """\n""" in splitedHours[j][k]:
                        weekend.append(splitedHours[j][k][2:-1])
                    else:
                        weekend.append(splitedHours[j][k][2:])
    
        workingDayEachPerson.append(workingDay)
        workingWeekendEachPerson.append(weekend)

    # print('Here is the splited days')
    # print(workingDayEachPerson)
    # print(workingWeekendEachPerson)

    splitedPersonWeek=[]
    for i in range(len(workingDayEachPerson)):
        splited=[]
        for j in range(len(workingDayEachPerson[i])):
            splited.append(workingDayEachPerson[i][j].split('-'))

        splitedPersonWeek.append(splited)

    splitedPersonWeekend=[]
    for i in range(len(workingWeekendEachPerson)):
        splited=[]
        for j in range(len(workingWeekendEachPerson[i])):
            splited.append(workingWeekendEachPerson[i][j].split('-'))

        splitedPersonWeekend.append(splited)
    

    # print('Aqui imprime horas separadas week',splitedPersonWeek)
    # print('Aqui imprime horas separadas weekend',splitedPersonWeekend)
    
    
    return splitedPersonWeek, splitedPersonWeekend, names


def paymentHourWeek(matrizWeek,weekOrWeekend):
    format_hora='%H:%M'
    lim1='00:00'
    lim2='09:00'
    lim3='18:00'
    
    hour1=datetime.strptime(matrizWeek[0], format_hora)
    hour2=datetime.strptime(matrizWeek[1], format_hora)

    lim1_c=datetime.strptime(lim1,format_hora)
    lim2_c=datetime.strptime(lim2,format_hora)
    lim3_c=datetime.strptime(lim3,format_hora)



    if hour1>=datetime.strptime(lim1,format_hora) and hour2<datetime.strptime(lim2,format_hora)  and hour2<=datetime.strptime(lim2,format_hora) and hour2!=lim1_c:
            
            # print("cumple caso 1.1")
            substract=hour2-hour1   
            value=substract.total_seconds()/3600

            if weekOrWeekend=='week':
                paymentValue=value*25
                # print(value)
            else :
                paymentValue=value*30
                # print(value)

            
            
             
    elif hour1>=datetime.strptime(lim1,format_hora) and hour1<datetime.strptime(lim2,format_hora)  and hour2<=datetime.strptime(lim3,format_hora) and hour2!=lim1_c:
        # print("cumple caso 1.2")
        substract1=lim2_c-hour1  
        value1=substract1.total_seconds()/3600
        # print(value1)
        substract2=hour2-lim2_c
        # print(substract2)
        value2=substract2.total_seconds()/3600
        # print(value2)
        if weekOrWeekend=='week':
            paymentValue=value1*25+value2*15
        else:
            paymentValue=value1*30+value2*20
        # print(value1+value2)

        


    elif hour1>=datetime.strptime(lim1,format_hora) and hour1<datetime.strptime(lim2,format_hora) and hour2>=datetime.strptime(lim3,format_hora) and hour2!=lim1_c:
        # print("cumple caso 1.3") 

        substract1=lim2_c-hour1   
        value1=substract1.total_seconds()/3600
        substract2=hour2-lim3_c
        value2=substract2.total_seconds()/3600
        # print(value1+value2+9)

        if weekOrWeekend=='week':
            paymentValue=value1*25+value2*20+8*15
        else:
            paymentValue=value1*30+value2*25+8*20


        

    elif hour1>=datetime.strptime(lim1,format_hora) and hour1<datetime.strptime(lim2,format_hora) and hour2==lim1_c:
        # print("cumple caso 1.4") 
        substract=lim2_c-hour1
        value=substract.total_seconds()/3600
        # print(value+9+6)
        
        if weekOrWeekend=='week':
            paymentValue=value*25+9*15+6*20
        else:
            paymentValue=value*30+9*20+6*25
        
    
    
    
    elif hour1>=datetime.strptime(lim2,format_hora) and hour1<datetime.strptime(lim3,format_hora) and hour2<=datetime.strptime(lim3,format_hora) and hour2!=lim1_c:
        # print("cumple caso 2.1")
        substract=hour2-hour1  
        value=substract.total_seconds()/3600
        # print(value)

        if weekOrWeekend=='week':
            paymentValue=value*15
        else:
            paymentValue=value*20
        


    elif hour1>=datetime.strptime(lim2,format_hora) and hour1<datetime.strptime(lim3,format_hora) and hour2>=datetime.strptime(lim3,format_hora) and hour2!=lim1_c:
        # print("cumple caso 2.2") 

        substract1=lim3_c-hour1 
        value1=substract1.total_seconds()/3600
        substract2=hour2-lim3_c
        value2=substract2.total_seconds()/3600
        # print(value1+value2)
        if weekOrWeekend=='week':
            paymentValue=value1*15+value2*20
        else:
            paymentValue=value1*20+value2*25

        


    elif hour1>=datetime.strptime(lim2,format_hora) and hour1<datetime.strptime(lim3,format_hora) and  hour2==lim1_c:
        # print("cumple caso 2.3") 
        substract=lim3_c-hour1
        value=substract.total_seconds()/3600
        # print(value+6)

        if weekOrWeekend=='week':
            paymentValue=value*15+6*20
        else:
            paymentValue=value*20+6*25
        
        

    elif hour1>=datetime.strptime(lim3,format_hora) and hour2!=lim1_c:
        # print("cumple caso 3.1") 
        substract=hour2-hour1
        value=substract.total_seconds()/3600
        # print(value)
        if weekOrWeekend=='week':
            paymentValue=value*20
        else:
            paymentValue=value*25
        
    
    elif hour1>=datetime.strptime(lim3,format_hora) and  hour2==lim1_c:
        # print('Cumple caos 3.2')
        substract=hour1-lim3_c
        value=6-substract.total_seconds()/3600
        # print(value)
        if weekOrWeekend=='week':
            paymentValue=value*20
        else:
            paymentValue=value*25
        

    else:
        print('Didnt met any condition ')

    # print('Aqui imprime cuanto va a pagar',paymentValue)
    return paymentValue


def main():
   
    data1 = []
    fullpath=pathname+"/datos.txt"
    print(fullpath)
    with open(fullpath) as fname:
        for lines in fname:
            data1.append(lines.split("="))
    # print (data1)
    
    hoursWeek, hoursWeekend, namePerson=workedHours(data1)
    
   
    paymentMatrix=[]

    for i in range(len(hoursWeek)):
        pay1=0
        pay2=0
        for j in range(len(hoursWeek[i])):
            pay1+=paymentHourWeek(hoursWeek[i][j],'week')

        for k in range(len(hoursWeekend[i])):
            pay2+=paymentHourWeek(hoursWeekend[i][k],'weekend')

            
        paymentMatrix.append(pay1+pay2)
        pay1=0
        pay2=0
    
    # print('Payment Matrix',paymentMatrix)

    

    for x in range(len(namePerson)):
        print('The amount to pay',namePerson[x],'is:', paymentMatrix[x], 'USD')
    
    input('Press any key to exit')


if __name__ == "__main__":
    main()