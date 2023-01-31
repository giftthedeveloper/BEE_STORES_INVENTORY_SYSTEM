#THANK YOU JESUS FOR LIGHT
#ABBA THE WAY
#HOLYSPIRIT MY LIFE
#THANKS TO THE HOLYSPIRIT


import tkinter as tk
import tkinter.messagebox as tkmessagebox
import pyodbc
import tkinter.ttk as ttk
#SETTING THE WINDOW GUI===========================================================
root = tk.Tk()
root.title("BEE STORES INVENTORY SYSTEM")
width = 1024
height = 520
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x =(screenwidth/2) - (width/2)
y = (screenheight/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg ="#8fdbc5")
#==================================================================================
#VARIABLESSSSSSS===================================================================
USERNAME = tk.StringVar()
PASSWORD = tk.StringVar()
SEARCH = tk.StringVar()
PRODUCT_NAME =tk.StringVar()
PRODUCT_QUANTITY = tk.StringVar()
SEARCH = tk.StringVar()
SEARCH_RESULT= tk.StringVar()
PRODUCT_NAME3 =tk.StringVar()
PRODUCT_QUANTITY3 =tk.StringVar()
PRODUCT_PRICE1 = tk.StringVar()

#=================================================
bg = tk.PhotoImage(file='bgtest.png')
labell = tk.Label(root, image=bg)
labell.place(x=0, y=0)
#=================================================
#functions==============================================
def logout():
    question = tkmessagebox.askquestion("BEE STORES INVENTORY","\nAre you sure you want to logout ?",icon="warning")
    if question == "yes":
        admin_id = ''
        root.destroy()

def Database():
    global conn, cursor
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Wikay\PycharmProjects\YAH\BEE STORES.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected to Database")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Table1 WHERE username ='Gift' AND password ='admin';")
    print("okay")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Table1 (username, password) VALUES ('Gift', 'admin')")
        conn.commit()

