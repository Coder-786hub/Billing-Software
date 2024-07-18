from tkinter import * 
from tkinter import messagebox
import random,os,tempfile,smtplib,mysql.connector
from mysql.connector import Error
import qrcode
from PIL import Image, ImageTk

# mysql connection 

def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786"
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS BILLING_DATA")
    cursor.close()
    connection.close()

def create_table_CUSTOMER_DETAILS():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CUSTOMER_DATA (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(50),
        PHONE_NO VARCHAR(15),
        BILL_NO VARCHAR(10),
        TOTAL_AMOUNT VARCHAR(15)
    )
    """)
    cursor.close()
    connection.close()

def create_table_cosmetics():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS COSMETICS_DATA (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        PRODUCT_NAME VARCHAR(50),
        QUANTITY INT,
        PRICE DECIMAL(10, 2)
    )""")
    cursor.close()
    connection.close()

def create_table_grocery():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS GROCERY_DATA (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        PRODUCT_NAME VARCHAR(50),
        QUANTITY INT,
        PRICE DECIMAL(10, 2)
    )
    """)
    cursor.close()
    connection.close()

def create_table_cold_drinks():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS COLD_DRINKS_DATA (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        PRODUCT_NAME VARCHAR(50),
        QUANTITY INT,
        PRICE DECIMAL(10, 2)
    ) 
    """)
    cursor.close()
    connection.close()



# Functionalaty

SENDER_EMAIL = "aftablamkhan8932@gmail.com"
SENDER_PASSWORD = "hokq mxxb dktx ofqm"

def email_bill():
    def send_gmail():
        try:
            ob = smtplib.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login(SENDER_EMAIL, SENDER_PASSWORD)
            message = email_textarea.get(1.0, END)
            ob.sendmail(SENDER_EMAIL, receiverEntry.get(), message)
            ob.quit()
            messagebox.showinfo("Success", "Bill is successfully sent", parent=root1)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Something went wrong. Please try again", parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror("Error", "Bill is empty")
    else:
        root1 = Toplevel()
        root1.title("Send Gmail")
        root1.config(bg="gray20")
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text="SENDER", font=("arial", 16, "bold"), bd=6, bg="gray20", fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=("arial", 14, "bold"), bg="gray20", fg="white")
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=("arial", 16, "bold"), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=10)
        senderEntry.insert(END, SENDER_EMAIL)  # Set default sender email

        passwordLabel = Label(senderFrame, text="Password", font=("arial", 14, "bold"), bg="gray20", fg="white")
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=("arial", 16, "bold"), bd=2, width=23, relief=RIDGE, fg="black", show="*")
        passwordEntry.grid(row=1, column=1, padx=10, pady=10)
        passwordEntry.insert(END, SENDER_PASSWORD)  # Set default password

        receipentFrame = LabelFrame(root1, text="RECIPIENT", font=("arial", 16, "bold"), bd=6, bg="gray20", fg='white')
        receipentFrame.grid(row=1, column=0, padx=40, pady=20)

        ReceiverLabel = Label(receipentFrame, text="Email Address", font=("arial", 14, "bold"), bg="gray20", fg="white")
        ReceiverLabel.grid(row=0, column=0, padx=10, pady=8)

        receiverEntry = Entry(receipentFrame, font=("arial", 16, "bold"), bd=2, width=23, relief=RIDGE, fg="black")
        receiverEntry.grid(row=0, column=1, padx=10, pady=10)

        messageLabel = Label(receipentFrame, text="Message ", font=("arial", 14, "bold"), bg="gray20", fg="white")
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(receipentFrame, font=("arial", 14, "bold"), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace("=", '').replace('-', '').replace("\t\t\t", "\t\t"))

        sendbutton = Button(root1, text="SEND", font=("arial", 16, "bold"), width=15, command=send_gmail)
        sendbutton.grid(row=2, column=0, pady=20)

        root1.mainloop()


  
