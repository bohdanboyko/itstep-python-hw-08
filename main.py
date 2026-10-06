import tkinter as tk
from tkinter import messagebox, ttk


# ---------------- ЗАВДАННЯ 1 ----------------
def task1():
    window = tk.Toplevel(root)
    window.title("Завдання 1")
    window.geometry("300x150")

    tk.Label(window, text="Натисніть кнопку для виходу").pack(pady=20)
    tk.Button(window, text="Вихід", command=window.destroy).pack()


# ---------------- ЗАВДАННЯ 2 ----------------
def task2():
    window = tk.Toplevel(root)
    window.title("Завдання 2")
    window.geometry("400x200")

    entry = tk.Entry(window, width=35)
    entry.pack(pady=20)

    label = tk.Label(window, text="Тут з'явиться введений текст")
    label.pack(pady=10)

    def confirm():
        label.config(text=entry.get())

    tk.Button(window, text="Підтвердити", command=confirm).pack()


# ---------------- ЗАВДАННЯ 3 ----------------
def task3():
    window = tk.Toplevel(root)
    window.title("Завдання 3")
    window.geometry("300x250")

    language = tk.StringVar(value="Українська")

    tk.Label(window, text="Оберіть мову:").pack(pady=10)

    languages = ["Українська", "Англійська", "Німецька"]

    for lang in languages:
        tk.Radiobutton(
            window,
            text=lang,
            variable=language,
            value=lang,
            command=lambda: messagebox.showinfo(
                "Мова", f"Ви обрали: {language.get()}"
            )
        ).pack(anchor="w", padx=80)


# ---------------- ЗАВДАННЯ 4 ----------------
def task4():
    window = tk.Toplevel(root)
    window.title("Завдання 4")
    window.geometry("350x250")

    tk.Label(window, text="Оберіть день:").pack(pady=5)

    days = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П'ятниця",
        "Субота",
        "Неділя"
    ]

    day_box = ttk.Combobox(window, values=days, state="readonly")
    day_box.pack(pady=5)

    tk.Label(window, text="Оберіть місяць:").pack(pady=5)

    months = [
        "Січень", "Лютий", "Березень", "Квітень",
        "Травень", "Червень", "Липень", "Серпень",
        "Вересень", "Жовтень", "Листопад", "Грудень"
    ]

    month_box = ttk.Combobox(window, values=months, state="readonly")
    month_box.pack(pady=5)

    def show_date():
        day = day_box.get()
        month = month_box.get()

        if day and month:
            messagebox.showinfo(
                "Обрана дата",
                f"Ви обрали: {day}, {month}"
            )

    tk.Button(window, text="Підтвердити", command=show_date).pack(pady=15)


# ---------------- ЗАВДАННЯ 5 ----------------
def task5():
    window = tk.Toplevel(root)
    window.title("Завдання 5 — Калькулятор")
    window.geometry("350x450")

    expression = tk.StringVar()

    display = tk.Entry(
        window,
        textvariable=expression,
        font=("Arial", 20),
        justify="right"
    )
    display.pack(fill="x", padx=10, pady=10)

    def add(value):
        expression.set(expression.get() + str(value))

    def clear():
        expression.set("")

    def calculate():
        try:
            result = eval(expression.get())
            expression.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Помилка", "Ділення на нуль неможливе!")
        except Exception:
            messagebox.showerror("Помилка", "Неправильний вираз!")

    buttons = [
        ("7", lambda: add(7)),
        ("8", lambda: add(8)),
        ("9", lambda: add(9)),
        ("/", lambda: add("/")),

        ("4", lambda: add(4)),
        ("5", lambda: add(5)),
        ("6", lambda: add(6)),
        ("*", lambda: add("*")),

        ("1", lambda: add(1)),
        ("2", lambda: add(2)),
        ("3", lambda: add(3)),
        ("-", lambda: add("-")),

        ("0", lambda: add(0)),
        (".", lambda: add(".")),
        ("+", lambda: add("+")),
        ("C", clear),
    ]

    frame = tk.Frame(window)
    frame.pack()

    row = 0
    col = 0

    for text, command in buttons:
        tk.Button(
            frame,
            text=text,
            width=6,
            height=2,
            command=command
        ).grid(row=row, column=col, padx=3, pady=3)

        col += 1

        if col == 4:
            col = 0
            row += 1

    tk.Button(
        window,
        text="Результат",
        width=25,
        height=2,
        command=calculate
    ).pack(pady=15)


# ---------------- ГОЛОВНЕ ВІКНО ----------------
root = tk.Tk()
root.title("Практична робота — Tkinter")
root.geometry("400x400")

tk.Label(
    root,
    text="Практична робота",
    font=("Arial", 18, "bold")
).pack(pady=20)

tk.Button(root, text="Завдання 1 — Вихід",
          width=30, command=task1).pack(pady=5)

tk.Button(root, text="Завдання 2 — Поле вводу",
          width=30, command=task2).pack(pady=5)

tk.Button(root, text="Завдання 3 — Вибір мови",
          width=30, command=task3).pack(pady=5)

tk.Button(root, text="Завдання 4 — День і місяць",
          width=30, command=task4).pack(pady=5)

tk.Button(root, text="Завдання 5 — Калькулятор",
          width=30, command=task5).pack(pady=5)

tk.Button(
    root,
    text="Закрити програму",
    width=30,
    command=root.destroy
).pack(pady=20)

root.mainloop()