def displayloginsettings():
    global loginform
    loginform = tk.Toplevel()
    loginform.title("BEE STORES INVENTORY SYSTEM/LOGIN")
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = (screenwidth/2) - (width/2)
    y = (screenheight/2) - (height/2)
    loginform.resizable(0,0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():
    global result_label #lf stands for login form
    login_form_header = tk.Frame(loginform, width=600, height=30,bg="#64adc4")
    login_form_header.pack(side="top", pady=20)
    login_admin_text = tk.Label(loginform, text="LOGIN AS ADMIN",fg="#367096", width=600, font=("impact", 22))
    login_admin_text.pack()
    midloginform = tk.Frame(loginform, width=600)
    midloginform.pack(side="top", pady=50)
    username_label = tk.Label(midloginform,fg="#367096", text="Username:", font=("helvetica bold", 20), bd=10)
    username_label.grid(row=0)
    password_label = tk.Label(midloginform,fg="#367096", text="Password:", font=("helvetica bold", 20), bd=20)
    password_label.grid(row=1)
    result_label = tk.Label(midloginform, text="", font=("helvetica", 20))
    result_label.grid(row=3, columnspan=2)
    username = tk.Entry(midloginform, bg="#bfdbc5", textvariable=USERNAME,width=20, font=("helvetica", 16))
    username.grid(row=0, column=1)
    password = tk.Entry(midloginform, bg="#bfdbc5", textvariable=PASSWORD,width=20, font=("helvetica", 16), show="*")
    password.grid(row=1, column=1)
    login_btn = tk.Button(midloginform,bg='#367096', fg="#ffffff", text="LOGIN", font=("helvetica bold", 18), command=Login)
    login_btn.grid(row=2, columnspan=2, pady=20)
    login_btn.bind('<Return>', Login)


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get == "":
        result_label.config(text="Please fill in the required fields", fg="red")
    else:
        cursor.execute("SELECT * FROM Table1 WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM Table1 WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            result_label.config(text="")
            root.mainloop()

        else:
            result_label.config(text="Invalid Username or Password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close()

def display_search():
    global searchwindow
    searchwindow = tk.Toplevel()
    searchwindow.title("BEE STORES INVENTORY SYSTEM/SEARCH")
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = (screenwidth / 2) - (width / 2)
    y = (screenheight / 2) - (height / 2)
    searchwindow.resizable(0, 0)
    searchwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    searchform()

def searchform():
    global search_result_label
    global parent_s # lf stands for login form
    search_form_header = tk.Frame(searchwindow, width=600, height=30, bg="#64adc4")
    search_form_header.pack(side="top", pady=20)
    search_text = tk.Label(searchwindow, text="SEARCH", fg="#367096", width=600, font=("impact", 22))
    search_text.pack()
    midsearchform = tk.Frame(searchwindow, width=600)
    midsearchform.pack(side="top", pady=50)
    search_entry = tk.Entry(searchwindow, bg="#bfdbc5", textvariable=SEARCH_RESULT, width=25, font=("helvetica", 20))
    search_entry.place(x=80, y=120)
    search_enter_btn = tk.Button(searchwindow,height=1, bg='#367096', fg="#ffffff", text="SEARCH", font=("helvetica bold", 16),
                          command=search_result)
    search_enter_btn.place(x=455, y=118)


    Midsearchresultform = tk.Frame(searchwindow, width=600)
    Midsearchresultform.pack(side="bottom")
    scrollbarx = tk.Scrollbar(Midsearchresultform, orient="horizontal")
    scrollbary = tk.Scrollbar(Midsearchresultform, orient="vertical")
    parent_s= ttk.Treeview(Midsearchresultform, columns=("ProductID", "Product Name", "Product Price"),
                          selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                          xscrollcommand=scrollbarx.set)
    scrollbary.config(command=parent_s.yview)
    scrollbary.pack(side="right", fill="y")
    scrollbarx.config(command=parent_s.xview)
    scrollbarx.pack(side="bottom", fill="x")
    parent_s.heading('ProductID', text="ProductID", anchor="w")
    parent_s.heading('Product Name', text="Product Name", anchor="w")
    parent_s.heading('Product Price', text="Product Price", anchor="w")
    parent_s.column('#0', stretch="no", minwidth=0, width=0)
    parent_s.column('#1', stretch="no", minwidth=0, width=0)
    parent_s.column('#2', stretch="no", minwidth=0, width=200)
    parent_s.column('#3', stretch="no", minwidth=0, width=120)
    parent_s.pack()
    display_display_data()

def display_display_data():
    Database()
    cursor.execute("SELECT * FROM Table3")
    fetch = cursor.fetchall()
    for data in fetch:
        parent_s.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def search_result():
    if SEARCH_RESULT.get() != "":
        parent_s.delete(*parent_s.get_children())
        Database()
        cursor.execute("SELECT * FROM Table3 WHERE product_name LIKE ?", ('%'+str(SEARCH_RESULT.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            parent_s.insert('', 'end', values=(data))
            print("done")
        cursor.close()
        conn.close()


def display_shop_now():
    global shopnowform
    shopnowform = tk.Toplevel()
    shopnowform.title("BEE STORES INVENTORY SYSTEM/Shop Now")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    shopnowform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    shopnowform.resizable(0, 0)
    shop_now_form()


def shop_now_form():

    shop_now_form_header = tk.Frame(shopnowform, width=600, height=30, bg="#64adc4")
    shop_now_form_header.pack(side="top", pady=20)
    shop_now_text = tk.Label(shopnowform, text="SHOP NOW", fg="#367096", width=600, font=("impact", 22))
    shop_now_text.pack()
    subshopnow = tk.Frame(shopnowform, width=600)
    subshopnow.pack(side="top", pady=50)
    product_label = tk.Label(subshopnow,fg="#367096", text="Product Name:", font=("Helvetica bold", 16))
    product_label.grid(row=0, sticky="w")
    quantity_label =tk.Label(subshopnow,fg="#367096", text="Product Quantity:", font=("Helvetica bold", 16))
    quantity_label.grid(row=3, sticky="W")
    prod_name_entry = tk.Entry(subshopnow, textvariable=PRODUCT_NAME, font=("helvetica", 18))
    prod_name_entry.grid(row=0, column=2)
    prod_qty_entry = tk.Entry(subshopnow, textvariable=PRODUCT_QUANTITY, font=("helvetica", 18))
    prod_qty_entry.grid(row=3, column=2)
    add_to_cart_btn = tk.Button(subshopnow, text="Add To Cart",font=("helvetica bold", 12), command=real_shop_now)
    add_to_cart_btn.grid(row=4, columnspan=6, pady=20)
    view_cart_btn = tk.Button(subshopnow, text="View Cart", font=("helvetica bold", 12), command=show_view)
    view_cart_btn.grid(row=4, columnspan=1, pady=20)



def real_shop_now():
    Database()

    cursor.execute("INSERT INTO Table2 (product_name, product_quantity)  VALUES(?, ?)", (str(PRODUCT_NAME.get()), (str(PRODUCT_QUANTITY.get()))))
    conn.commit()
    #cursor.execute("SELECT product_price FROM Table3 INNER JOIN Table2 WHERE Table3.product_name =Table2.product_name")
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_QUANTITY.set("")
    cursor.close()
    conn.close()

def show_view():
    global viewform
    viewform = tk.Toplevel()
    viewform.title("Simple Inventory System/View Cart")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    view_shopping()


def view_shopping():
    global parent
    TopViewForm = tk.Frame(viewform, width=400)
    TopViewForm.pack(side="bottom", fill="x")
    LeftViewForm = tk.Frame(viewform, width=600)
    LeftViewForm.pack(side="left", fill="y")
    MidViewForm = tk.Frame(viewform, width=600)
    MidViewForm.pack(side="right")
    view_cart_text = tk.Label(TopViewForm, text="View Products", font=('helvetica', 15), width=600)
    view_cart_text.pack(fill="x")
    view_cart_search = tk.Label(LeftViewForm, text="Search", font=('helvetica', 12))
    view_cart_search.pack(side="top", anchor="w")
    view_cart_search_entry = tk.Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    view_cart_search_entry.pack(side="top", padx=10, fill="x")
    view_cart_search_btn = tk.Button(LeftViewForm, text="Search", command=Search)
    view_cart_search_btn.pack(side="top", padx=10, pady=10, fill="x")
    view_cart_reset_btn = tk.Button(LeftViewForm, text="Reset", command=Reset)
    view_cart_reset_btn.pack(side="top", padx=10, pady=10, fill="x")
    view_cart_delete_btn = tk.Button(LeftViewForm, text="Delete", command=Delete)
    view_cart_delete_btn.pack(side="top", padx=10, pady=10, fill="x")
    scrollbarx = tk.Scrollbar(MidViewForm, orient="horizontal")
    scrollbary = tk.Scrollbar(MidViewForm, orient="vertical")
    parent = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price", "TOTAL"),
                         selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=parent.yview)
    scrollbary.pack(side="right", fill="y")
    scrollbarx.config(command=parent.xview)
    scrollbarx.pack(side="bottom", fill="x")
    parent.heading('ProductID', text="ProductID", anchor="w")
    parent.heading('Product Name', text="Product Name", anchor="w")
    parent.heading('Product Qty', text="Product Qty", anchor="w")
    parent.heading('Product Price', text="Product Price", anchor="w")
    parent.heading('TOTAL', text="TOTAL", anchor="w")
    parent.column('#0', stretch="no", minwidth=0, width=0)
    parent.column('#1', stretch="no", minwidth=0, width=0)
    parent.column('#2', stretch="no", minwidth=0, width=200)
    parent.column('#3', stretch="no", minwidth=0, width=120)
    parent.column('#4', stretch="no", minwidth=0, width=120)
    parent.column('#5', stretch="no", minwidth=0, width=120)
    parent.pack()
    Display_shopping_data()

def Display_shopping_data():
    Database()
    cursor.execute("SELECT * FROM Table2")
    fetch = cursor.fetchall()
    for data in fetch:
        parent.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        parent.delete(*parent.get_children())
        Database()
        cursor.execute("SELECT * FROM Table2 WHERE product_name LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            parent.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    parent.delete(*parent.get_children())
    Display_shopping_data()
    SEARCH.set("")

def Delete():
    selected_item = parent.selection()
    uid = parent.item(selected_item)['values']
    # contents =(parent.item(selectproduct))
    # selecteditem = contents['values']
    parent.delete(selected_item)
    Database()
    #('%' + str(SEARCH.get()) + '%',))
    cursor.execute("DELETE FROM Table2 WHERE product_id=%s",(uid))
    conn.commit()
    cursor.close()
    conn.close()

def show_restock():
    global restockform
    restockform = tk.Toplevel()
    restockform.title("Simple Inventory System/Restock")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    restockform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    restockform.resizable(0, 0)
    view_restock()



def view_restock():
    restock_form_header = tk.Frame(restockform, width=600, height=30, bg="#64adc4")
    restock_form_header.pack(side="top", pady=20)
    restock_text = tk.Label(restockform, text="RESTOCK", fg="#367096", width=600, font=("impact", 22))
    restock_text.pack()
    subrestock = tk.Frame(restockform, width=600)
    subrestock.pack(side="top", pady=50)
    product_label = tk.Label(subrestock, fg="#367096", text="Product Name:", font=("Helvetica bold", 16))
    product_label.grid(row=0, sticky="w")
    quantity_label = tk.Label(subrestock, fg="#367096", text="Product Quantity:", font=("Helvetica bold", 16))
    quantity_label.grid(row=2, sticky="W")
    product_price = tk.Label(subrestock, fg="#367096", text="Price Per Unit:", font=("Helvetica bold", 16))
    product_price.grid(row=3, sticky="W")
    prod_name_entry = tk.Entry(subrestock, textvariable=PRODUCT_NAME3, font=("helvetica", 18))
    prod_name_entry.grid(row=0, column=2)
    prod_qty_entry = tk.Entry(subrestock, textvariable=PRODUCT_QUANTITY3, font=("helvetica", 18))
    prod_qty_entry.grid(row=2, column=2)
    prod_price_entry = tk.Entry(subrestock, textvariable=PRODUCT_PRICE1, font=("helvetica", 18))
    prod_price_entry.grid(row=3, column=2)
    done_btn = tk.Button(subrestock, text="Add To Stock", font=("helvetica bold", 12), command=restock)
    done_btn.grid(row=4, columnspan=6, pady=20)
#"INSERT INTO Table1 (username, password) VALUES ('Gift', 'admin')"

def restock():
    Database()

    trials = cursor.execute("SELECT * FROM Table3 WHERE product_name = ?",
                                               (str(PRODUCT_NAME3.get())))
    cursor.execute("SELECT * FROM Table3 WHERE product_name=? AND UPDATE product_price SET product_price.value = product_price + ?", (str(PRODUCT_NAME3.get()), str(PRODUCT_PRICE1.get())))
    cursor.execute("INSERT INTO Table3 (product_name, product_quantity, product_price) VALUES(?, ?, ?)",
                   (str(PRODUCT_NAME3.get()), (str(PRODUCT_QUANTITY3.get())), (str(PRODUCT_PRICE1.get()))))
    cursor.fetchall()
    conn.commit()

    PRODUCT_NAME3.set("")
    PRODUCT_QUANTITY3.set("")
    PRODUCT_PRICE1.set("")
    cursor.close()
    conn.close()


def thing():
    my_label.config(text = "You clicked on a button")
def xit():
    print("hello")

#========================================================
#MENUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=thing)
filemenu.add_command(label="Exit", command=xit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label='Help', menu=filemenu)
root.config(menu=menubar)


#---------------------------------------------------------

Title = tk.Frame(root, bd=0, )
Title.pack(pady=0)

#TOP DESIGN=========================================================
top_header = tk.Label(Title,height=1, width=150, bg="#64adc4")
top_header.pack(pady=0)

#DISPLAY HEADER=======================================================
display_label_text = tk.Label(root, text="BEE STORES INVENTORY SYSTEM", fg="#367096",font=("impact", 45))
display_label_text.pack(pady=0)

#testing arena===========================================================


login_btn_1 = tk.PhotoImage(file='carticon.png')
login_btn_2 = tk.PhotoImage(file='ZOOMICON.png')
login_btn_3 = tk.PhotoImage(file='receipticon.png')
login_btn_4 = tk.PhotoImage(file='add.png')
btn_5 = tk.PhotoImage(file='acct.png')

# img_label = tk.Label(image=login_btn)
# img_label.pack(pady=20)

my_button_cart_icon = tk.Button(root, borderwidth=0, width=250, height=250, image=login_btn_1, command=display_shop_now)
my_button_cart_icon.place(x=20,y=120)
my_label_cart_icon =tk.Label(text="Shop Now", font=("helvetica", 10))
my_label_cart_icon.place(x=110, y=350)

my_button_search_icon = tk.Button(root, borderwidth=0, width=250, height=250, image=login_btn_2, command=display_search)
my_button_search_icon.place(x=270,y=120)
my_label_search_icon =tk.Label(text="Search For Product/Item", font=("helvetica", 10))
my_label_search_icon.place(x=325, y=350)

my_button_receipt_icon = tk.Button(root, borderwidth=0, width=250, height=250, image=login_btn_3, command=thing)
my_button_receipt_icon.place(x=520,y=120)
my_label_receipt_icon =tk.Label(text="Print Receipt/Invoice", font=("helvetica", 10))
my_label_receipt_icon.place(x=590, y=350)

my_button_account_icon = tk.Button(root, borderwidth=0, width=250, height=250, image=login_btn_4, command=show_restock)
my_button_account_icon.place(x=760,y=120)
my_label_account_icon =tk.Label(text="Add new items to Stock", font=("helvetica", 10))
my_label_account_icon.place(x=820, y=350)

up_label = tk.Button(root, borderwidth=0, width=50, height=50, image=btn_5, command=logout)
up_label.place(x=900, y=30)
my_label_account_icon =tk.Label(text="Accounts", font=("helvetica", 10))
my_label_account_icon.place(x=900, y=80)

my_label = tk.Label(root, text='')
my_label.pack(pady=20)
displayloginsettings()

root.mainloop()