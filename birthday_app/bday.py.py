from tkinter import*

root=Tk()
root.geometry("600x600")
root.title("welcome")
F=Label(root,text="|                                                                                         |",font=" Times 15 bold", bg="skyblue",fg="skyblue").pack()
L=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
C=Label(root,text=" WELCOME TO BIRTHDAY REMINDER APP ",font=" Times 15 bold").pack()
K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
#K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
K=Label(root,text="|                                                                                         |",font=" Times 15 bold",bg="skyblue",fg="skyblue").pack()
root.configure(background="skyblue")




textname=StringVar()
textdate=StringVar()
textfind=StringVar()


def myf():
    
    l = open("hello.txt","a")
    
    x=str(textname.get())
    l.write(x)
    l.write("--------date :: ")
    y=str(textdate.get())
    l.write(y)
    l.write("\n")
    l.close()
    
      



def addentry():
    
  my=Toplevel()
  my.geometry("500x500")
  my.configure(background="pink")
  
  K=Label(my,text="|                                                                                         |",font=" Times 20 bold",bg="pink",fg="skyblue").pack()
  K=Label(my,text="|                          ENTER NAME AND BIRTH DATE OF YOUR FRIEND                       |",font=" Times 10 bold",bg="pink",fg="brown").pack()
  K=Label(my,text="|                                                                                         |",font=" Times 20 bold",bg="pink",fg="skyblue").pack()
  user=Label(my,text="Enter name of ur friend  :: ").pack()
  K=Label(my,text="|                                                                                         |",font=" Times 5 bold",bg="pink",fg="skyblue").pack()
  userbox=Entry(my,textvariable=textname).pack()
  K=Label(my,text="|                                                                                         |",font=" Times 5 bold",bg="pink",fg="skyblue").pack()

  user=Label(my,text="Enter  bitrh date :: ").pack()
  K=Label(my,text="|                                                                                         |",font=" Times 5 bold",bg="pink",fg="skyblue").pack()
  userdate=Entry(my,textvariable=textdate).pack()
  K=Label(my,text="|                                                                                         |",font=" Times 5 bold",bg="pink",fg="skyblue").pack()
  bt=Button(my,text="submit" , command=myf, font=" Times 10 bold",fg="red").pack()
  
  



def viewentry():
  myred=Toplevel()
  myred.geometry("500x500")
  m=open("hello.txt")
  Label(myred,text=(m.read())).pack()
  m.close()


def tosearch():
  down=Toplevel()
  down.geometry("400x400")
  q=open("hello.txt","r")
  v=str(textfind.get())
  m=q.readlines()
  if v in open("hello.txt").read():
    print(v)
    Label(down,text=v ).pack()
    Label(down ,text="data found !!! you can check it from VIEW ALL ENTRIES").pack()
  else:
    Label(down,text="You dont have any such a entry").pack()
    
   

def find():
  top=Toplevel()
  top.geometry("400x400")
  top.configure(background="grey")


  K=Label(top,text="|                                                                                         |",font=" Times 20 bold",bg="grey",fg="skyblue").pack()
  K=Label(top,text="|                          ENTER NAME or BIRTH DATE OF YOUR FRIEND                        |",font=" Times 10 bold",bg="grey",fg="black").pack()
  K=Label(top,text="|                                                                                         |",font=" Times 20 bold",bg="grey",fg="skyblue").pack()
  user1=Label(top,text="Enter name of ur friend  :: ").pack()
  K=Label(top,text="|                                                                                           |",font=" Times 10 bold",bg="grey",fg="grey").pack()
  userbox1=Entry(top,textvariable=textfind).pack()
  K=Label(top,text="|                                                                                           |",font=" Times 10 bold",bg="grey",fg="grey").pack()

  bt1=Button(top,text="search" , command=tosearch).pack()





K=Label(root,text="_",font=" Times 15 bold",bg="skyblue",fg="red").pack()
K=Label(root,text="|  |",font=" Times 15 bold",bg="skyblue",fg="red").pack()
K=Label(root,text="|  |",font=" Times 15 bold",bg="skyblue",fg="red").pack()
btn=Button(root,text="  INSERT  " ,font=" Times 13 bold", command=addentry).pack()



#btn=Button(root,text="VIEW ALL ENTRIES " ,font=" Times 15 bold", command=viewentry).pack()


btn=Button(root,text="      CHECK   " ,font=" Times 13 bold", command=find).pack()
btn=Button(root,text=" VIEW ALL ENTRIES " ,font=" Times 13 bold", command=viewentry).pack()

root.mainloop()