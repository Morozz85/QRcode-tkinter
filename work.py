import customtkinter as ct
from PIL import Image


class App(ct.CTk):
    
    def __init__(self):
        super().__init__()
        # app settings
        self.set_settings()


        self.logo_label = ct.CTkLabel(master=self, text="Получение QR кода")
        self.logo_label.pack(pady=30)
        self.logo_label.configure(font=("Verdana", 20, "bold"))

        self.main_frame = ct.CTkFrame(master=self, fg_color="transparent", border_width=1)
        self.main_frame.pack(fill=ct.X,  expand=True, anchor="n")
        
        self.top_frame = ct.CTkFrame(master=self.main_frame, fg_color="transparent")
        self.top_frame.pack(pady=15, fill="x", expand=True)
        
        self.dog_label = ct.CTkLabel(master=self.top_frame, text="Номер договора")
        self.dog_label.grid(row=0, column=0, sticky="w", padx=(20,20))
        self.entry_dog = ct.CTkEntry(master=self.top_frame, width=450)
        self.entry_dog.grid(row=1, column=0, columnspan=1, padx=(20,20), sticky="nsew")
        
        self.dog_label = ct.CTkLabel(master=self.top_frame, text="Номер счёта")
        self.dog_label.grid(row=2, column=0, sticky="w", padx=(20,20))
        self.entry_dog = ct.CTkEntry(master=self.top_frame, width=450)
        self.entry_dog.grid(row=3, column=0, columnspan=1, padx=(20,20), sticky="nsew")
        
        
        # self.main_frame.grid(row=1, column=0, padx=(20,20),pady=(20,0), sticky="nsew")



    def set_styles(self, **kwargs):
        pass




    def set_settings(self):
        self.geometry("500x630")
        self.title("QRcode generator")
        self.resizable(False, False)    



if __name__ == "__main__":
    app = App()
    app.mainloop()


