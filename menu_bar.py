
import customtkinter as ctk

class MenuBar:

    def __init__(self, root, root_width) -> None:

        self.width = root_width
        self.height = 60

        self._init_main_frame(root)
        self._init_program_title()


    def _init_main_frame(self, root) -> None:
        self.main_frame = ctk.CTkFrame(root, width=self.width, height=self.height)
        self.main_frame.pack(side='top', fill='x', padx=5, pady=5)


    def _init_program_title(self) -> None:
        program_title = ctk.CTkLabel(self.main_frame, text="Adrenaline", font=("Arial", 30, "bold"), text_color='red')
        program_title.pack(side='left', padx=10, pady=10)
