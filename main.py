import tkinter as tk
from function import evaluate_expression, add_to_history, clear_history

def on_button_click(event):
    current_text = entry.get()
    new_text = current_text + event.widget.cget("text")
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def on_equal_button_click(event):
    current_text = entry.get()
    result = evaluate_expression(current_text)
    entry.delete(0, tk.END)
    entry.insert(0, result)
    add_to_history(calculation_history, current_text, result)

#
def clear(event):
    entry.delete(0, tk.END)

#история ввода
def history():
    history_window = tk.Toplevel(root)
    history_window.title("История расчетов")
    history_list = tk.Listbox(history_window, width=40, height=20)
    history_list.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar = tk.Scrollbar(history_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    history_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=history_list.yview)

    for item in calculation_history:
        history_list.insert(tk.END, item)

def on_key_press(event):
    return "break"

root = tk.Tk()
root.title("Калькулятор")
root.geometry("387x365")  # Set fixed width of 387px and initial height of 500px
root.resizable(False, False)  # Disable resizing

# Виджет для ввода
entry = tk.Entry(root, width=15, font=('Arial', 26), borderwidth=2, relief="solid", show="")
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")
entry.bind('<KeyPress>', on_key_press)

# Кнопка для полной очистки ввода
clear_all_button = tk.Button(root, text="AC", font=('Arial', 18), width=2, height=1)
clear_all_button.grid(row=0, column=3, pady=5, padx=41)
clear_all_button.bind('<ButtonPress-1>', clear)

# Кнопка для просмотра истории расчетов
history_button = tk.Button(root, text="→", font=('Arial', 18), width=2, height=1, command=history)
history_button.grid(row=0, column=3, pady=5, sticky="w")

# Инициализация истории расчетов
calculation_history = clear_history()

# Определяем кнопки калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Создаем кнопки и размещаем их
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 18), width=5, height=2)
    button.grid(row=row_val, column=col_val, padx=0, pady=1, sticky="w")
    if button_text not in {'=', 'C'}:
        button.bind('<Button-1>', on_button_click)
    if button_text == '=':
        button.bind('<Button-1>', on_equal_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
