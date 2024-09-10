def Convert():
    Fahrenheit = int(input("Enter a degree: "))
    Celsus = (Fahrenheit - 32) * (5/9)
    Answer = str(Celsus)
    print("Your number is " + Answer + " degrees Celsius.")

Convert()