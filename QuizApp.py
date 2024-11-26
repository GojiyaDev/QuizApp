import tkinter as tk
from tkinter import ttk, messagebox

# Questions, options, and answers
questions = [
    "What is the output of print(2 ** 3)?",
    "Which of these is not a valid Python data type?",
    "What does the 'len()' function do?",
    "Which keyword is used to define a function in Python?",
    "What is the correct syntax to output 'Hello World' in Python?"
]

options = [
    ["6", "8", "9", "Error"],
    ["List", "Tuple", "Map", "Dictionary"],
    ["Returns size of object", "Returns length of iterable", "Both", "None"],
    ["func", "function", "def", "lambda"],
    ["echo('Hello World')", "print('Hello World')", "write('Hello World')", "output('Hello World')"]
]

answers = [1, 2, 2, 2, 1]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.root.geometry("600x400")
        self.root.configure(bg="#f7f7f7")

        self.index = 0
        self.score = 0
        self.time_remaining = 30
        self.timer_job = None

        # Title Label
        self.title_label = ttk.Label(
            self.root, text="Python Quiz", font=("Arial", 24, "bold"), background="#f7f7f7", foreground="#333"
        )
        self.title_label.pack(pady=10)

        # Timer Label
        self.timer_label = ttk.Label(
            self.root, text=f"Time left: {self.time_remaining}s", font=("Arial", 14), background="#f7f7f7", foreground="red"
        )
        self.timer_label.pack(pady=5)

        # Question Label
        self.question_label = ttk.Label(
            self.root, text=questions[self.index], font=("Arial", 14), wraplength=500, background="#f7f7f7", anchor="center"
        )
        self.question_label.pack(pady=20)

        # Options as radio buttons
        self.options = tk.StringVar(value=-1)
        self.radio_buttons = []
        for i in range(4):
            rb = ttk.Radiobutton(self.root, text="", variable=self.options, value=i)
            rb.pack(anchor="w", padx=50, pady=5)
            self.radio_buttons.append(rb)

        # Next Button
        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
        

        self.display_question()
        self.update_timer()

    def display_question(self):
        """Display the current question and reset the timer."""
        self.question_label.config(text=questions[self.index])
        self.options.set(-1)  # Reset the selected option
        for i, text in enumerate(options[self.index]):
            self.radio_buttons[i].config(text=text)
        self.time_remaining = 30
        self.timer_label.config(text=f"Time left: {self.time_remaining}s")

    def update_timer(self):
        """Update the timer for the current question."""
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time left: {self.time_remaining}s")
            self.timer_job = self.root.after(1000, self.update_timer)
        else:
            self.next_question()  # Move to the next question if time runs out

    def next_question(self):
        """Handle the transition to the next question or display results."""
        # Cancel any pending timer updates
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        if self.options.get() == str(answers[self.index]):
            self.score += 1  # Increase score for the correct answer

        self.index += 1
        if self.index < len(questions):
            self.display_question()
            self.update_timer()  # Restart the timer for the new question
        else:
            self.show_result()

    def show_result(self):
        """Display the final score and close the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(questions)}!")
        self.root.destroy()


# Main application
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
