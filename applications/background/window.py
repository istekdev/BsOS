def close():
    window.destroy()

def fullscreen(obj):
  original = (obj.winfo_width(), obj.winfo_height(), obj.winfo_x(), obj.winfo_y())
  if fs == True:
    obj.place(x=0, y=0, relwidth=1, relheight=1)
    obj.configure(corner_radius=0)
  else:
    w, h, x, y = original
    obj.place(x=x, y=y, width=w, height=h)
    obj.configure(corner_radius=20)
    fs = False
