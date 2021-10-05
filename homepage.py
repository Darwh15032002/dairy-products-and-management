#from _typeshed import Self
from tkinter import *


class Bilpay:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing window")
        bg_color = "#DEF159"
        title = Label(self.root, text="Billing Window", relief=GROOVE, fg="black", bg=bg_color,
                      bd=12, font=("times new roman", 30), pady=2).pack(fill=X)
        f1 = LabelFrame(self.root, text="Customer details", font=(
            "times new roman", 15, "bold"), bd=10, relief=GROOVE, fg="blue", bg=bg_color)
        f1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(f1, text="Customer Name", bg=bg_color, fg="black", font=(
            "times new roman", 18, "bold")).grid(row=0, column=0, padx=15, pady=5)
        cname_txt = Entry(f1, width=20, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphone_lbl = Label(f1, text="Customer phone ", bg=bg_color, fg="black", font=(
            "times new roman", 18, "bold")).grid(row=0, column=2, padx=15, pady=5)
        cphone_txt = Entry(f1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(f1, text="Bil number", bg=bg_color, fg="black", font=(
            "times new roman", 18, "bold")).grid(row=0, column=4, padx=15, pady=5)
        cbill_txt = Entry(f1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)
        bill_btn = Button(f1, text="Search", width=8, bd=5,
                          font="arial 12 bold").grid(row=0, column=6, pady=10, padx=10)

       # milk frame
        f2 = LabelFrame(self.root, text="Milk products", font=(
            "times new roman", 15, "bold"), bd=10, relief=GROOVE, fg="blue", bg="#DEF159")
        f2.place(x=5, y=180, width=325, height=385)
        cow_lbl = Label(f2, text="Cow(AMUL 250ml)", font=("Times new roman ", 12, "bold"),
                        bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cow_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                        bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        buff_lbl = Label(f2, text="Buffellow (AMUL 250ml)", font=("Times new roman ", 12, "bold"),
                         bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        buff_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                         bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        chass1_lbl = Label(f2, text="chass (AMUL 250ml)", font=("Times new roman ", 12, "bold"),
                           bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        chass1_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                           bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        chass2_lbl = Label(f2, text="chass (AMUL 500ml)", font=("Times new roman ", 12, "bold"),
                           bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        chass2_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                           bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        dahi1_lbl = Label(f2, text="DAHI (AMUL 100gm)", font=("Times new roman ", 12, "bold"),
                          bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        dahi1_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                          bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        dahi2_lbl = Label(f2, text="DAHI (AMUL 250gm)", font=("Times new roman ", 12, "bold"),
                          bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        dahi2_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                          bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        lassii_lbl = Label(f2, text="lassi (AMUL 100gm)", font=("Times new roman ", 12, "bold"),
                           bg=bg_color, fg="black").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        lassii_txt = Entry(f2, width=8, font=("Times new roman ", 12, "bold"),
                           bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)
        # milk frame
        f3 = LabelFrame(self.root, text="COLD DRINKS", font=(
            "times new roman", 15, "bold"), bd=10, relief=GROOVE, fg="blue", bg="#DEF159")
        f3.place(x=335, y=180, width=670, height=385)
        masti_lbl = Label(f3, text="AMUL MASTI(butter milk)", font=("Times new roman ", 12, "bold"),
                          bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        masti_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                          bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        chocomilkshake_lbl = Label(f3, text="double chocomilkshake", font=("Times new roman ", 12, "bold"),
                                   bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        chocomilkshake_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                                   bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        cafe_lbl = Label(f3, text="kool cafe", font=("Times new roman ", 12, "bold"),
                         bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cafe_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                         bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        irish_lbl = Label(f3, text="irish drink", font=("Times new roman ", 12, "bold"),
                          bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        irish_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                          bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        pina_lbl = Label(f3, text="pina colada", font=("Times new roman ", 12, "bold"),
                         bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        pina_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                         bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        tru_lbl = Label(f3, text="amul tru", font=("Times new roman ", 12, "bold"),
                        bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tru_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                        bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        memory_lbl = Label(f3, text="Memory milk", font=("Times new roman ", 12, "bold"),
                           bg=bg_color, fg="black").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        memory_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                           bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)
        dairymilk_lbl = Label(f3, text="dairymilk", font=("Times new roman ", 12, "bold"),
                              bg=bg_color, fg="black").grid(row=0, column=3, padx=10, pady=10, sticky="w")
        dairymilk_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                              bd=5, relief=SUNKEN).grid(row=0, column=4, padx=10, pady=10)
        silk_lbl = Label(f3, text="silk", font=("Times new roman ", 12, "bold"),
                         bg=bg_color, fg="black").grid(row=1, column=3, padx=10, pady=10, sticky="w")
        silk_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                         bd=5, relief=SUNKEN).grid(row=1, column=4, padx=10, pady=10)
        bubly_lbl = Label(f3, text="bubbly", font=("Times new roman ", 12, "bold"),
                          bg=bg_color, fg="black").grid(row=2, column=3, padx=10, pady=10, sticky="w")
        bubly_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                          bd=5, relief=SUNKEN).grid(row=2, column=4, padx=10, pady=10)
        oreo_lbl = Label(f3, text="oreo", font=("Times new roman ", 12, "bold"),
                         bg=bg_color, fg="black").grid(row=3, column=3, padx=10, pady=10, sticky="w")
        oreo_txt = Entry(f3, width=8, font=("Times new roman ", 12, "bold"),
                         bd=5, relief=SUNKEN).grid(row=3, column=4, padx=10, pady=10)


root = Tk()
obj = Bilpay(root)
root.mainloop()
