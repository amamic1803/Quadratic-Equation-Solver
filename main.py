from tkinter import *
import os
import sys


def resource_path(relative_path=""):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def rj_kvadratne(a, b, c):
	d = (b ** 2) - (4 * a * c)
	if d > 0:
		prvo = ((- b) - (d ** 0.5)) / (2 * a)
		drugo = ((- b) + (d ** 0.5)) / (2 * a)
		rjesenja = f"X₁ = {prvo}\nX₂ = {drugo}"
	elif d == 0:
		jedino = (- b) / (2 * a)
		rjesenja = f"X = {jedino}"
	else:
		real = (- b) / (2 * a)
		complx = ((- d) ** 0.5) / (2 * a)
		rjesenja = f"X₁ = {real} + {complx}i\nX₂ = {real} - {complx}i"

	return rjesenja

def klik():
	global lbl, a, b, c

	lbl.config(text=rj_kvadratne(float(a.get()), float(b.get()), float(c.get())))

def validate_input(full_text):
	if " " in full_text or "-" in full_text or full_text.count(".") > 1 or len(full_text) > 5:
		return False
	elif full_text == "" or full_text == ".":
		return True
	else:
		try:
			float(full_text)
			return True
		except ValueError:
			return False


if __name__ == '__main__':

	root = Tk()
	root.geometry(f"500x200+{root.winfo_screenwidth() // 2 - 250}+{root.winfo_screenheight() // 2 - 100}")
	root.resizable(False, False)
	root.title("Quadratic-Equation-Solver")
	root.iconbitmap(resource_path("icon.ico"))

	jednadzba = Label(root, text="ax² + bx + c = 0", font=("Arial", 20, "bold"), anchor="center")
	jednadzba.place(x=0, y=0, width=250, height=35)
	reg = root.register(validate_input)

	a = Entry(root)
	b = Entry(root)
	c = Entry(root)
	btn = Button(root, text="Calculate", command=klik)
	lbl = Label(root)
	a.place(x=33, y=47, width=35, height=25, anchor="center")
	b.place(x=105, y=47, width=35, height=25, anchor="center")
	c.place(x=168, y=47, width=35, height=25, anchor="center")
	btn.place(x=125, y=85, width=100, height=25, anchor="center")
	lbl.place(x=125, y=150, width=250, height=80, anchor="center")
	root.mainloop()
