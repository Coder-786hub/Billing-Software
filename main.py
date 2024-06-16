from tkinter import * 
from tkinter import messagebox
import random,os,tempfile,smtplib,mysql.connector
from mysql.connector import Error
# Functionalaty

def email_bill():
    def send_gmail():
        try:
            ob=smtplib.SMTP("smtp.gmail.com",587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),receiverEntry.get(),message)
            ob.quit()
            messagebox.showinfo("Success","Bill is successfully sent",parent=root1)
        except:
            messagebox.showerror("Error","Something went wrong Please try again",parent=root1)
    if textarea.get(1.0,END)==('\n'):
        messagebox.showerror("Error","Bill is empty")
    else:
        root1=Toplevel()
        root1.title("Send Gmail")
        root1.config(bg="gray20")
        root1.resizable(0,0)


        senderFrame=LabelFrame(root1,text="SENDER",font=("arial",16,"bold"),bd=6,bg="gray20",fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=("arial",14,"bold"),bg="gray20",fg="white")
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=("arial",16,"bold"),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=10)

        passwordLabel=Label(senderFrame,text="Password'",font=("arial",14,"bold"),bg="gray20",fg="white")
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=("arial",16,"bold"),bd=2,width=23,relief=RIDGE,fg="black",show="*")
        passwordEntry.grid(row=1,column=1,padx=10,pady=10)


        receipentFrame=LabelFrame(root1,text="RECIPIENT",font=("arial",16,"bold"),bd=6,bg="gray20",fg='white')
        receipentFrame.grid(row=1,column=0,padx=40,pady=20)

        ReceiverLabel=Label(receipentFrame,text="Email Address",font=("arial",14,"bold"),bg="gray20",fg="white")
        ReceiverLabel.grid(row=0,column=0,padx=10,pady=8)

        receiverEntry=Entry(receipentFrame,font=("arial",16,"bold"),bd=2,width=23,relief=RIDGE,fg="black")
        receiverEntry.grid(row=0,column=1,padx=10,pady=10)

        messageLabel=Label(receipentFrame,text="Message ",font=("arial",14,"bold"),bg="gray20",fg="white")
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(receipentFrame,font=("arial",14,"bold"),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace("=",'').replace('-','').replace("\t\t\t","\t\t"))

        sendbutton=Button(root1,text="SEND",font=("arial",16,"bold"),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)

        root.mainloop()


  
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
    result =messagebox.askyesno("Confirm","Do you want to save the bill?")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f"Bills/{billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"Bill Number {billnumber} is saved succcessfully")
        billnumber=random.randint(1,1000)


billnumber=random.randint(1,1000)
 

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
    
    global soapPrice,facecreamPrice,facewashPrice,hairsprayPrice,hairgelPrice,bodylotionPrice
    global maazaPrice,pepsiPrice,spritePrice,dewprice,frootiPrice,cocaColaPrice
    global ricePrice,oilPrice,dallPrice,wheatPrice,sugaarPrice,teaPrice
    global totalbill
    global name_entry

    soapPrice=int(bath_entry.get())*20
    facecreamPrice=int(facecream_entry.get())*99
    facewashPrice=int(facewash_entry.get())*99
    hairsprayPrice=int(hairspray_entry.get())*121
    hairgelPrice=int(hairgel_entry.get())*59
    bodylotionPrice=int(bodylotion_entry.get())*199

    totalcosmeticPrice= soapPrice+facecreamPrice+facewashPrice+hairsprayPrice+hairgelPrice+bodylotionPrice
    Cosmeticprice_entry.delete(0,END)
    Cosmeticprice_entry.insert(0,f"{totalcosmeticPrice} RS")
    cosmeticstax=totalcosmeticPrice*0.12
    Cosmetictax_entry.delete(0,END)
    Cosmetictax_entry.insert(0,f"{cosmeticstax} RS")
    
# Grocery Total

    
    ricePrice=int(Rice_entry.get())*60
    oilPrice=int(oil_entry.get())*160
    dallPrice=int(Daal_entry.get())*145
    wheatPrice=int(Wheat_entry.get())*29
    sugaarPrice=int(Sugar_entry.get())*45
    teaPrice=int(Tea_entry.get())*10

    totalgroceryPrice= ricePrice+oilPrice+dallPrice+wheatPrice+sugaarPrice+teaPrice
    groceryprice_entry.delete(0,END)
    groceryprice_entry.insert(0,f"{totalgroceryPrice}  RS")
    grocerytax =totalgroceryPrice*0.05
    grocerytax_entry.delete(0,END)
    grocerytax_entry.insert(0,f"{grocerytax} RS")

    
