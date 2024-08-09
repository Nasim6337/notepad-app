from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import askokcancel,showinfo

def new_page():
    textarea.delete('1.0',END)
         

class save_file:   

    var=''
    def op_file(self):
        var=fd.askopenfile(title="open",initialdir="\\",filetypes=(("textfile","*.txt"),("all files","*.*")))
        if var:
            try:
                data=var.read()
                textarea.insert('1.0',data)
                win.title(f"{var.name}   notepad")
            except Exception as e:
                print(e)


    def sv_file(self):
        self.var=fd.asksaveasfile(title="save file",initialdir="\\",filetypes=(("textfile","*.txt"),("all files","*.*")),defaultextension="*.txt")
        data=textarea.get("1.0",END)
        self.var.write(data)
        

    def sv_as(self):
        var2=fd.asksaveasfilename(title="save as file",initialdir=self.var.name,filetypes=(("textfile","*.txt"),("all files","*.*")),defaultextension="*.txt")
        print(self.var)
        data=textarea.get("1.0",END)
        var2.write(data)


class zoom:
    value=21
    def plus(self):
        textarea.config(font=("lucida 13",self.value))
        self.value=self.value+1
     
    def minus(self):
        self.value=self.value-1
        textarea.config(font=("lucida 13",self.value))
        

sv=save_file()
zm=zoom()

def about():
    info=showinfo(title="About this notepad",message="This notepad is developed by Nasim Ali ")




win=Tk()
win.title("Untitled notepad")
win.geometry("700x500")

#file menu start
n_menu=Menu(win)
nm=Menu(n_menu,tearoff=0)
nm.add_command(label="New                           Ctrl+N",command=new_page)
nm.add_command(label="Open                          Ctrl+O",command=sv.op_file)
nm.add_command(label="Save                           Ctrl+S",command=sv.sv_file) 
nm.add_command(label="Save As                      Ctrl+shift+S",command=sv.sv_as)
win.config(menu=n_menu)
n_menu.add_cascade(label="File",menu=nm)
#file menu end here

#Edit menu strat here
em=Menu(n_menu,tearoff=0)
em.add_command(label="Undo                                 Ctrl+Z")
em.add_command(label="Cut                                  Ctrl+X")
em.add_command(label="Copy                                 Ctrl+C")
em.add_command(label="Paste                                Ctrl+V")
em.add_command(label="Delete                                  Del")
n_menu.add_cascade(label="Edit",menu=em)
#edit menu end here



#view menu start here

vm=Menu(n_menu,tearoff=0)
sub_vm=Menu(vm,tearoff=0)
vm.add_cascade(label="zoom",menu=sub_vm)
sub_vm.add_command(label="Zoom in                           ctrl+Plus",command=zm.plus)
sub_vm.add_command(label="Zoom out                          ctrl+minus",command=zm.minus)
vm.add_checkbutton(label="Status Bar")
n_menu.add_cascade(label="View",menu=vm)
#view menu end here

#help menu start here
hm=Menu(n_menu,tearoff=0)
hm.add_command(label="About Notepad  ",command=about)
n_menu.add_cascade(label="About",menu=hm)
#format menu end here

textarea=Text(win,font=("lucida 13",20))
textarea.pack(fill=BOTH,expand=True)
scroll=Scrollbar(textarea,cursor="hand2")
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)



win.mainloop()
