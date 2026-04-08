import tkinter as tk
from tkinter import ttk
from ticket_logic import submit_ticket_logic

# Define button functions
def submit_ticket():
    """Submit ticket function."""
    member_id = member_id_entry.get()
    ticket_notes = ticket_notes_entry.get("1.0", tk.END)
    submit_ticket_logic(member_id, ticket_notes)
    member_id_entry.delete(0, tk.END)
    ticket_notes_entry.delete("1.0", tk.END)

def switch_to_home():
    """Switch to home screen function."""
    pass

def switch_to_my_tickets():
    """Switch to my tickets screen function."""
    pass

# Define hover effects
def on_enter(e):
    """Change button color on hover."""
    e.widget.config(background='#0A3891')

def on_leave(e):
    """Revert button color when not hovering."""
    e.widget.config(background='#1866FF')

# Create main application window
root = tk.Tk()
root.title("eSMT Triage Assistant")

# Configure styles
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Arial', 10), background='#1866FF', foreground='white')
style.configure('TEntry', relief='solid', borderwidth=1)
style.configure('TLabel', font=('Arial', 10))
style.configure('TText', relief='solid', borderwidth=1)
style.configure('Header.TLabel', font=('Arial', 12, 'bold'))

# Main frame setup
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Navigation frame setup
top_frame = tk.Frame(main_frame, bg='#0A3891')
main_frame.columnconfigure(0, weight=1)
top_frame.grid(row=0, column=0, sticky='ew')

# Navigation buttons
home_button = tk.Button(top_frame, text="Home", bg='#1866FF', fg='white', command=switch_to_home)
my_tickets_button = tk.Button(top_frame, text="My Tickets", bg='#1866FF', fg='white', command=switch_to_my_tickets)
home_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
my_tickets_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Bind hover effects to navigation buttons
home_button.bind("<Enter>", on_enter)
home_button.bind("<Leave>", on_leave)
my_tickets_button.bind("<Enter>", on_enter)
my_tickets_button.bind("<Leave>", on_leave)

# Ticket entry frame setup
ticket_frame = tk.Frame(main_frame, bg='white')
ticket_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
main_frame.rowconfigure(1, weight=1)
ticket_frame.columnconfigure(1, weight=1)

# Ticket entry widgets
title_label = ttk.Label(ticket_frame, text="Ticket Entry Form", style='Header.TLabel', background='white')
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Member ID input
member_id_label = ttk.Label(ticket_frame, text="Enter member ID: ", style='TLabel', background='white')
member_id_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
member_id_entry = tk.Entry(ticket_frame, relief='solid', borderwidth=1, width=30)
member_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky=(tk.W+tk.E))

# Ticket notes input
ticket_notes_label = ttk.Label(ticket_frame, text="Enter ticket notes: ", style='TLabel', background='white')
ticket_notes_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
ticket_notes_entry = tk.Text(ticket_frame, height=5, width=30, relief='solid', borderwidth=1)
ticket_notes_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=(tk.W+tk.E))

# Submit button
submit_button = tk.Button(ticket_frame, text="Submit", bg='#1866FF', fg='white', command=submit_ticket)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Bind hover effects to submit button
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)

root.mainloop()
