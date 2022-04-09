from logging import root
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt?")
    return task

def get_message():
    message = simpledialog.askstring("Message", "Enter the secret message: ")
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message): # Runs through each letter of the message, adding the even letters to a list.
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message): # Runs through each letter of the message, adding the odd letters to a list.
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + "x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = "".join(letter_list)
    return new_message

def encrypt(message):
    swapped_message = swap_letters(message)
    encrypted_message = "".join(reversed(swapped_message))
    return encrypted_message

def decrypt(message):
    unreversed_message = "".join(reversed(message))
    decrypted_message = swap_letters(unreversed_message)
    return decrypted_message

root = tk.Tk()
root.withdraw()

while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo("Ciphertext of the secret message is:", encrypted)
    elif task == "decrypt":
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo("Plaintext of the secret message is:", decrypted)
    else:
        break

root.mainloop()