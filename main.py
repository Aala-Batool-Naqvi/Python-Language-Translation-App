# Importing libraries
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the Tkinter window
window = tk.Tk()
window.title("Language Translation App")
window.geometry("600x500")
window.configure(bg="#2e2e2e")  # Dark gray background

# Initialize the Translator
translator = Translator()

# Function to translate text
def translate_text():
    # Get the source and target languages from full names
    source_lang = language_codes[source_lang_combobox.get()]
    target_lang = language_codes[target_lang_combobox.get()]
    
    # Get the text to be translated
    text = source_text.get("1.0", "end-1c")
    
    # Translate the text
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    
    # Display the translated text
    target_text.delete("1.0", "end")
    target_text.insert("1.0", translated.text)

# Language name to code mapping
language_codes = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Hindi': 'hi',
    'Urdu': 'ur',
    'Arabic': 'ar',
    'Korean': 'ko',
    'Turkish': 'tr',
    'Dutch': 'nl',
    'Polish': 'pl',
    'Swedish': 'sv',
    'Greek': 'el',
    'Thai': 'th',
    'Vietnamese': 'vi',
    'Bengali': 'bn'
}

# Set styles for the widgets
style = ttk.Style()
style.configure('TLabel', background="#2e2e2e", foreground="white", font=('Helvetica', 12, 'bold'))  # White text on dark gray background
style.configure('TButton', background="#4CAF50", foreground="white", font=('Helvetica', 12, 'bold'))  # Green button with white text
style.configure('TCombobox', font=('Helvetica', 10))

# Create a frame to hold the input/output sections
frame = tk.Frame(window, bg="#444444", bd=2, relief=tk.SUNKEN)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Create the source language selection dropdown
source_lang_label = ttk.Label(frame, text="Source Language:")
source_lang_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
source_lang_combobox = ttk.Combobox(frame, values=list(language_codes.keys()), state="readonly")
source_lang_combobox.set("English")  # Default to English
source_lang_combobox.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

# Create the source text area
source_text_label = ttk.Label(frame, text="Enter text:")
source_text_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
source_text = tk.Text(frame, height=5, width=50, font=('Helvetica', 10))
source_text.grid(row=1, column=1, pady=10, padx=10)

# Create the target language selection dropdown
target_lang_label = ttk.Label(frame, text="Target Language:")
target_lang_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
target_lang_combobox = ttk.Combobox(frame, values=list(language_codes.keys()), state="readonly")
target_lang_combobox.set("Spanish")  # Default to Spanish
target_lang_combobox.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

# Create the target text area for the translation result
target_text_label = ttk.Label(frame, text="Translated text:")
target_text_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")
target_text = tk.Text(frame, height=5, width=50, font=('Helvetica', 10), bg="#f1f8e9")
target_text.grid(row=3, column=1, pady=10, padx=10)

# Create the Translate button
translate_button = tk.Button(window, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'), padx=10, pady=5)  # Green button with white text
translate_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
