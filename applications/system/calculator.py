from applications.background import appearance
import customtkinter, math, json, random
from termcolor import colored
from core import display

with open("./config.json", "r") as r:
  config = json.load(r)

calcBtns = [
  "(", ")", "C", "/",
  "7", "8", "9", "*",
  "4", "5", "6", "-",
  "1", "2", "3", "+",
  ".", "0", "+/-", "="
]

window = customtkinter.CTk()
if config["settings"]["appearances"]["theme"] == "light":
  calculator = customtkinter.CTkFrame(window, width=330, height=470, fg_color=config["settings"]["appearances"]["themes"]["light"]["background"], corner_radius=20)
  calculator.place(x=200, y=60)
  header = customtkinter.CTkFrame(calculator, height=40, fg_color=config["settings"]["appearances"]["themes"]["light"]["card"], corner_radius=20)
  header.pack(fill="x")
  customtkinter.CTkLabel(header, text="Calculator", text_color=config["settings"]["appearances"]["themes"]["light"]["title"], font=(config["settings"]["appearances"]["font"], 14, "bold"))
elif config["settings"]["appearances"]["theme"] == "dark":
  calculator = customtkinter.CTkFrame(window, width=330, height=470, fg_color=config["settings"]["appearances"]["themes"]["dark"]["background"], corner_radius=20)
  calculator.place(x=200, y=60)
  header = customtkinter.CTkFrame(calculator, height=40, fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"], corner_radius=20)
  header.pack(fill="x")
  customtkinter.CTkLabel(header, text="Calculator", text_color=config["settings"]["appearances"]["themes"]["dark"]["title"], font=(config["settings"]["appearances"]["font"], 14, "bold"))
elif config["settings"]["appearances"]["theme"] == "cursed":
  calculator = customtkinter.CTkFrame(window, width=330, height=470, fg_color=appearance.cursed(), corner_radius=20)
  calculator.place(x=200, y=60)
  header = customtkinter.CTkFrame(calculator, height=40, fg_color=appearance.cursed(), corner_radius=20)
  header.pack(fill="x")
  customtkinter.CTkLabel(header, text="Calculator", text_color=appearance.cursed(), font=(config["settings"]["appearances"]["font"], 14, "bold"))

output = customtkinter.StringVar()
if config["settings"]["appearances"]["theme"] == "light":
  screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=config["settings"]["appearances"]["themes"]["light"]["card"], corner_radius=10, anchor="e", font=("Arial", 20))
elif config["settings"]["appearances"]["theme"] == "dark":
  screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"], corner_radius=10, anchor="e", font=("Arial", 20))
elif config["settings"]["appearances"]["theme"] == "cursed":
  screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=appearance.cursed(), corner_radius=10, anchor="e", font=("Arial", 20))
screen.pack(pady=(10, 20))

rows = 0
columns = 0
body = customtkinter.CTkFrame(calculator, fg_color="transparent")
body.pack(fill="both", expand=True, padx=15, pady=15)
btns = customtkinter.CTkFrame(body, fg_color="transparent")
btns.pack(expand=True)
for btn in calcBtns:
  if config["settings"]["appearances"]["theme"] == "light":
    btn = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=config["settings"]["appearances"]["themes"]["light"]["card2"], fg_color=config["settings"]["appearances"]["themes"]["light"]["card"], text_color=config["settings"]["appearances"]["themes"]["light"]["title"], command=lambda x=btn: calc(x))
  elif config["settings"]["appearances"]["theme"] == "dark":
    btn = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=config["settings"]["appearances"]["themes"]["dark"]["card2"], fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"], text_color=config["settings"]["appearances"]["themes"]["dark"]["title"], command=lambda x=btn: calc(x))
  elif config["settings"]["appearances"]["theme"] == "cursed":
    btn = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=appearance.cursed(), fg_color=appearance.cursed(), text_color=appearance.cursed(), command=lambda x=btn: calc(x))
  btn.grid(row=row, column=columns, padx=6, pady=6)
  columns += 1
  if columns > 3:
      columns = 0
      row += 1

def calc(val):
  active = output.get()
  if val == "C":
      output.set("")
  elif val == "=":
    try:
        result = str(eval(active))
        output.set(result)
      except Exception:
          output.set("Error")
  elif val == "+/-":
    if active:
        if active.startswith("-"):
            output.set(active[1:])
        else:
            output.set("-" + active)
  else:
    output.set(active + val)
