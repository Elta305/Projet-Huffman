import tkinter
import tkinter.messagebox
import tkinter.filedialog
import customtkinter
import fichiers as f
import affichage as a

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Projet Huffman")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Charger fichier", command=self.load_file)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Charger clé", command=self.load_key)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Charger fichier encodé", command=self.load_encoded_file)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Enregistrer fichier", command=self.enregistrer_fichier)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Enregistrer clé", command=self.enregistrer_cle)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Enregistrer fichier encodé", command=self.enregistrer_fichier_encode)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Encoder", command=self.encode)
        self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_2 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Afficher Arbre", command=self.affichage_arbre)
        self.main_button_2.grid(row=1, column=3, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox_encode = customtkinter.CTkTextbox(self, width=250, height=50)
        self.textbox_encode.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self, width=250, height=70)
        self.textbox.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox_2 = customtkinter.CTkTextbox(self, width=250, height=70)
        self.textbox_2.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox_encode.insert("0.0", "Texte à encoder")
        self.textbox.insert("0.0", "Clé de décodage")
        self.textbox_2.insert("0.0", "Texte encodé")

        self.fichier = f.Fichier()
        self.arbre = a.Interface()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def load_file(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        file_path = tkinter.filedialog.Open(self, filetypes=ftypes).show()
        texte = open(file_path, "r", encoding = 'utf8').read()
        self.textbox_encode.delete("0.0", "end")
        self.textbox_encode.insert("0.0", texte)
        self.fichier.set_fichier(texte)
    
    def load_key(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        key_path = tkinter.filedialog.Open(self, filetypes=ftypes).show()
        cle = open(key_path, "r", encoding = 'utf8').read()
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", cle)
        self.fichier.set_cle(cle)
        
    def load_encoded_file(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        file_path = tkinter.filedialog.Open(self, filetypes=ftypes).show()
        texte_encode = open(file_path, "r", encoding = 'utf8').read()
        self.textbox_encode.delete("0.0", "end")
        self.textbox_encode.insert("0.0", texte_encode)
        self.fichier.set_texte_encode(texte_encode)
 
    def encode(self):
        texte_encode = self.fichier.enregistrement_encodage(self.textbox_encode.get("0.0", "end"))
        texte_cle = self.fichier.enregistrement_cle(self.textbox_encode.get("0.0", "end"))
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", texte_cle)
        self.textbox_2.delete("0.0", "end")
        self.textbox_2.insert("0.0", texte_encode)

    def enregistrer_fichier(self):
        self.fichier.enregistrement_encodage(self.textbox_2.get("0.0", "end"))

    def enregistrer_cle(self):
        self.fichier.enregistrement_cle(self.textbox.get("0.0", "end"))
    
    def enregistrer_fichier_encode(self):
        self.fichier.enregistrement_texte_encode(self.textbox_encode.get("0.0", "end"))

    def affichage_arbre(self):
        a.afficher_arbre()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()