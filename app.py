# only for windows

import flet as ft
import subprocess as sp

def main(page: ft.Page):
   def save(self):
      try: 
       path = path_to_save.value
       with open(f'{path}', 'w') as file:
         file.write(input_field.value)
         save_button.text = "save"
         page.update()
      except FileNotFoundError:
       save_button.text = "path doesn't exists"
       page.update()

   def load(self):
      path = path_to_load.value
      try:
       with open(f'{path}', 'r') as file:
         content = file.read()
         input_field.value = content
         page.update()
      except FileNotFoundError:
       load_button.text = "path doesn't exists"
       page.update()
   input_field = ft.TextField(label="type something", hint_text="start typing...", multiline=True)
   br = ft.Container(height=30)
   save_button = ft.ElevatedButton(icon=ft.Icons.SAVE, on_click=save, text="save")
   path_to_save = ft.TextField(label="path to save", hint_text=f"C:/Users/{sp.getoutput('echo %USERNAME%')}/...", width=200)
   load_button = ft.ElevatedButton(icon=ft.Icons.RECEIPT_LONG, on_click=load, text="load")
   path_to_load = ft.TextField(label="path to load", hint_text=f"C:/Users/{sp.getoutput('echo %USERNAME%')}/...", width=200)
   page.title = "notepad"
   page.theme_mode = ft.ThemeMode.DARK
   page.add(input_field, br, save_button, path_to_save, br, load_button, path_to_load)

ft.app(main)
