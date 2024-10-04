
import customtkinter

from menu_bar import MenuBar
from slider_section import SliderSection

class Main:

    def __init__(self) -> None:
        self.root = customtkinter.CTk()

        self.config_window()
        self.config_color()
        self.config_window_title()
        self.config_window_icon()

        self.add_menu_bar()
        self.add_slider_section()

    
    def config_window(self) -> None:
        self.width = 800
        self.height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))


    def config_color(self) -> None:
        customtkinter.set_default_color_theme("red.json")
        customtkinter.set_appearance_mode("dark")


    def config_window_title(self) -> None:
        self.root.title("Adrenaline")

    
    def config_window_icon(self) -> None:
        self.root.iconbitmap("blood icon.ico")


    def add_menu_bar(self) -> None:
        self.menu_bar = MenuBar(self.root)


    def add_slider_section(self) -> None:
        self.slider_section = SliderSection(self.root)


    def run(self) -> None:
        self.root.mainloop()
        

if __name__=='__main__':
    main = Main()
    main.run()