# Cold Drinks Total
    
    maazaPrice=int(Maaza_entry.get())*90
    pepsiPrice=int(Pepsi_entry.get())*50
    spritePrice=int(Sprite_entry.get())*50
    dewprice=int(Dew_entry.get())*50
    frootiPrice=int(Frooti_entry.get())*10
    cocaColaPrice=int(Coca_Cola_entry.get())*30

    totalcolddrinckprice= maazaPrice+pepsiPrice+spritePrice+dewprice+frootiPrice+cocaColaPrice
    Colddrinkprice_entry.delete(0,END)
    Colddrinkprice_entry.insert(0,f"{totalcolddrinckprice} RS")
    colddrinkstax=totalcolddrinckprice* 0.08
    Colddrinktax_entry.delete(0,END)
    Colddrinktax_entry.insert(0,f"{colddrinkstax} RS")

    totalbill = totalcosmeticPrice + totalgroceryPrice + totalcolddrinckprice + cosmeticstax + grocerytax + colddrinkstax
    # totalbill = f"{totalbill} RS"

def clear():
    bath_entry.delete(0, END)
    bath_entry.insert(0, 0)
    facecream_entry.delete(0, END)
    facecream_entry.insert(0, 0)
    facewash_entry.delete(0, END)
    facewash_entry.insert(0, 0)
    hairspray_entry.delete(0, END)
    hairspray_entry.insert(0, 0)
    hairgel_entry.delete(0, END)
    hairgel_entry.insert(0, 0)
    bodylotion_entry.delete(0, END)
    bodylotion_entry.insert(0, 0)

    Rice_entry.delete(0, END)
    Rice_entry.insert(0, 0)
    oil_entry.delete(0, END)
    oil_entry.insert(0, 0)
    Daal_entry.delete(0, END)
    Daal_entry.insert(0, 0)
    Wheat_entry.delete(0, END)
    Wheat_entry.insert(0, 0)
    Sugar_entry.delete(0, END)
    Sugar_entry.insert(0, 0)
    Tea_entry.delete(0, END)
    Tea_entry.insert(0, 0)

    Maaza_entry.delete(0, END)
    Maaza_entry.insert(0, 0)
    Pepsi_entry.delete(0, END)
    Pepsi_entry.insert(0, 0)
    Sprite_entry.delete(0, END)
    Sprite_entry.insert(0, 0)
    Dew_entry.delete(0, END)
    Dew_entry.insert(0, 0)
    Frooti_entry.delete(0, END)
    Frooti_entry.insert(0, 0)
    Coca_Cola_entry.delete(0, END)
    Coca_Cola_entry.insert(0, 0)

    name_entry.delete(0, END)
    phone_entry.delete(0, END)

    Cosmeticprice_entry.delete(0, END)
    groceryprice_entry.delete(0, END)
    Colddrinkprice_entry.delete(0, END)
    Cosmetictax_entry.delete(0, END)
    grocerytax_entry.delete(0, END)
    Colddrinktax_entry.delete(0, END)

    textarea.delete(1.0, END)


# GUI 
root =Tk()
root.title("Retail Billing System")
root.iconbitmap()
root.geometry("1270x685")
root.resizable(False,False)

# Heading Label
headinglabel =Label(root,text=("Retail Billing System"),font=("times new roman", 30, "bold"),bg="gray20",fg="gold",bd=12,relief=GROOVE)
headinglabel.pack(fill=X)

# customer Details.............

