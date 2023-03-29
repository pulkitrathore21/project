from logic import changeCtoF,changeFtoC
def init():

    
    exit=False
    while exit==False:
        temp=float(input("enter temperature in celcius:"))
        print("C: for converting from celcius to fereiheit\n F: for converting from fereiheit to celcius:\n0.exit")
        cha=input("enter your choice:")
        if cha.upper()=="C":
            r=changeCtoF(temp)
            print(f"{temp} degrees Celsius is {r} degrees Fahrenheit.")

        if cha.upper()=="F":
            r=changeFtoC(temp)
            print(f"{temp}degree fehrenheit is {r}degrees celcius")
        if cha.upper()=="0":
            exit=True
        



        