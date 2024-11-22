import tkinter as tk #tkinter ein gui tool kit

class TextBox:
    def __init__(self):
        self.root = tk.Tk() #fenster erstellen
        self.root.title("Text Box") #der title von der text box
        self.text_box = tk.Text(self.root, height=10, width=40) #die text box erstellen sowie einstellen
        self.text_box.pack() #keine ahnung was das sein soll
        self.button = tk.Button(self.root, text="Senden", command=self.check_input) #der button
        self.button.pack() #keine ahnung was das ist

    def check_input(self): #keine ahnung was das i
        input_text = self.text_box.get("1.0", tk.END) #keine ahnung was das ist
        input_text = input_text.lower() #keine ahnung was das ist

        if "hallo" in input_text:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "Hallo! Wie geht es dir?")
        elif "mir gehts gut und dir" in input_text:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "mir gehts gut danke")
        elif "bye" in input_text:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "Tschüss")
        else:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "Ich verstehe nicht, was du meinst.")

    def clear_text_box(self):
        self.text_box.delete("1.0", tk.END)

    def run(self): #keine ahnung was das ist
        self.root.mainloop() #keine ahnung was das ist

if __name__ == "__main__": #keine ahnung was das ist
    text_box = TextBox() #keine ahnung was das ist
    text_box.run() #keine ahnung was das ist