customerdetails =LabelFrame(root,text="Customer Details",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
customerdetails.pack(fill=X,pady=10)

name_label =Label(customerdetails,text="Name",font=("times new roman", 15, "bold"),bg="gray20",fg="white")
name_label.grid(row=0,column=0,padx=20)

name_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
name_entry.grid(row=0,column=1,padx=8)

phone_label =Label(customerdetails,text="Phone Number",font=("times new roman", 15, "bold"),bg="gray20",fg="white")
phone_label.grid(row=0,column=2,padx=8,pady=2)

phone_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
phone_entry.grid(row=0,column=3,padx=8)

billnumber_label =Label(customerdetails,text="Bill Number",font=("times new roman", 15, "bold"),bg="gray20",fg="white")
billnumber_label.grid(row=0,column=4,padx=10,pady=2)

bill_number_entry =Entry(customerdetails,font=("arial 15"),bd=7,width=18)
bill_number_entry.grid(row=0,column=5,padx=10)

search_btn=Button(customerdetails,text="SEARCH",font=("arial", 12, "bold"),bg="white",fg="gray20",bd=7,width=10,command=search_bill)
search_btn.grid(row=0,column=6,padx=35,pady=8)

# Products  Details
products_details=Frame(root)
products_details.pack(fill=X)

cosmetics_label=LabelFrame(products_details,text="Cosmetics",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
cosmetics_label.grid(row=0,column=0)

bathsoap=Label(cosmetics_label,text="Bath Soap",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
bathsoap.grid(row=0,column=0,pady=8,padx=10)

bath_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
bath_entry.grid(row=0,column=1,pady=8,padx=10)
bath_entry.insert(0,0)

facecream=Label(cosmetics_label,text="Face Cream",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
facecream.grid(row=1,column=0,pady=8,padx=10)

facecream_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
facecream_entry.grid(row=1,column=1,pady=8,padx=10)
facecream_entry.insert(0,0)

facewash=Label(cosmetics_label,text="Face Wash",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
facewash.grid(row=2,column=0,pady=8)

facewash_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
facewash_entry.grid(row=2,column=1,pady=8)
facewash_entry.insert(0,0)

hairspray=Label(cosmetics_label,text="Hair Spray",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
hairspray.grid(row=3,column=0,pady=8)

hairspray_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
hairspray_entry.grid(row=3,column=1,pady=8)
hairspray_entry.insert(0,0)

hairgel=Label(cosmetics_label,text="Hair Gel",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
hairgel.grid(row=4,column=0,pady=8)

hairgel_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
hairgel_entry.grid(row=4,column=1,pady=8)
hairgel_entry.insert(0,0)

bodylotion=Label(cosmetics_label,text="Body Lotion",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
bodylotion.grid(row=5,column=0,pady=8)

bodylotion_entry =Entry(cosmetics_label,font=("arial 12"),bd=5,width=10)
bodylotion_entry.grid(row=5,column=1,pady=8)
bodylotion_entry.insert(0,0)

# Grocery Details
grocery_details=LabelFrame(products_details,text="Grocery",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
grocery_details.grid(row=0,column=2)

Rice=Label(grocery_details,text="Rice",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Rice.grid(row=0,column=2,pady=8,padx=10)

Rice_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Rice_entry.grid(row=0,column=3,pady=8,padx=10)
Rice_entry.insert(0,0)

Oil=Label(grocery_details,text="Oil",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Oil.grid(row=1,column=2,pady=8,padx=10)

oil_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
oil_entry.grid(row=1,column=3,pady=8,padx=10)
oil_entry.insert(0,0)

Daal=Label(grocery_details,text="Daal",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Daal.grid(row=2,column=2,pady=8,padx=10)

Daal_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Daal_entry.grid(row=2,column=3,pady=8,padx=10)
Daal_entry.insert(0,0)

Wheat=Label(grocery_details,text="Wheat",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Wheat.grid(row=3,column=2,pady=8,padx=10)

Wheat_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Wheat_entry.grid(row=3,column=3,pady=8,padx=10)
Wheat_entry.insert(0,0)

Sugar=Label(grocery_details,text="Sugar",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Sugar.grid(row=4,column=2,pady=8,padx=10)

Sugar_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Sugar_entry.grid(row=4,column=3,pady=8,padx=10)
Sugar_entry.insert(0,0)

Tea=Label(grocery_details,text="Tea",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Tea.grid(row=5,column=2,pady=8,padx=10)

Tea_entry =Entry(grocery_details,font=("arial 12"),bd=5,width=10)
Tea_entry.grid(row=5,column=3,pady=8,padx=10)
Tea_entry.insert(0,0)

# Cold Drinks

coldDrinks=LabelFrame(products_details,text="Cold Drinks",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
coldDrinks.grid(row=0,column=4)

Maaza=Label(coldDrinks,text="Maaza",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Maaza.grid(row=0,column=4,pady=8,padx=10)

Maaza_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Maaza_entry.grid(row=0,column=5,pady=8,padx=10)
Maaza_entry.insert(0,0)

Pepsi=Label(coldDrinks,text="Pepsi",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Pepsi.grid(row=1,column=4,pady=8,padx=10)

Pepsi_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Pepsi_entry.grid(row=1,column=5,pady=8,padx=10)
Pepsi_entry.insert(0,0)

Sprite=Label(coldDrinks,text="Sprite",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Sprite.grid(row=2,column=4,pady=8,padx=10)

Sprite_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Sprite_entry.grid(row=2,column=5,pady=8,padx=10)
Sprite_entry.insert(0,0)

Dew=Label(coldDrinks,text="Dew",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Dew.grid(row=3,column=4,pady=8,padx=10)

Dew_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Dew_entry.grid(row=3,column=5,pady=8,padx=10)
Dew_entry.insert(0,0)

Frooti=Label(coldDrinks,text="Frooti",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Frooti.grid(row=4,column=4,pady=8,padx=10)

Frooti_entry =Entry(coldDrinks,font=("arial 12"),bd=5,width=10)
Frooti_entry.grid(row=4,column=5,pady=8,padx=10)
Frooti_entry.insert(0,0)

Coca_Cola=Label(coldDrinks,text="Coco Cola",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
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
textarea=Text(billframe,height=16,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# bill Menu 

Billmenu=LabelFrame(root,text="Bill Menu",font=("times new roman", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
Billmenu.pack(fill=X,pady=10)

Cosmeticprice=Label(Billmenu,text="Cosmetic Price",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Cosmeticprice.grid(row=0,column=0,pady=8,padx=10)

Cosmeticprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Cosmeticprice_entry.grid(row=0,column=1,pady=8,padx=10)
# Cosmeticprice_entry.insert(0,0)

groceryprice=Label(Billmenu,text="Grocery Price",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
groceryprice.grid(row=1,column=0,pady=8,padx=10)

groceryprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
groceryprice_entry.grid(row=1,column=1,pady=8,padx=10)
# groceryprice_entry.insert(0,0)

Colddrinkprice=Label(Billmenu,text="Cold Drink Price",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Colddrinkprice.grid(row=2,column=0,pady=8,padx=10)

Colddrinkprice_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Colddrinkprice_entry.grid(row=2,column=1,pady=8,padx=10)
# Colddrinkprice_entry.insert(0,0)

Cosmetictax=Label(Billmenu,text="Cosmetic Tax",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Cosmetictax.grid(row=0,column=2,pady=8,padx=10)

Cosmetictax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Cosmetictax_entry.grid(row=0,column=3,pady=8,padx=10)
# Cosmetictax_entry.insert(0,0)

grocerytax=Label(Billmenu,text="Grocery Tax",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
grocerytax.grid(row=1,column=2,pady=8,padx=10)

grocerytax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
grocerytax_entry.grid(row=1,column=3,pady=8,padx=10)
# grocerytax_entry.insert(0,0)

Colddrinktax=Label(Billmenu,text="Cold Drink Tax",font=("times new roman", 15,"bold"),bg="gray20",fg="white")
Colddrinktax.grid(row=2,column=2,pady=8,padx=10)

Colddrinktax_entry =Entry(Billmenu,font=("arial 12"),bd=5,width=10)
Colddrinktax_entry.grid(row=2,column=3,pady=8,padx=10)
# Colddrinktax_entry.insert(0,0)

# Button Frame
buttonFrame=Frame(Billmenu,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=10)

Totalbtn=Button(buttonFrame,text="Total",font=("arial 16 bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=total)
Totalbtn.grid(row=0,column=0,pady=20,padx=5)

billbtn=Button(buttonFrame,text="Bill",font=("arial 16 bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=bill_area)
billbtn.grid(row=0,column=1,pady=20,padx=5)

emailbtn=Button(buttonFrame,text="Email",font=("arial 16 bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=email_bill)
emailbtn.grid(row=0,column=2,pady=20,padx=5)

Printbtn=Button(buttonFrame,text="Print",font=("arial 16 bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=print_bill)
Printbtn.grid(row=0,column=3,pady=20,padx=5)

Clearbtn=Button(buttonFrame,text="Clear",font=("arial 16 bold"),bg="gray20",fg="white",bd=5,width=8,pady=10,command=clear)
Clearbtn.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()