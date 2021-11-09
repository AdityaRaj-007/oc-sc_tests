from tkinter import *


def get_values():
    Vo_ = float(Vo.get())
    Vsc_ = float(Vsc.get())
    Io_ = float(Io.get())
    Isc_ = float(Isc.get())
    Wo_ = float(Wo.get())
    Wsc_ = float(Wsc.get())
    return Vo_, Vsc_, Io_, Isc_, Wo_, Wsc_


def calculate():
    Voc, Vsc_, Ioc, Isc_, Woc, Wsc_ = get_values()
    cos = Woc/(Voc*Ioc)
    Icore = Ioc*cos
    Im = Ioc*((1-cos**2)**0.5)
    Rc = Voc/Icore
    Xm = Voc/Im
    Zsc = Vsc_/Isc_
    Rsc = Wsc_/(Isc_**2)
    Xsc = ((Zsc**2)-(Rsc**2))**0.5
    print("Open circuit test results\n")
    print("Icore = {0:.2f}\n".format(Icore))
    print("Im = {0:.2f}\n".format(Im))
    print("Xm = {0:.2f}\n".format(Xm))
    print("Rc = {0:.2f}\n".format(Rc))
    print("Short circuit test results\n")
    print("Zsc = {0:.2f}\n".format(Zsc))
    print("Rsc = {0:.2f}\n".format(Rsc))
    print("Xsc = {0:.2f}\n".format(Xsc))


root = Tk()
root.title("Transformer Tests")
root.geometry("924x574")

oc_test = Label(root, text="Open circuit test", relief=RAISED, bg="black", fg="white", font="comicsansms 20 bold ", padx=10, pady=10)
oc_test.grid(row=0, column=1, padx=10)

sc_test = Label(root, text="Short circuit test", relief=RAISED, bg="black", fg="white", font="comicsansms 20 bold ", padx=10, pady=10)
sc_test.grid(row=0, column=2, padx=10)

voltage = Label(root, text="Voltage(Volts)", borderwidth=8, bg="black", fg="white", relief=RAISED, font='comicsansms 18 ', padx=19, pady=15)
current = Label(root, text="Current(Amp)", borderwidth=8, bg="black", fg="white", relief=RAISED, font='comicsansms 18 ', padx=20, pady=15)
power = Label(root, text="Power(Watts)", borderwidth=8, bg="black", fg="white", relief=RAISED, font='comicsansms 18 ', padx=20, pady=15)
voltage.grid(row=1, column=0)
current.grid(row=2, column=0)
power.grid(row=3, column=0)

Vo = StringVar()
Io = StringVar()
Wo = StringVar()
Vsc = StringVar()
Isc = StringVar()
Wsc = StringVar()

Vo_value = Entry(root, textvariable=Vo, font="comicsansms 18", relief=SUNKEN, borderwidth=8)
Vsc_value = Entry(root, textvariable=Vsc, font="comicsansms 18", relief=SUNKEN, borderwidth=8)
Io_value = Entry(root, textvariable=Io, font="comicsansms 18", relief=SUNKEN, borderwidth=8)
Isc_value = Entry(root, textvariable=Isc, font="comicsansms 18", relief=SUNKEN, borderwidth=8)
Wo_value = Entry(root, textvariable=Wo, font="comicsansms 18", relief=SUNKEN, borderwidth=8)
Wsc_value = Entry(root, textvariable=Wsc, font="comicsansms 18", relief=SUNKEN, borderwidth=8)

Vo_value.grid(row=1, column=1, padx=10)
Vsc_value.grid(row=1, column=2, padx=10)
Io_value.grid(row=2, column=1, padx=10)
Isc_value.grid(row=2, column=2, padx=10)
Wo_value.grid(row=3, column=1, padx=10)
Wsc_value.grid(row=3, column=2, padx=10)

b1 = Button(root, text="Calculate", font="comicsansms 18", relief=RAISED, borderwidth=6, bg="black", fg="white", command=calculate)
b1.grid(row=4, column=1)

root.mainloop()
