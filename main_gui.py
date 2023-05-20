import tkinter as tk
from tkinter import messagebox
from main import *

class MainGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create the widgets
        self.label = tk.Label(self, text="Choose an encryption method:")
        self.label.pack()
        self.substitution_button = tk.Button(self, text="Substitution cipher", command=self.substitution_method)
        self.substitution_button.pack()
        self.caesar_button = tk.Button(self, text="Caesar cipher", command=self.caesar_method)
        self.caesar_button.pack()
        self.sha256_button = tk.Button(self, text="SHA-256 hash", command=self.sha256_method)
        self.sha256_button.pack()
        self.fernet_button = tk.Button(self, text="Fernet encryption", command=self.fernet_method)
        self.fernet_button.pack()

    def substitution_method(self):
        self.new_window()
        self.text_label = tk.Label(self.new_window, text="Enter the plaintext:")
        self.text_label.pack()
        self.text_entry = tk.Entry(self.new_window)
        self.text_entry.pack()
        self.key_label = tk.Label(self.new_window, text="Enter the substitution key:")
        self.key_label.pack()
        self.key_entry = tk.Entry(self.new_window)
        self.key_entry.pack()
        self.encrypt_button = tk.Button(self.new_window, text="Encrypt", command=self.encrypt_substitution)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(self.new_window, text="Decrypt", command=self.decrypt_substitution)
        self.decrypt_button.pack()

    def caesar_method(self):
        self.new_window()
        self.text_label = tk.Label(self.new_window, text="Enter the plaintext:")
        self.text_label.pack()
        self.text_entry = tk.Entry(self.new_window)
        self.text_entry.pack()
        self.key_label = tk.Label(self.new_window, text="Enter the Caesar shift key:")
        self.key_label.pack()
        self.key_entry = tk.Entry(self.new_window)
        self.key_entry.pack()
        self.encrypt_button = tk.Button(self.new_window, text="Encrypt", command=self.encrypt_caesar)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(self.new_window, text="Decrypt", command=self.decrypt_caesar)
        self.decrypt_button.pack()

    def sha256_method(self):
        self.new_window()
        self.text_label = tk.Label(self.new_window, text="Enter the message:")
        self.text_label.pack()
        self.text_entry = tk.Entry(self.new_window)
        self.text_entry.pack()
        self.hash_button = tk.Button(self.new_window, text="Hash", command=self.hash_sha256)
        self.hash_button.pack()

    def fernet_method(self):
        self.new_window()
        self.text_label = tk.Label(self.new_window, text="Enter the message:")
        self.text_label.pack()
        self.text_entry = tk.Entry(self.new_window)
        self.text_entry.pack()
        self.key_label = tk.Label(self.new_window, text="Enter the encryption key (leave blank to generate a new key):")
        self.key_label.pack()
        self.key_entry = tk.Entry(self.new_window)
        self.key_entry.pack()
        self.encrypt_button = tk.Button(self.new_window, text="Encrypt", command=self.encrypt_fernet)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(self.new_window, text="Decrypt", command=self.decrypt_fernet)
        self.decrypt_button.pack()


    # continue adding more widgets as needed
