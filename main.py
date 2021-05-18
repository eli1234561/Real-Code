from tkinter import *
from PIL import Image, ImageTk
names = []


class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.

        background_color="OldLace"# to set it as background color for all the label widgets
        background_color="OldLace"
        self.bg_image = PhotoImage(file="road.png") 
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color)
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.

        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0) 
         #label for image
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.grid(row=0, column=1) #on right side


        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=1) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="green", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)        
       
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.quiz_frame.destroy() #Destroy name frame then open the quiz runner
      
           
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz") 
    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear