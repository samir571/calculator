from _ast import Lambda
from tkinter import*

expression = ""

def button_click(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def button_clear():
    global expression
    expression=""
    equation.set("")

def button_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error!")
        expression=""

root = Tk()
root.title("CALCULATOR")
root.iconbitmap(r'calculator.ico')
equation = StringVar()

txtDisplay = Entry(root, font=('arial', 20,'bold'), textvariable=equation,bd=30, insertwidth=30,bg="light blue")\
    .grid(columnspan=4)

#row 1 buttons:
button_7 = Button(root, text="7", padx=16, pady=16, bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(9)).grid(row=1, column=2)
Addition = Button(root, text="+", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                    command=lambda: button_click("+")).grid(row=1, column=3)


#row 2 buttons
button_4 = Button(root, text="4", padx=16, pady=16,bd=8, fg="black",font=('arial', 20,'bold'), bg="light blue",
                  command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'), bg = "light blue",
                  command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'), bg="light blue",
                  command=lambda: button_click(6)).grid(row=2, column=2)

Division = Button(root, text="/", padx=20, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                    command=lambda: button_click("/")).grid(row=2, column=3)

#row 3 buttons
button_1 = Button(root, text="1", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(3)).grid(row=3, column=2)
multiplication = Button(root, text="*", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                    command=lambda: button_click("*")).grid(row=3, column=3)


#row 4 buttons
button_0 = Button(root, text="0", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(0)).grid(row=4, column=0)
Decimal = Button(root, text=".", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                  command=lambda: button_click(".")).grid(row=4, column=1)

subtraction = Button(root, text="-", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                    command=lambda: button_click("-")).grid(row=4, column=3)
power = Button(root, text="x^y", padx=16, pady=16,bd=8,fg="black",font=('arial', 16,'bold'),bg="light blue",
                    command=lambda: button_click("**")).grid(row=4, column=2)

#row 5 buttons
button_equal = Button(root, text="=", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                      command=button_equal).grid(row=5, column=3)
button_clear = Button(root, text="C", padx=16, pady=16,bd=8,fg="black",font=('arial', 20,'bold'),bg="light blue",
                      command=button_clear).grid(row=5, column=2)
root.mainloop()