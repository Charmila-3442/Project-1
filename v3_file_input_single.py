with open("inputs_single.txt","r") as f:
    lines=f.readlines()

a=float(lines[0])
b=float(lines[1])
c=float(lines[2])
t=float(lines[3])

t=a*t**2+b*t+c
print(f"Prdicted temperature at t={t} : {t:.2f} degrees Celsius")
