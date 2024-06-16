import os
import tkinter as tk
from commands.commands import clear_files
from widgets_manager.WidgetManger import WidgetManager
from tkinter import messagebox
from tkinter import filedialog

folder_paths = {
    "Temp": r"C:\Windows\Temp",
    "%Temp%": rf"C:\Users\{os.getlogin()}\AppData\Local\Temp",
    "Prefetch": r"C:\Windows\Prefetch"
}


def add_temp_folders():
    name_folder = os.getlogin()
    temp_widget.select()
    percent_temp_widget.select()
    prefetch_widget.select()
    folders_to_delete["Temp"] = r"C:\Windows\Temp"
    folders_to_delete["%Temp%"] = rf"C:\Users\{name_folder}\AppData\Local\Temp"
    folders_to_delete["Prefetch"] = r"C:\Windows\Prefetch"


def on_find_folder():
    path = filedialog.askdirectory()
    if path:
        folders_to_delete["select_folder"] = path
        entry_path.delete(0, tk.END)
        entry_path.insert(0, path)


def clear_all_files():
    removed_files = clear_files(folders_to_delete)
    message = ""
    for key, amount in removed_files.items():
        message += f" {amount} arquivos da pasta {key} foram removidos!\n"
    messagebox.showinfo("Alerta", message)
    reset_interface()


def select_all():
    if var_all_selected.get() == 1:
        add_temp_folders()
    else:
        reset_interface()


def remove_folder_to_list_delete(name):
    if name in folders_to_delete.keys():
        del folders_to_delete[name]


def reset_interface():
    entry_path.delete(0, tk.END)
    temp_widget.deselect()
    percent_temp_widget.deselect()
    prefetch_widget.deselect()
    select_all_checkbox.deselect()
    folders_to_delete.clear()


def add_folder_to_delete_list():
    for folder_key, folder_path in folder_paths.items():
        if folder_key == "Temp" and var_temp.get() == 1:
            folders_to_delete[folder_key] = folder_path
        elif folder_key == "%Temp%" and var_percent_temp.get() == 1:
            folders_to_delete[folder_key] = folder_path
        elif folder_key == "Prefetch" and var_prefetch.get() == 1:
            folders_to_delete[folder_key] = folder_path
        else:
            remove_folder_to_list_delete(folder_key)


folders_to_delete = {}
widgets_manager = WidgetManager()
window = tk.Tk()
window.title("FilesCleaner")
window.geometry("300x300")

var_all_selected = tk.IntVar()
var_temp = tk.IntVar()
var_percent_temp = tk.IntVar()
var_prefetch = tk.IntVar()

# Widgets
widgets_manager.create_widget(tk.Label(window, text="Caminho: "))
entry_path = widgets_manager.create_widget(tk.Entry(window, width=40))
button_find_folder = widgets_manager.create_widget(tk.Button(window, text="Procurar", command=on_find_folder))

select_all_checkbox = widgets_manager.create_widget(
    tk.Checkbutton(window, text="Selecionar todos", variable=var_all_selected, command=select_all))
temp_widget = widgets_manager.create_widget(
    tk.Checkbutton(window, text="Temp", variable=var_temp, command=add_folder_to_delete_list))
percent_temp_widget = widgets_manager.create_widget(
    tk.Checkbutton(window, text="%Temp%", variable=var_percent_temp, command=add_folder_to_delete_list))
prefetch_widget = widgets_manager.create_widget(
    tk.Checkbutton(window, text="Prefetch", variable=var_prefetch, command=add_folder_to_delete_list))
button_clear = widgets_manager.create_widget(tk.Button(window, text="Apagar", command=clear_all_files))

widgets_manager.start()

# Start
window.mainloop()
