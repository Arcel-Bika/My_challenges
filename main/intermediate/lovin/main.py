import tkinter
from const import DO_VINOS

import tkintermapview
import customtkinter


root_tk = tkinter.Tk()  # Creation de la fenetre
root_tk.geometry(f"{root_tk.winfo_screenwidth()}x{root_tk.winfo_screenheight()}")
root_tk.iconbitmap('img/icon_region.ico')
root_tk.title("Lovin")
root_tk.configure(bg='#130626')


label_lovin = customtkinter.CTkLabel(master=root_tk, text="Lovin", width=120, height=50, text_font=30,
                                     corner_radius=8, text_color="#F1F1F1")
label_lovin.grid(column=0, row=0)


def call_loc(my_button):
    map_widget = tkintermapview.TkinterMapView(root_tk, width=1080, height=700)
    map_widget.grid(column=1, row=0, rowspan=len(DO_VINOS) + 1, padx=10, pady=10)

    map_widget.set_position(DO_VINOS[my_button][0][0], DO_VINOS[my_button][0][1], text=my_button)
    map_widget.set_zoom(15)


def my_button():
    for i, button in enumerate(DO_VINOS):
        button1 = customtkinter.CTkButton(master=root_tk, text=button, width=180, height=40, border_width=1,
                                          corner_radius=0, fg_color="#5D04D9", text_color="#F1F1F1",
                                          command=lambda b=button: call_loc(b))
        button1.grid(column=0, row=i+1)


my_button()
root_tk.mainloop()