def print_bill():
    if textarea.get(1.0,END)==('\n'):
        messagebox.showerror("Error","Bill is empty")
    else:
        file=tempfile.mktemp(".txt")
        open(file,"w").write(textarea.get(1.0,END))
        os.startfile(file,"print")


def search_bill():
    bill_number = bill_number_entry.get()
    if not bill_number:
        messagebox.showerror("Error", "Invalid Bill Number")
        return

    for i in os.listdir("Bills/"):
        if i.split(".")[0] == bill_number:
            with open(f"Bills/{i}", "r") as f:
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END, data)
            break
    else:
        messagebox.showerror("Error", "Bill Number not found")

if not os.path.exists("Bills/"):
    os.mkdir("Bills/")

def save_bill():
    global billnumber
    result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f"Bills/{billnumber}.txt", "w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success", f"Bill Number {billnumber} is saved successfully")
        insert_billing_data()
billnumber = random.randint(1, 1000)
 
# inserting data in tables
def insert_billing_data():
    customer_name = name_entry.get()
    customer_phone = phone_entry.get()
    bill_no = billnumber
    total_amount = f"{totalbill:.3f} RS"

    # Insert customer details into CUSTOMER_DATA table
    insert_customer_details(customer_name, customer_phone, bill_no, total_amount)

    # Insert cosmetic data into COSMETICS_DATA table if quantities are not zero
    if bath_entry.get() != "0":
        insert_cosmetics_data("Bath Soap", bath_entry.get(), soapPrice)
    if facecream_entry.get() != "0":
        insert_cosmetics_data("Face Cream", facecream_entry.get(), facecreamPrice)
    if facewash_entry.get() != "0":
        insert_cosmetics_data("Face Cream", facewash_entry.get(), facewashPrice)
    if hairspray_entry.get() != "0":
        insert_cosmetics_data("Face Cream", hairspray_entry.get(), hairsprayPrice)
    if hairgel_entry.get() != "0":
        insert_cosmetics_data("Face Cream", hairgel_entry.get(), hairgelPrice)
    if bodylotion_entry.get() != "0":
        insert_cosmetics_data("Face Cream", bodylotion_entry.get(), bodylotionPrice)
    

    # Insert grocery data into GROCERY_DATA table if quantities are not zero
    if Rice_entry.get() != "0":
        insert_grocery_data("Rice", Rice_entry.get(), ricePrice)
    if oil_entry.get() != "0":
        insert_grocery_data("Oil", oil_entry.get(), oilPrice)
    if Daal_entry.get() != "0":
        insert_grocery_data("Daal", Daal_entry.get(), dallPrice)
    if Wheat_entry.get() != "0":
        insert_grocery_data("Wheat", Wheat_entry.get(), wheatPrice)
    if Sugar_entry.get() != "0":
        insert_grocery_data("Sugar", Sugar_entry.get(), sugaarPrice)
    if Tea_entry.get() != "0":
        insert_grocery_data("Tea", Tea_entry.get(), teaPrice)
    

    # Insert cold drinks data into COLD_DRINKS_DATA table if quantities are not zero
    if Maaza_entry.get() != "0":
        insert_cold_drinks_data("Maaza", Maaza_entry.get(), maazaPrice)
    if Pepsi_entry.get() != "0":
        insert_cold_drinks_data("Pepsi", Pepsi_entry.get(), pepsiPrice)
    if Sprite_entry.get() != "0":
        insert_cold_drinks_data("Sprite", Sprite_entry.get(), spritePrice)
    if Dew_entry.get() != "0":
        insert_cold_drinks_data("Dew", Dew_entry.get(), dewprice)
    if Frooti_entry.get() != "0":
        insert_cold_drinks_data("Frooti", Frooti_entry.get(), frootiPrice)
    if Coca_Cola_entry.get() != "0":
        insert_cold_drinks_data("Coca Cola", Coca_Cola_entry.get(), cocaColaPrice)
    
