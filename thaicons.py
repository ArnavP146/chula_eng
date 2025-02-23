import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai (Chicken)"),
    ("ข", "Khor Khai (Egg)"),
    ("ค", "Khor Khuat (Bottle)"),
    ("ง", "Ngor Ngu (Snake)"),
    ("จ", "Jor Jaan (Plate)"),
    ("ฉ", "Chor Ching (Cymbals)"),
    ("ช", "Chor Chang (Elephant)"),
    ("ด", "Dor Dek (Child)"),
    ("ต", "Tor Tao (Turtle)"),
    ("ป", "Por Pla (Fish)"),
    ("พ", "Por Phan (Tray)"),
    ("ม", "Mor Ma (Horse)"),
    ("ร", "Ror Reua (Boat)"),
    ("ล", "Lor Ling (Monkey)"),
    ("ว", "Wor Waen (Ring)")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_front = True
        self.current_card = random.choice(thai_consonants)
        
        self.label = tk.Label(root, text=self.current_card[0], font=("Arial", 50))
        self.label.pack(pady=20)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()
    
    def flip_card(self):
        if self.card_front:
            self.label.config(text=self.current_card[1])
        else:
            self.label.config(text=self.current_card[0])
        self.card_front = not self.card_front
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_front = True
        self.label.config(text=self.current_card[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
