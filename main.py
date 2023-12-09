import os
import sys
import tkinter as tk
from tkinter.messagebox import showerror


def resource_path(relative_path=""):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def rj_kvad(a, b, c):
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
			ispis = "X₁ = + i\nX₂ = - i"

	return ispis

def validate_number(full_text):
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

class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry(f"500x250"
		                   f"+{self.root.winfo_screenwidth() // 2 - 250}"
		                   f"+{self.root.winfo_screenheight() // 2 - 125}")
		self.root.resizable(False, False)
		self.root.title("Quadratic Equation Solver")
		self.root.iconbitmap(resource_path("resources/quad-icon.ico"))
		self.root.config(background="#202A44")

		self.title = tk.Label(self.root, text="Quadratic Equation Solver", font=("Helvetica", 25, "bold", "italic"),
		                      borderwidth=0, background="#202A44", activebackground="#202A44", foreground="#ffffff",
		                      activeforeground="#ffffff", highlightthickness=0)
		self.title.place(x=0, y=0, width=500, height=80)

		self.jednadzba = tk.Label(self.root, text="          X² +           X +           = 0",
		                          font=("Arial", 20, "bold"), anchor="center", borderwidth=0, background="#202A44",
		                          activebackground="#202A44", foreground="#ffffff", activeforeground="#ffffff",
		                          highlightthickness=0)
		self.jednadzba.place(x=0, y=92, width=500, height=35)

		self.reg = self.root.register(validate_number)

		self.a = tk.Entry(self.root, justify=tk.CENTER, font=("Arial", 13, "bold"),
		                  validate="key", validatecommand=(self.reg, "%P"),
		                  borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green",
		                  disabledbackground="grey15", disabledforeground="#ffffff", background="grey15",
		                  foreground="#ffffff", insertbackground="#ffffff")
		self.b = tk.Entry(self.root, justify=tk.CENTER, font=("Arial", 13, "bold"),
		                  validate="key", validatecommand=(self.reg, "%P"),
		                  borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green",
		                  disabledbackground="grey15", disabledforeground="#ffffff", background="grey15",
		                  foreground="#ffffff", insertbackground="#ffffff")
		self.c = tk.Entry(self.root, justify=tk.CENTER, font=("Arial", 13, "bold"),
		                  validate="key", validatecommand=(self.reg, "%P"),
		                  borderwidth=0, highlightthickness=1, highlightbackground="green", highlightcolor="green",
		                  disabledbackground="grey15", disabledforeground="#ffffff", background="grey15",
		                  foreground="#ffffff", insertbackground="#ffffff")
		self.a.place(x=54, y=90, width=75, height=35)
		self.b.place(x=193, y=90, width=75, height=35)
		self.c.place(x=323, y=90, width=75, height=35)

		self.result_lbl = tk.Label(self.root, text="", font=("Arial", 13, "bold"), anchor="center",
		                           borderwidth=0, background="#202A44", activebackground="#202A44",
		                           foreground="#ffffff", activeforeground="#ffffff", highlightthickness=0)
		self.result_lbl.place(x=0, y=130, width=500, height=70)

		self.solve_btn = tk.Label(self.root, text="Solve", font=("Helvetica", 10, "bold"), cursor="hand2",
		                          highlightthickness=1, highlightbackground="green", highlightcolor="green",
		                          borderwidth=0, background="grey15", activebackground="grey15", foreground="#ffffff",
		                          activeforeground="#ffffff")
		self.solve_btn.place(x=25, y=200, width=450, height=30)
		self.solve_btn.bind("<Enter>", lambda event: self.solve_btn.config(highlightthickness=3))
		self.solve_btn.bind("<Leave>", lambda event: self.solve_btn.config(highlightthickness=1))
		self.solve_btn.bind("<ButtonRelease-1>", lambda event: self.solve_click())
		self.root.bind("<KeyRelease-Return>", lambda event: self.solve_click())

		self.root.mainloop()

	def solve_click(self):
		err = False

		try:
			a_val = float(self.a.get())
		except ValueError:
			if self.a.get() != "":
				err = True
				self.a.delete(0, tk.END)
			else:
				a_val = 0

		try:
			b_val = float(self.b.get())
		except ValueError:
			if self.b.get() != "":
				err = True
				self.b.delete(0, tk.END)
			else:
				b_val = 0

		try:
			c_val = float(self.c.get())
		except ValueError:
			if self.c.get() != "":
				err = True
				self.c.delete(0, tk.END)
			else:
				c_val = 0

		if err:
			showerror("Invalid input!", "Invalid number was given!")
		else:
			self.result_lbl.config(text=rj_kvad(a_val, b_val, c_val))

def main():
	App()


if __name__ == '__main__':
	main()
