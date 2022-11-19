hrs = input("Enter Hours:")
h = float(hrs)
rate= input("Enter rate:")
r= float(rate)
if h < 40:
    gross_pay= h * r
else:
    overtime= h- 40
    gross_pay= (overtime*(r * 1.5)) +(h-overtime)*r
print(gross_pay)