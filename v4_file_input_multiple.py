with open("inputs_multiple.txt","r") as f:
    for lines in f:
        a,b,c,t=map(float,lines.split())
        t=a*t**2+b*t+c
        print(f"Prdicted temperature at t={t} : {t:.2f} degrees Celsius")
