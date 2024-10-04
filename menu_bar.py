
import customtkinter

class MenuBar:

    def __init__(self, root) -> None:

        self.width = root.winfo_width()
        self.height = 60

        self._init_main_frame(root)
        self._init_program_title()


    def _init_main_frame(self, root) -> None:
        self.main_frame = customtkinter.CTkFrame(root, width=self.width, height=self.height)
        self.main_frame.pack(side='top', fill='x')


    def _init_program_title(self) -> None:
        program_title = customtkinter.CTkLabel(self.main_frame, text="Adrenaline", font=("Arial", 30, "bold"), text_color='red')
        program_title.pack(side='left', padx=10, pady=10)
