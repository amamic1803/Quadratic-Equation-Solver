import os
import sys
from tkinter import *
from tkinter.messagebox import showerror


def resource_path(relative_path=""):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def rj_kvadratne(a, b, c):
	rjesenja = []
	kompleksna = False
	if a == 0:
		if b != 0:
			rjesenja.append(- c / b)
		else:
			return ""
	else:
		d = (b ** 2) - (4 * a * c)
		if d > 0:
			rjesenja.extend((((- b) - (d ** 0.5)) / (2 * a), ((- b) + (d ** 0.5)) / (2 * a)))
		elif d == 0:
			rjesenja.append((- b) / (2 * a))
		else:
			rjesenja.extend(((- b) / (2 * a), ((- d) ** 0.5) / (2 * a)))
			kompleksna = True

	for i in range(len(rjesenja)):
		if rjesenja[i] == 0:
			rjesenja.pop(i)
			rjesenja.insert(i, 0)
		elif abs(round(rjesenja[i], 0) - rjesenja[i]) < 0.00001:
			temp = int(round(rjesenja[i], 0))
			rjesenja.pop(i)
			rjesenja.insert(i, temp)

	for i in range(len(rjesenja)):
		temp = rjesenja[i]
		rjesenja.pop(i)
		if temp < 0:
			rjesenja.insert(i, f"- {abs(temp)}")
		else:
			rjesenja.insert(i, temp)

	if len(rjesenja) == 2 and not kompleksna:
		ispis = f"X₁ = {rjesenja[0]}\nX₂ = {rjesenja[1]}"
	elif len(rjesenja) == 1:
		ispis = f"X = {rjesenja[0]}"
	else:
		if rjesenja[0] != 0 and rjesenja[1] != 1:
			ispis = f"X₁ = {rjesenja[0]} + {rjesenja[1]}i\nX₂ = {rjesenja[0]} - {rjesenja[1]}i"
		elif rjesenja[0] == 0 and rjesenja[1] != 1:
			ispis = f"X₁ = + {rjesenja[1]}i\nX₂ = - {rjesenja[1]}i"
		elif rjesenja[0] != 0 and rjesenja[1] == 1:
			ispis = f"X₁ = {rjesenja[0]} + i\nX₂ = {rjesenja[0]} - i"
		else:
			ispis = f"X₁ = + i\nX₂ = - i"

	return ispis

def klik(event=None):
	global lbl, a, b, c

	err = False

	try:
		a_val = float(a.get())
	except ValueError:
		if a.get() != "":
			err = True
			a.delete(0, END)
		else:
			a_val = 0

	try:
		b_val = float(b.get())
	except ValueError:
		if b.get() != "":
			err = True
			b.delete(0, END)
		else:
			b_val = 0

	try:
		c_val = float(c.get())
	except ValueError:
		if c.get() != "":
			err = True
			c.delete(0, END)
		else:
			c_val = 0

	if err:
		showerror("Invalid input!", "Invalid number was given!")
	else:
		lbl.config(text=rj_kvadratne(a_val, b_val, c_val))

def validate_input(full_text):
	if " " in full_text or full_text.count(".") > 1:
		return False
	elif full_text == "" or full_text == "." or full_text == "-":
		return True
	else:
		try:
			float(full_text)
			if len(full_text) < 12:
				return True
			else:
				return False
		except ValueError:
			return False

def convert_change_thickness(event, typ):
	global convert_btn
	if typ:
		convert_btn.config(highlightthickness=1)
	else:
		convert_btn.config(highlightthickness=3)

def main():
	global convert_btn
	global lbl, a, b, c

	root = Tk()
	root.geometry(f"500x250+{root.winfo_screenwidth() // 2 - 250}+{root.winfo_screenheight() // 2 - 125}")
	root.resizable(False, False)
	root.title("Quadratic Equation Solver")
	root.iconbitmap(resource_path("data/quad-eq-solver-icon.ico"))
	root.config(background="#202A44")

	title = Label(root, text="Quadratic Equation Solver", font=("Helvetica", 25, "bold", "italic"), borderwidth=0, background="#202A44", activebackground="#202A44", foreground="#ffffff", activeforeground="#ffffff", highlightthickness=0)
	title.place(x=0, y=0, width=500, height=80)

	jednadzba = Label(root, text="          X² +           X +           = 0", font=("Arial", 20, "bold"), anchor="center", borderwidth=0, background="#202A44", activebackground="#202A44", foreground="#ffffff", activeforeground="#ffffff", highlightthickness=0)
	jednadzba.place(x=0, y=90, width=500, height=35)
	reg = root.register(validate_input)

	a = Entry(root, justify=CENTER, validate="key", validatecommand=(reg, "%P"), borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green", disabledbackground="grey15", disabledforeground="#ffffff", background="grey15", foreground="#ffffff", insertbackground="#ffffff")
	b = Entry(root, justify=CENTER, validate="key", validatecommand=(reg, "%P"), borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green", disabledbackground="grey15", disabledforeground="#ffffff", background="grey15", foreground="#ffffff", insertbackground="#ffffff")
	c = Entry(root, justify=CENTER, validate="key", validatecommand=(reg, "%P"), borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green", disabledbackground="grey15", disabledforeground="#ffffff", background="grey15", foreground="#ffffff", insertbackground="#ffffff")
	lbl = Label(root, text="", font=("Arial", 13, "bold"), anchor="center", borderwidth=0, background="#202A44", activebackground="#202A44", foreground="#ffffff", activeforeground="#ffffff", highlightthickness=0)
	a.place(x=54, y=90, width=75, height=35)
	b.place(x=193, y=90, width=75, height=35)
	c.place(x=323, y=90, width=75, height=35)

	convert_btn = Label(root, text="Solve", font=("Helvetica", 10, "bold"), highlightthickness=1, highlightbackground="green", highlightcolor="green", borderwidth=0, background="grey15", activebackground="grey15", foreground="#ffffff", activeforeground="#ffffff")
	convert_btn.place(x=25, y=215, width=450, height=30)
	convert_btn.bind("<Enter>", lambda event: convert_change_thickness(event, False))
	convert_btn.bind("<Leave>", lambda event: convert_change_thickness(event, True))
	convert_btn.bind("<ButtonRelease-1>", klik)

	root.bind("<KeyRelease-Return>", klik)

	lbl.place(x=0, y=130, width=500, height=90)
	root.mainloop()


if __name__ == '__main__':
	main()
