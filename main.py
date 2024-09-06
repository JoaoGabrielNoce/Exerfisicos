import customtkinter
import os
import math
from PIL import Image

class DialogWindow(customtkinter.CTkToplevel):
    def __init__(self, master, _text, complete, radiobutton_ans_var, radiobutton_ans_1, radiobutton_ans_2, radiobutton_ans_3, radiobutton_ans_4, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x200")
        self.resizable(False,False)
        self.title("Mensagem")
        self.protocol("WM_DELETE_WINDOW", "disable_event")

        self.label = customtkinter.CTkLabel(master=self, text=_text, fg_color="transparent",font=("Arial",12))
        self.label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        def close():
            radiobutton_ans_var.set(-1)
            radiobutton_ans_1.configure(state = "normal")
            radiobutton_ans_2.configure(state = "normal")
            radiobutton_ans_3.configure(state = "normal")
            radiobutton_ans_4.configure(state = "normal")
            
            self.destroy()

        def exit():
            master.destroy()

        button1 = customtkinter.CTkButton(master=self, text="RESPONDER NOVAMENTE", command=close)
        button1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button2 = customtkinter.CTkButton(master=self, text="VOLTAR AO MENU", command=exit)
        button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        if complete >= 5:
            button1.configure(state="disabled")

class ErrorWindow(customtkinter.CTkToplevel):
    def __init__(self, master, radiobutton_ans_var, radiobutton_ans_1, radiobutton_ans_2, radiobutton_ans_3, radiobutton_ans_4, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x200")
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", "disable_event")
        self.title("Error")

        self.label = customtkinter.CTkLabel(master=self, text="Erro: Escolha uma resposta!", fg_color="transparent",font=("Arial",12))
        self.label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        def close():
            radiobutton_ans_var.set(-1)
            radiobutton_ans_1.configure(state = "normal")
            radiobutton_ans_2.configure(state = "normal")
            radiobutton_ans_3.configure(state = "normal")
            radiobutton_ans_4.configure(state = "normal")

            self.destroy()

        button = customtkinter.CTkButton(master=self, text="OK", command=close)
        button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

class CompletedWindow(customtkinter.CTkToplevel):
    def __init__(self, master, func, complete, difficult, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x200")
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", "disable_event")
        self.title("Mensagem")


        if(complete < 5): points = round((50 * difficult *difficult + 50) / math.pow(2,complete))
        else: points = 0

        self.label = customtkinter.CTkLabel(master=self, text= f"Exercício já resolvido, deseja refazer?\nConclusões restantes: {5-complete}/5\nValor de pontos: {points}", fg_color="transparent",font=("Arial",12))
        self.label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        def confirm():
            self.destroy()

        def cancel():
            func(False)
            self.destroy()

        button1 = customtkinter.CTkButton(master=self, text="RESPONDER NOVAMENTE", command=confirm)
        button1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button2 = customtkinter.CTkButton(master=self, text="CANCELAR", command=cancel)
        button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        if complete >= 5: 
            button1.configure(state="disabled")

class UncompletedWindow(customtkinter.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x200")
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", "disable_event")
        self.title("Mensagem")

        self.label = customtkinter.CTkLabel(master=self, text="O exercício precisa estar resolvido\n para ser consultado.", fg_color="transparent",font=("Arial",14))
        self.label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        def cancel():
            self.destroy()

        button = customtkinter.CTkButton(master=self, text="FECHAR", command=cancel)
        button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

class CheckWindow(customtkinter.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x200")
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", "disable_event")
        self.title("Mensagem")

        self.label = customtkinter.CTkLabel(master=self, text="Você precisa concluir um exercício de dificuldade\ninferior antes de resolver este.", fg_color="transparent",font=("Arial",12))
        self.label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        def cancel():
            self.destroy()

        button = customtkinter.CTkButton(master=self, text="FECHAR", command=cancel)
        button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


class ExerciseWindow(customtkinter.CTkToplevel):

    def __init__(self, master, item, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("1200x700")
        self.resizable(False,False)
        

        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        difficult = int(f.readline().rstrip())
        title = f.readline().rstrip()
        complete = int(f.readline().rstrip())
        exercise = f.readline().rstrip()
        answer = int(f.readline().rstrip())
        option1 = f.readline().rstrip()
        option2 = f.readline().rstrip()
        option3 = f.readline().rstrip()
        option4 = f.readline().rstrip()
        f.close()

        self.title(title)

        self.label = customtkinter.CTkLabel(master=self, text=title, fg_color="transparent",font=("Arial",30))
        self.label.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

        
        self.label = customtkinter.CTkLabel(master=self, text=exercise,  fg_color="transparent",font=("Arial",20), wraplength=1080, justify="left")
        self.label.place(relx=0.05, rely=0.25, anchor=customtkinter.W)

        def send_answer():

            

            if radiobutton_ans_var.get() == -1:
                if self.dialog_window is None or not self.dialog_window.winfo_exists():
                    self.dialog_window = ErrorWindow(self,  radiobutton_ans_var, radiobutton_ans_1, radiobutton_ans_2, radiobutton_ans_3, radiobutton_ans_4)
                    self.dialog_window.grab_set()
                else:
                    self.dialog_window.focus() 
            elif radiobutton_ans_var.get() == answer:

                

                with open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8") as f:
                    lines = f.readlines()
                lines[2] = f"{int(lines[2]) + 1}\n"

                with open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "w", encoding="utf8") as f:
                     f.writelines(lines)
                
                if(int(lines[2]) < 5): points = round((50 * difficult *difficult + 50) / math.pow(2,int(lines[2])))
                else: points = 0

                with open(os.path.join(current_dir, "dados" ,"dados.txt"), "r", encoding="utf8") as f:
                    data_lines = f.readlines()
                data_lines[0] = str(int(data_lines[0]) + points*2) + "\n"
                if int(data_lines[1]) < difficult: data_lines[1] = str(difficult)


                with open(os.path.join(current_dir, "dados" ,"dados.txt"), "w", encoding="utf8") as f:
                     f.writelines(data_lines)
                
                if self.dialog_window is None or not self.dialog_window.winfo_exists():
                    self.dialog_window = DialogWindow(self, f"Você acertou! :D\nConclusões restantes: {5-int(lines[2])}/5\nValor de pontos: {points}", int(lines[2]),  radiobutton_ans_var, radiobutton_ans_1, radiobutton_ans_2, radiobutton_ans_3, radiobutton_ans_4)
                    self.dialog_window.grab_set()
                else:
                    self.dialog_window.focus() 
                
            else:
                if(complete < 5): points = round((50 * difficult *difficult + 50) / math.pow(2,complete))
                else: points = 0
                if self.dialog_window is None or not self.dialog_window.winfo_exists():
                    self.dialog_window = DialogWindow(self, f"Você errou D:\nConclusões restantes: {5-complete}/5\nValor de pontos: {points}", complete,  radiobutton_ans_var, radiobutton_ans_1, radiobutton_ans_2, radiobutton_ans_3, radiobutton_ans_4)
                    self.dialog_window.grab_set()
                else:
                    self.dialog_window.focus() 
            radiobutton_ans_1.configure(state = "disabled")
            radiobutton_ans_2.configure(state = "disabled")
            radiobutton_ans_3.configure(state = "disabled")
            radiobutton_ans_4.configure(state = "disabled")

        radiobutton_ans_var = customtkinter.IntVar(value=-1)

        radiobutton_ans_1 = customtkinter.CTkRadioButton(master=self, text=option1, variable=radiobutton_ans_var, value=0)
        radiobutton_ans_1.place(relx=0.05, rely=0.4, anchor=customtkinter.W)

        radiobutton_ans_2 = customtkinter.CTkRadioButton(master=self, text=option2, variable=radiobutton_ans_var, value=1)
        radiobutton_ans_2.place(relx=0.05, rely=0.5, anchor=customtkinter.W)

        radiobutton_ans_3 = customtkinter.CTkRadioButton(master=self, text=option3, variable=radiobutton_ans_var, value=2)
        radiobutton_ans_3.place(relx=0.05, rely=0.6, anchor=customtkinter.W)

        radiobutton_ans_4 = customtkinter.CTkRadioButton(master=self, text=option4, variable=radiobutton_ans_var, value=3)
        radiobutton_ans_4.place(relx=0.05, rely=0.7, anchor=customtkinter.W)


        self.dialog_window = None    
        
        button = customtkinter.CTkButton(master=self, text="ENVIAR RESPOSTA", command=send_answer)
        button.place(relx=0.05, rely=0.8, anchor=customtkinter.W)


class AnswerWindow(customtkinter.CTkToplevel):

    def __init__(self, master, item, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("1200x700")
        self.resizable(False,False)
        

        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        difficult = int(f.readline().rstrip())
        title = f.readline().rstrip()
        complete = int(f.readline().rstrip())
        exercise = f.readline().rstrip()
        answer = int(f.readline().rstrip())
        option1 = f.readline().rstrip()
        option2 = f.readline().rstrip()
        option3 = f.readline().rstrip()
        option4 = f.readline().rstrip()
        f.close()

        self.title(title)

        self.label = customtkinter.CTkLabel(master=self, text=title, fg_color="transparent",font=("Arial",30))
        self.label.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

        
        self.label = customtkinter.CTkLabel(master=self, text=exercise,  fg_color="transparent",font=("Arial",20), wraplength=1080, justify="left")
        self.label.place(relx=0.05, rely=0.25, anchor=customtkinter.W)


            
        radiobutton_ans_var = customtkinter.IntVar(value=answer)

        radiobutton_ans_1 = customtkinter.CTkRadioButton(master=self, text=option1, variable=radiobutton_ans_var, value=0)
        radiobutton_ans_1.place(relx=0.05, rely=0.4, anchor=customtkinter.W)

        radiobutton_ans_2 = customtkinter.CTkRadioButton(master=self, text=option2, variable=radiobutton_ans_var, value=1)
        radiobutton_ans_2.place(relx=0.05, rely=0.5, anchor=customtkinter.W)

        radiobutton_ans_3 = customtkinter.CTkRadioButton(master=self, text=option3, variable=radiobutton_ans_var, value=2)
        radiobutton_ans_3.place(relx=0.05, rely=0.6, anchor=customtkinter.W)

        radiobutton_ans_4 = customtkinter.CTkRadioButton(master=self, text=option4, variable=radiobutton_ans_var, value=3)
        radiobutton_ans_4.place(relx=0.05, rely=0.7, anchor=customtkinter.W)


        radiobutton_ans_1.configure(state = "disabled")
        radiobutton_ans_2.configure(state = "disabled")
        radiobutton_ans_3.configure(state = "disabled")
        radiobutton_ans_4.configure(state = "disabled")


        self.dialog_window = None    
        
        button = customtkinter.CTkButton(master=self, text="FECHAR", command=self.destroy)
        button.place(relx=0.05, rely=0.8, anchor=customtkinter.W)


class UpdateWindow(customtkinter.CTkToplevel):

    def __init__(self, master, item, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("1200x700")
        self.resizable(False,False)
        

        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        difficult = int(f.readline().rstrip())
        title = f.readline().rstrip()

        f.close()

        self.title(title)

        self.label = customtkinter.CTkLabel(master=self, text=title, fg_color="transparent",font=("Arial",30))
        self.label.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

            
        radiobutton_ans_var = customtkinter.IntVar(value=difficult)

        radiobutton_ans_1 = customtkinter.CTkRadioButton(master=self, text="Fácil", variable=radiobutton_ans_var, value=1)
        radiobutton_ans_1.place(relx=0.05, rely=0.4, anchor=customtkinter.W)

        radiobutton_ans_2 = customtkinter.CTkRadioButton(master=self, text="Médio", variable=radiobutton_ans_var, value=2)
        radiobutton_ans_2.place(relx=0.05, rely=0.5, anchor=customtkinter.W)

        radiobutton_ans_3 = customtkinter.CTkRadioButton(master=self, text="Difícil", variable=radiobutton_ans_var, value=3)
        radiobutton_ans_3.place(relx=0.05, rely=0.6, anchor=customtkinter.W)

        self.dialog_window = None    
        
        def confirm():
            with open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8") as f:
                lines = f.readlines()
            lines[0] = str(radiobutton_ans_var.get())+"\n"

            with open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "w", encoding="utf8") as f:
                    f.writelines(lines)
            self.destroy()

        button = customtkinter.CTkButton(master=self, text="CONFIRMAR", command=confirm)
        button.place(relx=0.05, rely=0.8, anchor=customtkinter.W)


class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, rcommand=None, ccommand=None, acommand=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.rcommand = rcommand
        self.ccommand = ccommand
        self.acommand = acommand
        self.radiobutton_variable = customtkinter.StringVar()
        self.item_list = list()
        self.difficult_list = list()
        self.label_list = list()
        self.dlabel_list = list()
        self.rbutton_list = list()
        self.cbutton_list = list()
        self.abutton_list = list()

    def add_item(self, item, difficult, txt, image=None):
        label = customtkinter.CTkLabel(self, text=txt, image=image, compound="left", padx=5, anchor="w")
    
        if difficult == 1: 
            label2 = customtkinter.CTkLabel(self, text="Fácil", compound="left", padx=5, anchor="w")
        elif difficult == 2: 
            label2 = customtkinter.CTkLabel(self, text="Médio", compound="left", padx=5, anchor="w")
        elif difficult == 3:
            label2 = customtkinter.CTkLabel(self, text="Difícil", compound="left", padx=5, anchor="w")

        rbutton = customtkinter.CTkButton(self, text="Resolver", width=100, height=24)
        cbutton = customtkinter.CTkButton(self, text="Consultar", width=100, height=24)
        abutton = customtkinter.CTkButton(self, text="Alterar", width=100, height=24)

        if self.rcommand is not None:
            rbutton.configure(command=lambda: self.rcommand(item))

        if self.ccommand is not None:
            cbutton.configure(command=lambda: self.ccommand(item))

        if self.acommand is not None:
            abutton.configure(command=lambda: self.acommand(item))


        label.grid(row=len(self.label_list), column=0, pady=(10, 10), sticky="w")
        label2.grid(row=len(self.dlabel_list), column=1, pady=(10, 10), sticky="w")
        rbutton.grid(row=len(self.rbutton_list), column=2, pady=(10, 10), padx=5)
        cbutton.grid(row=len(self.cbutton_list), column=3, pady=(10, 10), padx=5)
        abutton.grid(row=len(self.abutton_list), column=4, pady=(10, 10), padx=5)
        
        self.item_list.append(item)
        self.difficult_list.append(difficult)
        self.label_list.append(label)
        self.dlabel_list.append(label2)
        self.rbutton_list.append(rbutton)
        self.cbutton_list.append(cbutton)
        self.abutton_list.append(abutton)
            
    def sort_items(self):
        zipped_lists = zip(self.difficult_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list, self.item_list)
        sorted_pairs = sorted(zipped_lists, key=lambda x: x[0])
        self.difficult_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list, self.item_list = zip(*sorted_pairs)

        i = 0
        for _item, label, label2, rbutton, cbutton, abutton in zip(self.item_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list):
            label.grid(row=i, column=0, pady=(10, 10), sticky="w")
            label2.grid(row=i, column=1, pady=(10, 10), sticky="w")
            rbutton.grid(row=i, column=2, pady=(10, 10), padx=5)
            cbutton.grid(row=i, column=3, pady=(10, 10), padx=5)
            abutton.grid(row=i, column=4, pady=(10, 10), padx=5)
            i+=1

    def reverse_sort_items(self):

        zipped_lists = zip(self.difficult_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list, self.item_list)
        sorted_pairs = sorted(zipped_lists, key=lambda x: x[0],reverse=True)
        self.difficult_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list, self.item_list = zip(*sorted_pairs)

        i = 0
        for _item, label, label2, rbutton, cbutton, abutton in zip(self.item_list, self.label_list, self.dlabel_list, self.rbutton_list, self.cbutton_list, self.abutton_list):
            label.grid(row=i, column=0, pady=(10, 10), sticky="w")
            label2.grid(row=i, column=1, pady=(10, 10), sticky="w")
            rbutton.grid(row=i, column=2, pady=(10, 10), padx=5)
            cbutton.grid(row=i, column=3, pady=(10, 10), padx=5)
            abutton.grid(row=i, column=4, pady=(10, 10), padx=5)
            i+=1
        
    def update_items(self):  
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        for _item, label in zip(self.item_list, self.label_list):
            f = open(os.path.join(current_dir, "exercicios" ,f"{_item}.txt"), "r", encoding="utf8")
            next(f)
            next(f)
            complete = int(f.readline().rstrip())

            if complete >= 1:
                label.configure(image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_done.png"))))

            f.close()

        


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.title("Exercícios de Física")
        self.geometry("1200x700")
        self.resizable(False,False)

        self.check = True

        self.label = customtkinter.CTkLabel(master=self, text="Exercícios de Física", fg_color="transparent",font=("Arial",40))
        self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.radiobutton_var = customtkinter.IntVar(value=1)

        radiobutton_1 = customtkinter.CTkRadioButton(master=self, text=u"Dificuldade Crescente", variable=self.radiobutton_var, value=1, command=self.filter_event)
        radiobutton_1.place(relx=0.72, rely=0.15, anchor=customtkinter.N)

        radiobutton_2 = customtkinter.CTkRadioButton(master=self, text=u"Dificuldade Decrescente", variable=self.radiobutton_var, value=2, command=self.reverse_filter_event)
        radiobutton_2.place(relx=0.86, rely=0.15, anchor=customtkinter.N)

        f = open(os.path.join(current_dir, "dados" ,"dados.txt"), "r", encoding="utf8")
        points = int(f.readline().rstrip())
        f.close()

        self.labelPoints = customtkinter.CTkLabel(master=self, text=f"Pontos: {points}", fg_color="transparent",font=("Arial",12))
        self.labelPoints.place(relx=0.08, rely=0.175, anchor=customtkinter.W)


        # Cria menu de exercícios
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=1000, height=500, rcommand=self.answer_event, ccommand=self.view_event, 
                                                                        acommand=self.update_event, corner_radius=0, label_text="Escolha o exercício que deseja realizar abaixo: ")
        self.scrollable_label_button_frame.place(relx=0.5, rely=0.2, anchor=customtkinter.N)

        i = 0
        while os.path.isfile(os.path.join(current_dir, "exercicios" ,f"{i}.txt")): 
            f = open(os.path.join(current_dir, "exercicios" ,f"{i}.txt"), "r", encoding="utf8")
            difficult = int(f.readline().rstrip())
            title = f.readline().rstrip()
            complete = int(f.readline().rstrip())
            if complete == 0:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_not_done.png"))))
            elif complete >= 1:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_done.png"))))
            i += 1
            f.close()


        self.toplevel_window = None    
        self.scrollable_label_button_frame.sort_items()
        
    

    def answer_event(self, item):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        difficult = int(f.readline().rstrip())
        next(f)
        complete = int(f.readline().rstrip())
        f.close()

        f = open(os.path.join(current_dir, "dados" ,"dados.txt"), "r", encoding="utf8")
        next(f)
        check = int(f.readline().rstrip())
        f.close()

        if difficult-1 <= check:
            if complete >= 1:
                self.dialog_window = CompletedWindow(self, self.receiver, complete, difficult)
                self.dialog_window.grab_set()
                self.wait_window(self.dialog_window)
            if self.check:
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ExerciseWindow(self, item)
                    self.toplevel_window.grab_set()
                    self.wait_window(self.toplevel_window)
                    self.scrollable_label_button_frame.update_items()
                    f = open(os.path.join(current_dir, "dados" ,"dados.txt"), "r", encoding="utf8")
                    points = int(f.readline().rstrip())
                    f.close()
                    self.labelPoints.configure(text=f"Pontos: {points}")
            self.check = True
        else:
            self.dialog_window = CheckWindow(self)
            self.dialog_window.grab_set()
            self.wait_window(self.dialog_window)

    def view_event(self, item):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        next(f)
        next(f)
        complete = int(f.readline().rstrip())
        f.close()
        if complete == 0:
            self.dialog_window = UncompletedWindow(self)
            self.dialog_window.grab_set()
            self.wait_window(self.dialog_window)
        if complete >= 1:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = AnswerWindow(self, item)
                self.toplevel_window.grab_set()
                self.wait_window(self.toplevel_window)
                self.scrollable_label_button_frame.update_items()
        
    def update_event(self, item):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(current_dir, "exercicios" ,f"{item}.txt"), "r", encoding="utf8")
        next(f)
        next(f)
        complete = int(f.readline().rstrip())
        f.close()
        if complete == 0:
            self.dialog_window = UncompletedWindow(self)
            self.dialog_window.grab_set()
            self.wait_window(self.dialog_window)
        if complete >= 1:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = UpdateWindow(self, item)
                self.toplevel_window.grab_set()
                self.wait_window(self.toplevel_window)
                self.update_frame()
                
        
    def receiver(self, check):
        self.check = check
        

    def filter_event(self):
        self.scrollable_label_button_frame.sort_items()

    def reverse_filter_event(self):
        self.scrollable_label_button_frame.reverse_sort_items()

    def update_frame(self):
        self.scrollable_label_button_frame.destroy()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=1000, height=500, rcommand=self.answer_event, ccommand=self.view_event, 
                                                                        acommand=self.update_event, corner_radius=0, label_text="Escolha o exercício que deseja realizar abaixo: ")
        self.scrollable_label_button_frame.place(relx=0.5, rely=0.2, anchor=customtkinter.N)

        i = 0
        while os.path.isfile(os.path.join(current_dir, "exercicios" ,f"{i}.txt")): 
            f = open(os.path.join(current_dir, "exercicios" ,f"{i}.txt"), "r", encoding="utf8")
            difficult = int(f.readline().rstrip())
            title = f.readline().rstrip()
            complete = int(f.readline().rstrip())
            if complete == 0:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_not_done.png"))))
            elif complete >= 1:
                self.scrollable_label_button_frame.add_item(i, difficult, title, image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "imagens", "icon_done.png"))))
            i += 1
            f.close()
        if (self.radiobutton_var.get() == 1): self.scrollable_label_button_frame.sort_items()
        else: self.scrollable_label_button_frame.reverse_sort_items()


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()