# inserting customer details in customer table
def insert_customer_details(name, phone_no, bill_no, total_amount):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    customer_insert_query = ("INSERT INTO CUSTOMER_DATA (NAME, PHONE_NO, BILL_NO, TOTAL_AMOUNT) VALUES (%s, %s, %s, %s)")
    cursor.execute(customer_insert_query, (name, phone_no, bill_no, total_amount))
    connection.commit()
    cursor.close()
    connection.close()

# # INSERT DATA IN cosmetic_TABLE
def insert_cosmetics_data(product_name, quantity, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cosmetics_insert_query = ("INSERT INTO COSMETICS_DATA (PRODUCT_NAME, QUANTITY, PRICE) VALUES (%s, %s, %s)")
    cursor.execute(cosmetics_insert_query, (product_name, quantity, price))
    connection.commit()
    cursor.close()
    connection.close()

# # INSERT DATA IN grocery_TABLE
def insert_grocery_data(product_name, quantity, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    grocery_insert_query = ("INSERT INTO GROCERY_DATA (PRODUCT_NAME, QUANTITY, PRICE) VALUES (%s, %s, %s)")
    cursor.execute(grocery_insert_query, (product_name, quantity, price))
    connection.commit()
    cursor.close()
    connection.close()

# INSERT DATA IN cold_drinks_TABLE
def insert_cold_drinks_data(product_name, quantity, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="BILLING_DATA"
    )
    cursor = connection.cursor()
    cold_drinks_insert_query = ("INSERT INTO COLD_DRINKS_DATA (PRODUCT_NAME, QUANTITY, PRICE) VALUES (%s, %s, %s)")
    cursor.execute(cold_drinks_insert_query, (product_name, quantity, price))
    connection.commit()
    cursor.close()
    connection.close()

def bill_area():
    if name_entry.get() == "" and phone_entry.get() == "":
        messagebox.showerror("Error", "Customer Details Are Required")
    elif Cosmeticprice_entry.get() == "" and groceryprice_entry.get() == "" and Colddrinkprice_entry.get() == "":
        messagebox.showerror("Error", "No Products Are Selected")
    elif Cosmeticprice_entry.get() == "0 RS" and groceryprice_entry.get() == "0 RS" and Colddrinkprice_entry.get() == "0 RS":
        messagebox.showerror("Error", "No Products Are Selected")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, " \t\t\t**Welcome Customer**\n")
        textarea.insert(END, f"\nBill Number: {billnumber}\n")
        textarea.insert(END, f"\nCustomer Name: {name_entry.get()}\n")
        textarea.insert(END, f"\nCustomer Phone Number: {phone_entry.get()}\n")
        textarea.insert(END,"\n============================================================\n")
        textarea.insert(END,"Products\t\t\tQuantity\t\t\tPrice\n")
        textarea.insert(END,"\n============================================================\n")
        if bath_entry.get()!="0":
            textarea.insert(END,f"Bath Soap\t\t\t{bath_entry.get()}\t\t\t{soapPrice} RS\n")
        if facecream_entry.get()!="0":
            textarea.insert(END,f"Face Cream\t\t\t{facecream_entry.get()}\t\t\t{facecreamPrice} RS\n") 
        if facewash_entry.get()!="0":
            textarea.insert(END,f"Face Wash\t\t\t{facewash_entry.get()}\t\t\t{facewashPrice} RS\n") 
        if hairspray_entry.get()!="0":
            textarea.insert(END,f"Hair Spray\t\t\t{hairspray_entry.get()}\t\t\t{hairsprayPrice} RS\n")
        if hairgel_entry.get()!="0":
            textarea.insert(END,f"Hair Gel\t\t\t{hairgel_entry.get()}\t\t\t{hairgelPrice} RS\n")
        if bodylotion_entry.get()!="0":
            textarea.insert(END,f"Body Lotion\t\t\t{bodylotion_entry.get()}\t\t\t{bodylotionPrice} RS\n")

    # grocery text
        if Rice_entry.get()!="0":
            textarea.insert(END,f"Rice\t\t\t{Rice_entry.get()}\t\t\t{ricePrice} RS\n")
        if oil_entry.get()!="0":
            textarea.insert(END,f"Oil\t\t\t{oil_entry.get()}\t\t\t{oilPrice} RS\n")
        if Daal_entry.get()!="0":
            textarea.insert(END,f"Daal\t\t\t{Daal_entry.get()}\t\t\t{dallPrice} RS\n")
        if Wheat_entry.get()!="0":
            textarea.insert(END,f"Wheat\t\t\t{Wheat_entry.get()}\t\t\t{wheatPrice} RS\n")
        if Sugar_entry.get()!="0":
            textarea.insert(END,f"Sugar\t\t\t{Sugar_entry.get()}\t\t\t{sugaarPrice} RS\n")
        if Tea_entry.get()!="0":
            textarea.insert(END,f"Tea\t\t\t{Tea_entry.get()}\t\t\t{teaPrice} RS\n")
        
    # cold drinks text

        if Maaza_entry.get()!="0":
            textarea.insert(END,f"Maaza\t\t\t{Maaza_entry.get()}\t\t\t{maazaPrice} RS\n")
        if Pepsi_entry.get()!="0":
            textarea.insert(END,f"Pepsi\t\t\t{Pepsi_entry.get()}\t\t\t{pepsiPrice} RS\n")
        if Sprite_entry.get()!="0":
            textarea.insert(END,f"Sprite\t\t\t{Sprite_entry.get()}\t\t\t{spritePrice} RS\n")
        if Dew_entry.get()!="0":
            textarea.insert(END,f"Dew\t\t\t{Dew_entry.get()}\t\t\t{dewprice} RS\n")
        if Frooti_entry.get()!="0":
            textarea.insert(END,f"Frooti\t\t\t{Frooti_entry.get()}\t\t\t{frootiPrice} RS\n")
        if Coca_Cola_entry.get()!="0":
            textarea.insert(END,f"Coco Cola\t\t\t{Coca_Cola_entry.get()}\t\t\t{cocaColaPrice} RS\n")
        textarea.insert(END,"------------------------------------------------------------\n")

    #  tax area 
        if Cosmetictax_entry.get()!="0.0 RS":
            textarea.insert(END,f"Cosmetic Tax\t\t\t\t{Cosmetictax_entry.get()}\n")
        if grocerytax_entry.get()!="0.0 RS":
            textarea.insert(END,f"Grocery Tax\t\t\t\t{grocerytax_entry.get()}\n")
        if Colddrinktax_entry.get()!="0.0 RS":
            textarea.insert(END,f"Cold Drinks Tax\t\t\t\t{Colddrinktax_entry.get()}\n")

        textarea.insert(END,f"\nTotal Bill\t\t\t\t{totalbill:.3f} RS\n")
        textarea.insert(END,"------------------------------------------------------------\n")
        save_bill()
    
    

def total():
    global soapPrice, facecreamPrice, facewashPrice, hairsprayPrice, hairgelPrice, bodylotionPrice
    global maazaPrice, pepsiPrice, spritePrice, dewprice, frootiPrice, cocaColaPrice
    global ricePrice, oilPrice, dallPrice, wheatPrice, sugaarPrice, teaPrice
    global totalbill, total_amount_for_payment

    # Calculate prices for cosmetics
    soapPrice = int(bath_entry.get()) * 20
    facecreamPrice = int(facecream_entry.get()) * 99
    facewashPrice = int(facewash_entry.get()) * 99
    hairsprayPrice = int(hairspray_entry.get()) * 121
    hairgelPrice = int(hairgel_entry.get()) * 59
    bodylotionPrice = int(bodylotion_entry.get()) * 199

    totalcosmeticPrice = soapPrice + facecreamPrice + facewashPrice + hairsprayPrice + hairgelPrice + bodylotionPrice
    Cosmeticprice_entry.delete(0, END)
    Cosmeticprice_entry.insert(0, f"{totalcosmeticPrice} RS")
    cosmeticstax = totalcosmeticPrice * 0.12
    Cosmetictax_entry.delete(0, END)
    Cosmetictax_entry.insert(0, f"{cosmeticstax:.3f} RS")

    # Calculate prices for groceries
    ricePrice = int(Rice_entry.get()) * 60
    oilPrice = int(oil_entry.get()) * 160
    dallPrice = int(Daal_entry.get()) * 145
    wheatPrice = int(Wheat_entry.get()) * 29
    sugaarPrice = int(Sugar_entry.get()) * 45
    teaPrice = int(Tea_entry.get()) * 10

    totalgroceryPrice = ricePrice + oilPrice + dallPrice + wheatPrice + sugaarPrice + teaPrice
    groceryprice_entry.delete(0, END)
    groceryprice_entry.insert(0, f"{totalgroceryPrice} RS")
    grocerytax = totalgroceryPrice * 0.05
    grocerytax_entry.delete(0, END)
    grocerytax_entry.insert(0, f"{grocerytax:.3f} RS")

    # Calculate prices for cold drinks
    maazaPrice = int(Maaza_entry.get()) * 90
    pepsiPrice = int(Pepsi_entry.get()) * 50
    spritePrice = int(Sprite_entry.get()) * 50
    dewprice = int(Dew_entry.get()) * 50
    frootiPrice = int(Frooti_entry.get()) * 10
    cocaColaPrice = int(Coca_Cola_entry.get()) * 30

    totalcolddrinckprice = maazaPrice + pepsiPrice + spritePrice + dewprice + frootiPrice + cocaColaPrice
    Colddrinkprice_entry.delete(0, END)
    Colddrinkprice_entry.insert(0, f"{totalcolddrinckprice} RS")
    colddrinkstax = totalcolddrinckprice * 0.08
    Colddrinktax_entry.delete(0, END)
    Colddrinktax_entry.insert(0, f"{colddrinkstax:.3f} RS")

    # Calculate total bill
    totalbill = totalcosmeticPrice + totalgroceryPrice + totalcolddrinckprice + cosmeticstax + grocerytax + colddrinkstax
    total_amount_for_payment = totalbill  # Save for QR code generation

def clear():
    # List of entry fields to clear and reset
    cosmetic_entries = [
        bath_entry, facecream_entry, facewash_entry,
        hairspray_entry, hairgel_entry, bodylotion_entry
    ]
    
    grocery_entries = [
        Rice_entry, oil_entry, Daal_entry,
        Wheat_entry, Sugar_entry, Tea_entry
    ]
    
    cold_drink_entries = [
        Maaza_entry, Pepsi_entry, Sprite_entry,
        Dew_entry, Frooti_entry, Coca_Cola_entry
    ]
    
    # Clear cosmetic entries
    for entry in cosmetic_entries:
        entry.delete(0, END)
        entry.insert(0, 0)

    # Clear grocery entries
    for entry in grocery_entries:
        entry.delete(0, END)
        entry.insert(0, 0)

    # Clear cold drink entries
    for entry in cold_drink_entries:
        entry.delete(0, END)
        entry.insert(0, 0)

    # Clear customer details
    name_entry.delete(0, END)
    phone_entry.delete(0, END)

    # Clear price and tax entries
    price_tax_entries = [
        Cosmeticprice_entry, groceryprice_entry,
        Colddrinkprice_entry, Cosmetictax_entry,
        grocerytax_entry, Colddrinktax_entry
    ]
    
    for entry in price_tax_entries:
        entry.delete(0, END)

    # Clear the textarea
    textarea.delete(1.0, END)




def generate_qr(payment_window):
    global total_amount_for_payment
    global img  

    upi_id = "aftablamkhan8932@oksbi"
    payment_amount = total_amount_for_payment  

    upi_link = f"upi://pay?pa={upi_id}&pn=AftabAlam&am={payment_amount}&cu=INR"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("payment_qr.png")

    # Display the QR code
    qr_window = Toplevel()
    qr_window.title("QR Code for Payment")
    qr_window.geometry("300x300")
    qr_window.config(bg="gray20")

    img = Image.open("payment_qr.png")
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    Label(qr_window, text="Scan to Pay", font=("arial", 20, "bold"), bg="gray20", fg="white").pack(pady=10)
    Label(qr_window, image=img, bg="gray20").pack()

    # Close payment options window when QR code is generated
    payment_window.destroy()

    # Button to simulate payment success
    Button(qr_window, text="Payment Successful", command=lambda: payment_success(qr_window)).pack(pady=10)

def payment_success(qr_window):
    qr_window.destroy()  # Close the QR window
    textarea.insert(END, "Payment Successful!\n")
    save_bill()  # Save the bill data to the database

def payment_option():
    global root1
    root1 = Tk()
    root1.title("Payment Options")
    root.iconbitmap()
    root1.geometry("600x400")
    root1.config(bg="gray20")
    root1.resizable(0, 0)

    Label(root1, text="Choose Payment Option", font=("arial", 20, "bold"), bg="gray20", fg="white").pack(pady=20)

    Button(root1, text="Cash Payment", font=("arial", 16), width=20, command=bill_area).pack(pady=30)
    Button(root1, text="Online Payment", font=("arial", 16), width=20, command=lambda: generate_qr(root1)).pack(pady=30)

    root1.mainloop()






# GUI 
root =Tk()
root.title("Retail Billing System")
icon="Billing Software/Retail.ico"
root.iconbitmap(icon)
root.geometry("1380x690")
root.resizable(False,False)

# Heading Label
headinglabel =Label(root,text=("Retail Billing System"),font=("times new roman", 30, "bold"),bg="blue",fg="gold",bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

# customer Details.............

customerdetails =LabelFrame(root,text="Customer Details",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="blue")
customerdetails.pack(fill=X,pady=10)

name_label =Label(customerdetails,text="Name",font=("times new roman", 15, "bold"),bg="blue",fg="white")
name_label.grid(row=0,column=0,padx=20)

name_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
name_entry.grid(row=0,column=1,padx=8)

phone_label =Label(customerdetails,text="Phone Number",font=("times new roman", 15, "bold"),bg="blue",fg="white")
phone_label.grid(row=0,column=2,padx=8,pady=2)

phone_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
phone_entry.grid(row=0,column=3,padx=8)

billnumber_label =Label(customerdetails,text="Bill Number",font=("times new roman", 15, "bold"),bg="blue",fg="white")
billnumber_label.grid(row=0,column=4,padx=10,pady=2)

bill_number_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
bill_number_entry.grid(row=0,column=5,padx=10)

search_btn=Button(customerdetails,text="SEARCH",font=("arial", 12, "bold"),bg="white",fg="gray20",bd=7,width=10,command=search_bill)
search_btn.grid(row=0,column=6,padx=35,pady=8)

# Products  Details
products_details=Frame(root)
products_details.pack(fill=X)

cosmetics_label=LabelFrame(products_details,text="Cosmetics",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="blue")
cosmetics_label.grid(row=0,column=0)

bathsoap=Label(cosmetics_label,text="Bath Soap",font=("times new roman", 15,"bold"),bg="blue",fg="white")
bathsoap.grid(row=0,column=0,pady=8,padx=10)

bath_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
bath_entry.grid(row=0,column=1,pady=8,padx=10)
bath_entry.insert(0,0)

facecream=Label(cosmetics_label,text="Face Cream",font=("times new roman", 15,"bold"),bg="blue",fg="white")
facecream.grid(row=1,column=0,pady=8,padx=10)

facecream_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
facecream_entry.grid(row=1,column=1,pady=8,padx=10)
facecream_entry.insert(0,0)

facewash=Label(cosmetics_label,text="Face Wash",font=("times new roman", 15,"bold"),bg="blue",fg="white")
facewash.grid(row=2,column=0,pady=8)

facewash_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
facewash_entry.grid(row=2,column=1,pady=8)
facewash_entry.insert(0,0)

hairspray=Label(cosmetics_label,text="Hair Spray",font=("times new roman", 15,"bold"),bg="blue",fg="white")
hairspray.grid(row=3,column=0,pady=8)

hairspray_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
hairspray_entry.grid(row=3,column=1,pady=8)
hairspray_entry.insert(0,0)

hairgel=Label(cosmetics_label,text="Hair Gel",font=("times new roman", 15,"bold"),bg="blue",fg="white")
hairgel.grid(row=4,column=0,pady=8)

hairgel_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
hairgel_entry.grid(row=4,column=1,pady=8)
hairgel_entry.insert(0,0)

bodylotion=Label(cosmetics_label,text="Body Lotion",font=("times new roman", 15,"bold"),bg="blue",fg="white")
bodylotion.grid(row=5,column=0,pady=8)

bodylotion_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
bodylotion_entry.grid(row=5,column=1,pady=8)
bodylotion_entry.insert(0,0)

# Grocery Details
grocery_details=LabelFrame(products_details,text="Grocery",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="blue")
grocery_details.grid(row=0,column=2)

Rice=Label(grocery_details,text="Rice",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Rice.grid(row=0,column=2,pady=8,padx=10)

Rice_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Rice_entry.grid(row=0,column=3,pady=8,padx=10)
Rice_entry.insert(0,0)

Oil=Label(grocery_details,text="Oil",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Oil.grid(row=1,column=2,pady=8,padx=10)

oil_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
oil_entry.grid(row=1,column=3,pady=8,padx=10)
oil_entry.insert(0,0)

Daal=Label(grocery_details,text="Daal",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Daal.grid(row=2,column=2,pady=8,padx=10)

Daal_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Daal_entry.grid(row=2,column=3,pady=8,padx=10)
Daal_entry.insert(0,0)

Wheat=Label(grocery_details,text="Wheat",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Wheat.grid(row=3,column=2,pady=8,padx=10)

Wheat_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Wheat_entry.grid(row=3,column=3,pady=8,padx=10)
Wheat_entry.insert(0,0)

Sugar=Label(grocery_details,text="Sugar",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Sugar.grid(row=4,column=2,pady=8,padx=10)

Sugar_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Sugar_entry.grid(row=4,column=3,pady=8,padx=10)
Sugar_entry.insert(0,0)

Tea=Label(grocery_details,text="Tea",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Tea.grid(row=5,column=2,pady=8,padx=10)

Tea_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Tea_entry.grid(row=5,column=3,pady=8,padx=10)
Tea_entry.insert(0,0)

# Cold Drinks

coldDrinks=LabelFrame(products_details,text="Cold Drinks",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="blue")
coldDrinks.grid(row=0,column=4)

Maaza=Label(coldDrinks,text="Maaza",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Maaza.grid(row=0,column=4,pady=8,padx=10)

Maaza_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Maaza_entry.grid(row=0,column=5,pady=8,padx=10)
Maaza_entry.insert(0,0)

Pepsi=Label(coldDrinks,text="Pepsi",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Pepsi.grid(row=1,column=4,pady=8,padx=10)

Pepsi_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Pepsi_entry.grid(row=1,column=5,pady=8,padx=10)
Pepsi_entry.insert(0,0)

Sprite=Label(coldDrinks,text="Sprite",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Sprite.grid(row=2,column=4,pady=8,padx=10)

Sprite_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Sprite_entry.grid(row=2,column=5,pady=8,padx=10)
Sprite_entry.insert(0,0)

Dew=Label(coldDrinks,text="Dew",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Dew.grid(row=3,column=4,pady=8,padx=10)

Dew_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Dew_entry.grid(row=3,column=5,pady=8,padx=10)
Dew_entry.insert(0,0)

Frooti=Label(coldDrinks,text="Frooti",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Frooti.grid(row=4,column=4,pady=8,padx=10)

Frooti_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Frooti_entry.grid(row=4,column=5,pady=8,padx=10)
Frooti_entry.insert(0,0)

Coca_Cola=Label(coldDrinks,text="Coco Cola",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Coca_Cola.grid(row=5,column=4,pady=8,padx=10)

Coca_Cola_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Coca_Cola_entry.grid(row=5,column=5,pady=8,padx=10)
Coca_Cola_entry.insert(0,0)

# Bill Area 
billframe=Frame(products_details,bd=6,relief=GROOVE)
billframe.grid(row=0,column=5,padx=10)

billarealabel=Label(billframe,text="Bill Area",font=("times new roman", 18,"bold"),bd=5,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=16,width=74,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# bill Menu 

Billmenu=LabelFrame(root,text="Bill Menu",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="blue")
Billmenu.pack(fill=X,pady=10)

Cosmeticprice=Label(Billmenu,text="Cosmetic Price",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Cosmeticprice.grid(row=0,column=0,pady=8,padx=10)

Cosmeticprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Cosmeticprice_entry.grid(row=0,column=1,pady=8,padx=10)
# Cosmeticprice_entry.insert(0,0)

groceryprice=Label(Billmenu,text="Grocery Price",font=("times new roman", 15,"bold"),bg="blue",fg="white")
groceryprice.grid(row=1,column=0,pady=8,padx=10)

groceryprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
groceryprice_entry.grid(row=1,column=1,pady=8,padx=10)
# groceryprice_entry.insert(0,0)

Colddrinkprice=Label(Billmenu,text="Cold Drink Price",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Colddrinkprice.grid(row=2,column=0,pady=8,padx=10)

Colddrinkprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Colddrinkprice_entry.grid(row=2,column=1,pady=8,padx=10)
# Colddrinkprice_entry.insert(0,0)

Cosmetictax=Label(Billmenu,text="Cosmetic Tax",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Cosmetictax.grid(row=0,column=2,pady=8,padx=10)

Cosmetictax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Cosmetictax_entry.grid(row=0,column=3,pady=8,padx=10)
# Cosmetictax_entry.insert(0,0)

grocerytax=Label(Billmenu,text="Grocery Tax",font=("times new roman", 15,"bold"),bg="blue",fg="white")
grocerytax.grid(row=1,column=2,pady=8,padx=10)

grocerytax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
grocerytax_entry.grid(row=1,column=3,pady=8,padx=10)
# grocerytax_entry.insert(0,0)

Colddrinktax=Label(Billmenu,text="Cold Drink Tax",font=("times new roman", 15,"bold"),bg="blue",fg="white")
Colddrinktax.grid(row=2,column=2,pady=8,padx=10)

Colddrinktax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Colddrinktax_entry.grid(row=2,column=3,pady=8,padx=10)
# Colddrinktax_entry.insert(0,0)

# Button Frame
buttonFrame=Frame(Billmenu,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=10)

Totalbtn=Button(buttonFrame,text="Total",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=total)
Totalbtn.grid(row=0,column=0,pady=20,padx=5)

paidbtn=Button(buttonFrame,text="Pay",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=payment_option)
paidbtn.grid(row=0,column=1,pady=20,padx=5)

billbtn=Button(buttonFrame,text="Bill",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=bill_area)
billbtn.grid(row=0,column=2,pady=20,padx=5)

emailbtn=Button(buttonFrame,text="Email",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=email_bill)
emailbtn.grid(row=0,column=3,pady=20,padx=5)

Printbtn=Button(buttonFrame,text="Print",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=print_bill)
Printbtn.grid(row=0,column=4,pady=20,padx=5)

Clearbtn=Button(buttonFrame,text="Clear",font=("arial 16 bold"),bg="blue",fg="white",bd=5,width=8,pady=10,command=clear)
Clearbtn.grid(row=0,column=5,pady=20,padx=5)

create_database()
create_table_CUSTOMER_DETAILS()
create_table_cosmetics()
create_table_grocery()
create_table_cold_drinks()

root.mainloop()
