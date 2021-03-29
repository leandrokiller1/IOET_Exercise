# IOET_Exercise
Recruitment process exercise


## Getting Started

The exercise proposed is a script that calculate the amount of money that must be paid to the employees of the ACME company based on the days and hours worked, according to the following table:

00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD
Saturday and Sunday
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD


### Prerequisites

The solution was made in Python 3.9.2 and and includes two files, the executable file that contains the script and a text file that contains the data to be entered. It requires nothing more than a computer to run the .exe file.

In the .txt file you will find the data with which the calculations will be made to determine the amount of money that must be paid for the hours worked. This text file must have a specific format to enter the data, otherwise there will be errors in the execution.

First you must write the name of the person followed by a colon, for example:

RENE:

To enter the days you have to use the following abbreviations:

MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday


You must also write the hours in which each person works, for example:

10:00-12:00

The hours and days that a person works must be separated with commas. Finally, the data of each person must be separated with an enter, as shown in the following examples

```

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ERICK=MO00:00-7:00,WE08:00-18:00,FR12:00-20:00,SA06:00-12:00,SU15:00-00:00
LUIS=TU06:00-7:00,TH10:00-15:00,FR09:00-12:00,SU15:00-00:00
IRENE=WE04:00-12:00,TH11:00-17:00,SA06:00-11:00

```
With these data, the values that people should be paid for their working hours will be obtained. With these data, the values that people should be paid for their working hours will be obtained, which will be shown on the screen as follows:

The amount to pay RENE is: 215.0
The amount to pay ASTRID is: 85.0
The amount to pay ERICK is: 825.0
The amount to pay LUIS is: 355.0
The amount to pay IRENE is: 390.0


##Solution overview

The central problem of this exercise was to separate each one of the data to analyze it in parts. For the implemented solution, what was done was to separate the data, first by the names of the people. Then the days worked, divided by a comma, were separated . Once the separate days were obtained, the data for each day was divided depending on whether it was a weekday or if it was a weekend, and these were grouped into different matrices. Subsequently, the time intervals that people worked were obtained and, depending on what day and time of day it is, formulas were applied to obtain the value of each hour of work and added them to obtain the total amount of money that must be paid to all people.

## Code deployment

First, the data is obtained from the .txt file with the open command. Since the executable file must work on any computer, commands were used to obtain a relative path. Then the file data is divided between the name of the person and the days and hours worked with the split command.

With this division a function called workedHours was created, which is in charge of obtaining the names of the people and the hours they worked. Then the days that were worked are separated and ordered depending on whether it was a weekday or if it was a weekend. Later again, the split command was used, which divides the hours that are separated with a hyphen to find the entry time and exit time of each work day. The function workedHours will return 3 matrices, one that contains the hours worked during the week, one that contains the hours worked on the weekend and the last one that contains the names of the people.

After this, the PaymentHourWeek function was developed in which 3 time limits were included to perform the calculations: 00:00, 09:00 and 18:00, which were used to put conditions in relation to the cost depending on the time and day that people worked. In this function, the strptime method was used to transform the hours that are in string format to a date format in order to perform calculations with the entry and exit times, calculating the subtraction between these two values and multiplying by the respective cost. This function returns a matrix in which it is obtained how much people should be paid for their working hours.

Finally, in the main function, the total payment of each person is calculated and it is related to the matrix of names, then a print function shows the amount of money to be paid on the screen.



## Built With

-Python 3.9.2

## Authors

ERICK LEANDRO BORBOR PINEDA
