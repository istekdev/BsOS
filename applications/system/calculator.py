"""
Status: WIP

Needs Finished:
- Fullscreen Adjustment
- Exiting Fullscreen
- Dragging
"""

from applications.background import appearance
import customtkinter, json, time

with open("./config.json", "r") as r:
  config = json.load(r)

fs = False
original = {}

def close():
    CALC.destroy()

def fullscreen(obj):
  global fs, original
  if fs == False:
    original["x"] = obj.winfo_x()
    original["y"] = obj.winfo_y()
    original["w"] = obj.winfo_width()
    original["h"] = obj.winfo_height()
    obj.place(x=0, y=0, relwidth=1, relheight=1)
    obj.configure(corner_radius=0)
    fs = True
  else:
    obj.place(x=original["x"], y=original["y"])
    obj.configure(width=original["w"], height=original["h"], corner_radius=20)
    fs = False

def minimize():
    CALC.iconify()

calcBtns = [
  "(", ")", "C", "/",
  "7", "8", "9", "*",
  "4", "5", "6", "-",
  "1", "2", "3", "+",
  ".", "0", "+/-", "="
]

def open():
  CALC = customtkinter.CTk()
  if config["settings"]["appearances"]["theme"] == "light":
    calculator = customtkinter.CTkFrame(CALC, width=330, height=470, fg_color=config["settings"]["appearances"]["themes"]["light"]["background"], corner_radius=20)
    header = customtkinter.CTkFrame(calculator, height=100, fg_color=config["settings"]["appearances"]["themes"]["light"]["card"])
    header.pack(fill="x")
    title = customtkinter.CTkLabel(header, text="Calculator", text_color=config["settings"]["appearances"]["themes"]["light"]["title"], font=(config["settings"]["appearances"]["font"], 14, "bold"))
    title.pack(side="right", padx=10)
  elif config["settings"]["appearances"]["theme"] == "dark":
    calculator = customtkinter.CTkFrame(CALC, width=330, height=470, fg_color=config["settings"]["appearances"]["themes"]["dark"]["background"], corner_radius=20)
    header = customtkinter.CTkFrame(calculator, height=100, fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"])
    header.pack(fill="x")
    title = customtkinter.CTkLabel(header, text="Calculator", text_color=config["settings"]["appearances"]["themes"]["dark"]["title"], font=(config["settings"]["appearances"]["font"], 14, "bold"))
    title.pack(side="right", padx=10)
  elif config["settings"]["appearances"]["theme"] == "cursed":
    calculator = customtkinter.CTkFrame(CALC, width=330, height=470, fg_color=appearance.cursed(), corner_radius=20)
    header = customtkinter.CTkFrame(calculator, height=100, fg_color=appearance.cursed())
    header.pack(fill="x")
    title = customtkinter.CTkLabel(header, text="Calculator", text_color=appearance.cursed(), font=(config["settings"]["appearances"]["font"], 14, "bold"))
    title.pack(side="right", padx=10)

  x, y = 200, 60
  for apps in config["system"]["runningApps"]:
    if apps["x"] == x and apps["y"] == y:
      x += 25
      y+= 25
      calculator.place(x=x, y=y)
    else:
      calculator.place(x=200, y=60)

  block = {"application": "Calculator", "directory": "/applications/system/calculator.py", "x": x, "y": y}
  config["system"]["runningApps"].append(block)
  with open("./config.json", "w") as w:
    json.dump(config, w, indent=4)

  left = customtkinter.CTkFrame(header, fg_color="transparent")
  left.pack(side="left", padx=10)

  close = customtkinter.CTkButton(left, text="", width=15, height=15, corner_radius=15, fg_color=config["system"]["controls"]["exit"], command=close)
  minimum = customtkinter.CTkButton(left, text="", width=15, height=15, corner_radius=15, fg_color=config["system"]["controls"]["minimize"], command=minimize)
  maximum = customtkinter.CTkButton(left, text="", width=15, height=15, corner_radius=15, fg_color=config["system"]["controls"]["maximize"], command=lambda: fullscreen(calculator))
  close.pack(side="left", padx=4)
  minimum.pack(side="left", padx=4)
  maximum.pack(side="left", padx=4)

  body = customtkinter.CTkFrame(calculator, fg_color="transparent")
  body.pack(fill="both", expand=True, padx=15, pady=15)
  output = customtkinter.StringVar()
  if config["settings"]["appearances"]["theme"] == "light":
    screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=config["settings"]["appearances"]["themes"]["light"]["card"], corner_radius=10, anchor="e", font=(config["settings"]["appearances"]["font"], 20))
  elif config["settings"]["appearances"]["theme"] == "dark":
    screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"], corner_radius=10, anchor="e", font=(config["settings"]["appearances"]["font"], 20))
  elif config["settings"]["appearances"]["theme"] == "cursed":
    screen = customtkinter.CTkLabel(body, textvariable=output, width=310, height=50, fg_color=appearance.cursed(), corner_radius=10, anchor="e", font=(config["settings"]["appearances"]["font"], 20))
  screen.pack(fill="x", pady=(10, 20))

  rows = 0
  columns = 0
  btns = customtkinter.CTkFrame(body, fg_color="transparent")
  btns.pack(expand=True)
  for btn in calcBtns:
    if config["settings"]["appearances"]["theme"] == "light":
      bt = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=config["settings"]["appearances"]["themes"]["light"]["card2"], fg_color=config["settings"]["appearances"]["themes"]["light"]["card"], text_color=config["settings"]["appearances"]["themes"]["light"]["title"], command=lambda x=btn: calc(x))
    elif config["settings"]["appearances"]["theme"] == "dark":
      bt = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=config["settings"]["appearances"]["themes"]["dark"]["card2"], fg_color=config["settings"]["appearances"]["themes"]["dark"]["card"], text_color=config["settings"]["appearances"]["themes"]["dark"]["title"], command=lambda x=btn: calc(x))
    elif config["settings"]["appearances"]["theme"] == "cursed":
      bt = customtkinter.CTkButton(btns, text=btn, width=60, height=60, corner_radius=15, hover_color=appearance.cursed(), fg_color=appearance.cursed(), text_color=appearance.cursed(), command=lambda x=btn: calc(x))
    bt.grid(row=rows, column=columns, padx=6, pady=6, sticky="nsew")
    columns += 1
    if columns > 3:
      columns = 0
      rows += 1
  for b in range(4):
    btns.grid_columnconfigure(b, weight=1)
    btns.grid_rowconfigure(b, weight=1)

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
      time.sleep(1)
      output.set("")
  elif val == "+/-":
    if active:
      if active.startswith("-"):
        output.set(active[1:])
      else:
        output.set("-" + active)
  else:
    output.set(active + val)
