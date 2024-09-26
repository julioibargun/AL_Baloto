import tkinter as tk
from tkinter import ttk
import alg2


def submit_form():
   # Retrieve values from the form
   number_poblacion = entry_poblacion.get()
   number_iterations = entry_interatione.get()
   objetivo = entry_objetivo.get()
   max_cru_pob = entry_al_poblation.get()
   r1, r2, iter, obj = alg2.mainExce(number_poblacion, number_iterations, objetivo, max_cru_pob)
 


   # Display the submitted information in blue color
   result_label.config(text=f"Solucion!\n"
                             f"Objetivo: {obj}\n"
                             f"Iteraciones: {iter}\n"
                             f"Mejor resultado 1: {r1}\n"
                             f"Mejor resultado 2: {r2}\n")

root = tk.Tk()
root.title("Flood-Registration Form")
root.geometry("400x400")
root.configure(bg="lightgreen")

# Create labels
label_number_poblacion = ttk.Label(root, text="Poblacion Aleatoria:", foreground="purple")
label_number_iterations = ttk.Label(root, text="Maximo Iteraciones:", foreground="purple")
label_objetivo = ttk.Label(root, text="Obejtivo:", foreground="purple")
label_max_cru_pobr = ttk.Label(root, text="mamximo poblacion cruzada:", foreground="purple")

# Create entry widgets
entry_poblacion = ttk.Entry(root)
entry_interatione = ttk.Entry(root)
entry_objetivo = ttk.Entry(root)
entry_al_poblation = ttk.Entry(root)



# Create submit button
submit_button = ttk.Button(root, text="iniciar", command=submit_form, style="TButton")
# Create label for displaying the result
result_label = ttk.Label(root, text="", foreground="blue")

# Place widgets on the grid
label_number_poblacion.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_number_iterations.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_objetivo.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_max_cru_pobr.grid(row=3, column=0, padx=10, pady=5, sticky="w")



entry_poblacion.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_interatione.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_objetivo.grid(row=2, column=1, padx=10, pady=5, sticky="w")
entry_al_poblation.grid(row=3, column=1, padx=10, pady=5, sticky="w")

submit_button.grid(row=6, column=0, columnspan=2, pady=10)
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Configure style for the submit button
style = ttk.Style()
style.configure("TButton", foreground="red")

# Run the Tkinter main loop
root.mainloop()