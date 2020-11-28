from tkinter import *

wd = Tk()
wd.title("Miles to Kilometers")
wd.minsize(width=300, height=110)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)


def button_click():
    num = float(miles_input.get())
    num *= 1.609344
    num = "{:0.2f}".format(num)
    print(num)
    conversion_output.config(text=f"{num}")


miles_label = Label(text="Miles", font=("System", 15, "normal"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("System", 15, "normal"))
is_equal_label.grid(column=0, row=1)

conversion_output = Label(text="0", font=("System", 15, "normal"))
conversion_output.grid(column=1, row=1)

km_label = Label(text="Km", font=("System", 15, "normal"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_click)
calculate_button.grid(column=1, row=2)

wd.mainloop()
