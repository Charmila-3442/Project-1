a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))
t=float(input("Enter time t(hour/day): "))

t=a*t**2+b*t+c
print(f"Prdicted temperature at t={t} : {t:.2f} degrees Celsius")
