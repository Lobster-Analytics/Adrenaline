
import customtkinter as ctk

class SliderSection:

    def __init__(self, root, root_width, root_height, menu_bar_height) -> None:
        
        self.width = root_width / 3
        self.height = root_height - menu_bar_height

        self._init_main_frame(root)
        self.add_sliders()


    def _init_main_frame(self, root) -> None:
        self.main_frame = ctk.CTkFrame(root, width=self.width, height=self.height)
        self.main_frame.pack(side='left', fill='y', padx=5, pady=2)


    def add_sliders(self) -> None:
        self.add_x_slider()
        self.add_y_slider()
        self.add_z_slider()
        self.add_power_slider()


    def add_x_slider(self) -> None:
        self.x_slider_label = ctk.CTkLabel(self.main_frame, text="X: 50", font=("Arial", 20, "bold"), text_color='red')
        self.x_slider_label.pack(side='top', padx=10, pady=10)
        self.x_slider = ctk.CTkSlider(self.main_frame, from_=0, to=100, command=self.x_slider_event)
        self.x_slider.pack(side='top', padx=10, pady=10)


    def add_y_slider(self) -> None:
        self.y_slider_label = ctk.CTkLabel(self.main_frame, text="Y: 50", font=("Arial", 20, "bold"), text_color='red')
        self.y_slider_label.pack(side='top', padx=10, pady=10)
        self.y_slider = ctk.CTkSlider(self.main_frame, from_=0, to=100, command=self.y_slider_event)
        self.y_slider.pack(side='top', padx=10, pady=10)


    def add_z_slider(self) -> None:
        self.z_slider_label = ctk.CTkLabel(self.main_frame, text="Z: 50", font=("Arial", 20, "bold"), text_color='red')
        self.z_slider_label.pack(side='top', padx=10, pady=10)
        self.z_slider = ctk.CTkSlider(self.main_frame, from_=0, to=100, command=self.z_slider_event)
        self.z_slider.pack(side='top', padx=10, pady=10)


    def add_power_slider(self) -> None:
        self.power_slider_label = ctk.CTkLabel(self.main_frame, text="Power: 50", font=("Arial", 20, "bold"), text_color='red')
        self.power_slider_label.pack(side='top', padx=10, pady=10)
        self.power_slider = ctk.CTkSlider(self.main_frame, from_=0, to=100, command=self.power_slider_event)
        self.power_slider.pack(side='top', padx=10, pady=10)


    def x_slider_event(self, value) -> None:
        self.x_slider_label.configure(text=f"X: {int(value)}")


    def y_slider_event(self, value) -> None:
        self.y_slider_label.configure(text=f"Y: {int(value)}")


    def z_slider_event(self, value) -> None:
        self.z_slider_label.configure(text=f"Z: {int(value)}")


    def power_slider_event(self, value) -> None:
        self.power_slider_label.configure(text=f"Power: {int(value)}")
