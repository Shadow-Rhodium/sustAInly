import tkinter as tk
from tkinter import messagebox
import pygame as VHS
import time as clock

print("""
 _____                       _____ 
( ___ )                     ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____   _   _  ____   |   | 
 |   | |  _ \ | \ | |/ ___|  |   | 
 |   | | | | ||  \| |\___ \  |   | 
 |   | | |_| || |\  | ___) | |   | 
 |   | |____/ |_| \_||____/  |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                     (_____)    
      """)

def mp3(dir):
    VHS.mixer.init()

    try:
        VHS.mixer.music.load(f"C:/Users/HassanHN/OneDrive/Desktop/Sustainly/{dir}")
        VHS.mixer.music.play()
        while VHS.mixer.music.get_busy():  
            clock.sleep(1) 

    except:
        print("No Sound File")

def open_sustania():
    messagebox.showinfo("Sustania", "Hello! I'm Sustania, your AI sustainability assistant. Let's reduce your carbon footprint together!")

def open_tracker():
    messagebox.showinfo("Carbon Tracker", "Track your travel, food, and energy habits here. Connected via blockchain for transparency!")

def open_plans():
    messagebox.showinfo("Custom Plans", "Your personalized sustainability plan: Reduce waste by 20% this month!")

def open_rewards():
    mp3("blipSelect.wav")
    messagebox.showinfo("Rewards", "You earned 50 points! Redeem discounts at eco-friendly stores with your MySustAlnly Card.")

def open_leaderboard():
    messagebox.showinfo("Leaderboard", "You're #3 in your community this week! Keep going!")

root = tk.Tk()
root.title("SustAlnly App")
root.geometry("400x300")
root.configure(bg="#f0f8f0")  # Light green 

# Label
title_label = tk.Label(
    root, 
    text="Welcome to SustAlnly", 
    font=("Helvetica", 16, "bold"), 
    bg="#f0f8f0", 
    fg="#2e8b57"  # Dark green 
)
title_label.pack(pady=10)

# Buttons 
button1 = tk.Button(
    root, 
    text="Meet Sustania (AI Assistant)", 
    command=open_sustania, 
    bg="#4caf50",  # Green
    fg="white",
    padx=10,
    pady=5
)
button1.pack(pady=5)

button2 = tk.Button(
    root, 
    text="Carbon Footprint Tracker", 
    command=open_tracker, 
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
button2.pack(pady=5)

button3 = tk.Button(
    root, 
    text="Custom Sustainability Plans", 
    command=open_plans, 
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
button3.pack(pady=5)

button4 = tk.Button(
    root, 
    text="Eco-Rewards", 
    command=open_rewards, 
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
button4.pack(pady=5)

button5 = tk.Button(
    root, 
    text="Community Leaderboard", 
    command=open_leaderboard, 
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
button5.pack(pady=5)

# Footer
footer_label = tk.Label(
    root, 
    text="Aligning with UN SDGs • UAE Green Agenda 2050", 
    font=("Helvetica", 8), 
    bg="#f0f8f0", 
    fg="#2e8b57"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()