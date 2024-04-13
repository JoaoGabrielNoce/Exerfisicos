import customtkinter
import os
from PIL import Image

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.item_list = []
        self.difficult_list = []
        self.label_list = []
        self.dlabel_list = []
        self.button_list = []

    def add_item(self, item, difficult, txt, image=None):
        label = customtkinter.CTkLabel(self, text=txt, image=image, compound="left", padx=5, anchor="w")
    
        if difficult == 1: 
            label2 = customtkinter.CTkLabel(self, text="Fácil", compound="left", padx=5, anchor="w")
        elif difficult == 2: 
            label2 = customtkinter.CTkLabel(self, text="Médio", compound="left", padx=5, anchor="w")
        elif difficult == 3:
            label2 = customtkinter.CTkLabel(self, text="Difícil", compound="left", padx=5, anchor="w")

        button = customtkinter.CTkButton(self, text="Resolver", width=100, height=24)

        if self.command is not None:
            button.configure(command=lambda: self.command(item))

        label.grid(row=len(self.label_list), column=0, pady=(10, 10), sticky="w")
        label2.grid(row=len(self.dlabel_list), column=1, pady=(10, 10), sticky="w")
        button.grid(row=len(self.button_list), column=2, pady=(10, 10), padx=5)
        
        self.item_list.append(item)
        self.difficult_list.append(difficult)
        self.label_list.append(label)
        self.dlabel_list.append(label2)
        self.button_list.append(button)

    def remove_item(self, item):
        for _item, label, button in zip(self.item_list, self.label_list, self.button_list):
            if item == _item:
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                self.item_list.remove(item)
                return
            
    def sort_items(self):
        zipped_lists = zip(self.difficult_list, self.label_list, self.dlabel_list, self.button_list, self.item_list)
        sorted_pairs = sorted(zipped_lists, key=lambda x: x[0])
        self.difficult_list, self.label_list, self.dlabel_list, self.button_list, self.item_list = zip(*sorted_pairs)

        i = 0
        for _item, label, label2, button in zip(self.item_list, self.label_list, self.dlabel_list, self.button_list):
            label.grid(row=i, column=0, pady=(10, 10), sticky="w")
            label2.grid(row=i, column=1, pady=(10, 10), sticky="w")
            button.grid(row=i, column=2, pady=(10, 10), padx=5)
            i+=1

    def reverse_sort_items(self):

        zipped_lists = zip(self.difficult_list, self.label_list, self.dlabel_list, self.button_list, self.item_list)
        sorted_pairs = sorted(zipped_lists, key=lambda x: x[0],reverse=True)
        self.difficult_list, self.label_list, self.dlabel_list, self.button_list, self.item_list = zip(*sorted_pairs)

        i = 0
        for _item, label, label2, button in zip(self.item_list, self.label_list, self.dlabel_list, self.button_list):
            label.grid(row=i, column=0, pady=(10, 10), sticky="w")
            label2.grid(row=i, column=1, pady=(10, 10), sticky="w")
            button.grid(row=i, column=2, pady=(10, 10), padx=5)
            i+=1
        


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Exercícios de Física")
        self.geometry("1200x700")
        self.resizable(False,False)


        self.label = customtkinter.CTkLabel(master=self, text="Exercícios de Física", fg_color="transparent",font=("Arial",40))
        self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        radiobutton_var = customtkinter.IntVar(value=1)

        radiobutton_1 = customtkinter.CTkRadioButton(master=self, text="Dificuldade ↓", variable=radiobutton_var, value=1, command=self.filter_event)
        radiobutton_1.place(relx=0.78, rely=0.15, anchor=customtkinter.N)

        radiobutton_2 = customtkinter.CTkRadioButton(master=self, text="Dificuldade ↑", variable=radiobutton_var, value=2, command=self.reverse_filter_event)
        radiobutton_2.place(relx=0.88, rely=0.15, anchor=customtkinter.N)

        # Cria menu de exercícios
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=1000, height=500, command=self.label_button_frame_event, 
                                                                        corner_radius=0, label_text="Escolha o exercício que deseja realizar abaixo: ")
        self.scrollable_label_button_frame.place(relx=0.5, rely=0.2, anchor=customtkinter.N)

        i = 0
        while os.path.isfile(os.path.join(current_dir, "exercicios" ,f"{i}.txt")): 
            f = open(os.path.join(current_dir, "exercicios" ,f"{i}.txt"), "r", encoding="utf8")
            difficult = int(f.readline().rstrip())
            title = f.readline().rstrip()
            complete = int(f.readline().rstrip())
            if complete == 0:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_not_done.png"))))
            elif complete == 1:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_done.png"))))
            i += 1
        
        

    def label_button_frame_event(self, item):
        print(f"{item} clicado")
        
    def filter_event(self):
        self.scrollable_label_button_frame.sort_items()

    def reverse_filter_event(self):
        self.scrollable_label_button_frame.reverse_sort_items()


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()