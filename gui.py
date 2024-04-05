from tkinter import*
import tkinter.messagebox 
from  tkinter import ttk
root=Tk()
#assign variable type
firstname=StringVar()
passwd=StringVar()
cpwd=StringVar()
selectedSeatsArr = []
selectionLable = Label()

# last page of summary
# def summary():
#     check_page=Tk()
#     check_page.title("check the details")
#     check_page.geometry("500x800")
#     username=StringVar()

#     last_frame=Frame(check_page,bg="black",width=800,height=500).place(x=300,y=100)
#     check_page.mainloop()


#function for seat module 
def seat_selection():
            
    seat=Tk()
    seat.geometry("199x250")
        
    # seat.config("#")
    seat.title("seats selection")
    selected_seats_label = Label(seat, text="Selected Seats: None")
    global selectedSeats
    selectedSeats = tkinter.StringVar(seat)

    #show selected seats
    selected_seats_label = tkinter.Label(seat, text="Selected Seats: None")
    selected_seats_label.place(x=25,y=175)
    #colour change of button
   
    def perform(value, button):

        button.config(bg='red',state="disable")  
        selectedSeatsArr.append(value)
        
        

    def updateSeats():
        confirm_button.config(bg='green')
        selected_seats_label.config(text="Selected Seats: " + str(selectedSeatsArr))
        selected_Lab.config(text="Selected Seats: " + str(selectedSeatsArr))
        selectedSeats.set(str(selectedSeatsArr))
        seat.destroy()

    def clear_seat():
        b1.config(bg='blue', state='normal')
        selectedSeatsArr.clear() 
        b2.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b3.config(bg='blue', state='normal')
        selectedSeatsArr.clear() 
        b4.config(bg='blue', state='normal')
        selectedSeatsArr.clear() 
        b5.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b6.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b7.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b8.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b9.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b10.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b11.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b12.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b13.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b14.config(bg='blue', state='normal')
        selectedSeatsArr.clear()
        b15.config(bg='blue', state='normal')
        selectedSeatsArr.clear()



    # def undo():
    #     for button in selectedSeatsArr:
    #         buttons[button].config(bg='SystemButtonFace')  # Reset background color
    #         enable_button(buttons[button])  # Enable the button
    #     selectedSeatsArr.clear()  # Clear the selected seats list


   
        
    
    #driver row   
    Button(seat,text="D").grid(row=0,column=10,columnspan=10)
    # row ---1
    b1 = tkinter.Button(seat,text="1",bg='blue',command=lambda:perform("1",b1))
    b1.grid(row=1,column=0)  
    b2 = tkinter.Button(seat,text="2",bg='blue',command=lambda:perform("2",b2))
    b2.grid(row=1,column=10) 
    b3 = tkinter.Button(seat,text="3",bg='blue',command=lambda:perform("3",b3))
    b3.grid(row=1,column=11)
    #row ---2
    b4 = tkinter.Button(seat,text="4",bg='blue',command=lambda:perform("4",b4))
    b4.grid(row=2,column=0)
    b5 = tkinter.Button(seat,text="5",bg='blue',command=lambda:perform("5",b5))
    b5.grid(row=2,column=10)
    b6 = tkinter.Button(seat,text="6",bg='blue',command=lambda:perform("6",b6))
    b6.grid(row=2,column=11)
    # row ---3
    b7 = tkinter.Button(seat,text="7",bg='blue',command=lambda:perform("7",b7))
    b7.grid(row=3,column=0)
    b8 = tkinter.Button(seat,text="8",bg='blue',command=lambda:perform("8",b8))
    b8.grid(row=3,column=10)
    b9 = tkinter.Button(seat,text="9",bg='blue',command=lambda:perform("9",b9))
    b9.grid(row=3,column=11)
     # row ---4
    b10 = tkinter.Button(seat,text="10",bg='blue',command=lambda:perform("10",b10))
    b10.grid(row=4,column=0)
    b11 = tkinter.Button(seat,text="11",bg='blue',command=lambda:perform("11",b11))
    b11.grid(row=4,column=10)
    b12 = tkinter.Button(seat,text="12",bg='blue',command=lambda:perform("12",b12))
    b12.grid(row=4,column=11)
    #row---5
    b13 = tkinter.Button(seat,text="13",bg='blue',command=lambda:perform("10",b13))
    b13.grid(row=5,column=0)
    b14 = tkinter.Button(seat,text="14",bg='blue',command=lambda:perform("11",b14))
    b14.grid(row=5,column=10)
    b15 = tkinter.Button(seat,text="15",bg='blue',command=lambda:perform("12",b15))
    b15.grid(row=5,column=11)


    # Create a button to print selected seats
    confirm_button = tkinter.Button(seat, text="Confirm Seats", command=updateSeats)
    confirm_button.grid(row=8, column=5, columnspan=7)

    clear_button=tkinter.Button(seat,text="clear",command=clear_seat)
    clear_button.grid(row=8, column=13, columnspan=7)


    seat.mainloop()

# function
def register():
    fname="logindetails.txt"
    # if(selectedSeatsBool == TRUE):
    #     def local_update_lable_two():
    #         selectionLable.config(first,text="Selected Seats: " + str(selectedSeatsArr))

    
    if(len(firstname.get())!=0 and len(passwd.get())!=0 and len(cpwd.get())!=0):
        
        if passwd.get()==cpwd.get():
            with open(fname,'a') as f:
                f.write(f'{firstname.get()},{passwd.get()}')
                tkinter.messagebox.showinfo('Register',"SUCCESSFULLY REGISTERD")
                                
    #    else:
    #        tkinter.messagebox.showinfo('Register',("PASSWORDS ARE NOT MATCHED"))
    # else:
    #         tkinter.messagebox.showinfo('Warning',("Please enter all the Fields"))
                   
    # passenger details page 
        
            first=Tk()
            first.geometry("1380x1900")
            first.title("Travel Details")
            first.config(bg= "#753a88")
   
   
            lab1=Label(first,text="----Passenger Details----",padx=10,pady=18,font="Helvetica 40 italic",bg="#753a88")
            lab1.pack()
            #frame in first
            fra1=Frame(first,bg="black",width=800,height=500).place(x=300,y=100)
            #pickup Label
            pick=StringVar()
            lab2=Label(first,fra1,text="Pickup",textvariable=pick,padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
            lab2.pack()

    #drop down for pickup
            global pickdropvar
            pickdropvar=tkinter.StringVar(first)
            option=['chennai','Tirunelveli','Madurai']
            dm=ttk.OptionMenu(first,pickdropvar,'Select',*option)
            dm.place(x=650,y=150,width=97)

    #label for destination

            lab3=Label(first,fra1,text="Destination",padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
            lab3.place(x=650,y=200)
            #drop down for destination
            global desdropvar
            desdropvar = tkinter.StringVar(first)
            desdropvar.set("none")
            option1=['chennai','Tirunelveli','Madurai']
            dm1=ttk.OptionMenu(first,desdropvar,'Select',*option1)
            dm1.place(x=650,y=250,width=97)

    #spinbox for male & female seat 

            lab4=Label(first,text="Male",padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
            lab4.place(x=500,y=300)
            global sp
            sp=Spinbox(first,from_=0,to=20,width=20)
            sp.place(x=500,y=350)

            lab5=Label(first,text="Female",padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
            lab5.place(x=700,y=300)
            global sp1
            sp1=Spinbox(first,from_=0,to=20,width=20)
            sp1.place(x=700,y=350)

            lab6=Label(first,text="SEATS",padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black").place(x=650,y=400)
            Button(first,text="Select the Seats",font="arial 10 bold",command=seat_selection).place(x=600,y=440)
            Button(first,text="Done",font="arial 10 bold",command=final_Page).place(x=900,y=550)
            #show selected seats
            global selected_Lab
            selected_Lab=tkinter.Label(first,text="Selected Seats: ",padx=10,pady=10,fg="red",font="serif 10 bold italic",bg="black")
            selected_Lab.pack()
            selected_Lab.place(x=650,y=500)

            Button(first,fra1,text="BACK",padx=10,pady=5).place(x=300,y=550)

            first.mainloop()
        else:
            tkinter.messagebox.showinfo('Register',("PASSWORDS ARE NOT MATCHED"))
    else:
            tkinter.messagebox.showinfo('Warning',("Please enter all the Fields"))    


# def calculate():
#     global finalamount
#     finalamount=tkinter.IntVar()
#     final
#     finalamount=len(selectedSeatsArr)*200
#     print(finalamount)

    
    




#finalpage
def final_Page():
    

    if pickdropvar.get() !=desdropvar.get():
        last=Tk()
        last.geometry("1380x1900")
        last.title("Travel Details")
        last.config(bg= "#753a88")
        def calculate():
            global finalamount
            finalamount=tkinter.IntVar()
            finalamount=len(selectedSeatsArr)*200
            final_label.config(text="final amount " + str(finalamount))
           
        def great():
             tkinter.messagebox.showinfo('greatings',("Thank you --your ticket is conformed"))
            
        # print(finalamount)
    
        lab1=Label(last,text="----Booking Details----",padx=10,pady=18,font="Helvetica 40 italic",bg="#753a88")
        lab1.pack()

        #frame in first
        fra1=Frame(last,bg="black",width=800,height=500).place(x=300,y=100)

        #pickup Label
        pick_Lab=Label(last,fra1,text="Pickup: " + pickdropvar.get(),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        pick_Lab.pack()

        #destination Label
        des_Lab=Label(last,fra1,text="Destination: " + desdropvar.get(),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        des_Lab.pack()

        male_Lab=Label(last,text="Male: " + sp.get(),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        male_Lab.pack()

        female_Lab=Label(last,text="Female: " + sp1.get(),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        female_Lab.pack()

        sel_Lab=Label(last,text="Selected Seats: " + selectedSeats.get(),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        sel_Lab.pack()

        tic_Lab=Label(last,text="ticket payment:no.of seats x 200",padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        tic_Lab.pack()

        Button(last,text="calculate",command=calculate).pack()

        final_label=Label(last,text="final amount:" +str(0),padx=10,pady=10,fg="white",font="serif 10 bold italic",bg="black")
        final_label.pack()

        Button(last,text="conform",command=great).pack()

       

        # tkinter.messagebox.showinfo(last,"your ticket amount :"+finalamount.get())

        # Button(last,text="BACK",padx=10,pady=5).place(x=300,y=550)


        last.mainloop()
    else:
        tkinter.messagebox.showinfo('Warning',("Pickup location and drop location are same-check it and make done"))


# root page 
    
root.config(bg= "#753a88")
root.title("login page")

lb=Label(root,text="Book your travel",bg= "#753a88",fg="black",font="Helvetica 40 italic").place(x=590,y=100)

root.geometry("1380x1900")

root.maxsize(2000,2000)
lb1=Label(root,text="USERNAME",bg= "#753a88",font="serif 10 bold italic",padx=20,pady=8).place(x=500,y=205)
Entry(root,font="arial 15 bold",textvariable=firstname).place(x=650,y=210)

lb1=Label(root,text="PASSWORD",bg= "#753a88",font="serif 10 bold italic",padx=20,pady=8).place(x=500,y=255)
Entry(root,show="*",font="arial 15 bold",textvariable=passwd).place(x=650,y=260)

lb1=Label(root,text="CONFORM PWD",bg= "#753a88",font="serif 10 bold italic",padx=20,pady=8).place(x=500,y=305)
Entry(root,show="*",font="arial 15 bold",bg="beige",textvariable=cpwd).place(x=650,y=310)


Button(root,text="Submit",font="arial 10 bold",command=register,padx=150,pady=10).place(x=520,y=370)


root.mainloop()