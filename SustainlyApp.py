import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser as internet
from datetime import datetime
import google.generativeai as Sustainia
import random as dice
import pygame as VHS
import time as clock
from pyautogui import alert 

def voice(dir):
    VHS.mixer.init()

    try:
        VHS.mixer.music.load(f"C:/Users/HassanHN/OneDrive/Desktop/Sustainly/{dir}")
        VHS.mixer.music.play()
        while VHS.mixer.music.get_busy():  
            clock.sleep(1) 

    except:
        alert(text='No Sound File', title='ERROR', button='OK')

footprint = "Undefined kg Co2"

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
    }

model = Sustainia.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

chat_session = model.start_chat(history=[])

Sustainia.configure(api_key="REDACTED")



# ======================
#  CONSTANTS & SETTINGS
# ======================
DARK_GREEN = "#2e8b57"
LIGHT_GREEN = "#e6f2f2"
ACCENT_GOLD = "#f2c94c"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_MAIN = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")  # Added missing font definition
FONT_TITLE = ("Segoe UI Semibold", 14)

# Simulated user data
current_user = None
selected_interests = []

# ======================
#  WELCOME SCREEN
# ======================
def show_welcome_screen():
    clear_window()
    # Header
    header = tk.Frame(root, bg=DARK_GREEN, height=80)
    header.pack(fill="x")
    tk.Label(header, text="♻️ Sustainly", 
                     font=("Helvetica", 20, "bold"), 
                     fg=WHITE, 
                     bg=DARK_GREEN,
                     padx=10,
                     pady=10).pack(pady=20)
    
    # Main content
    content = tk.Frame(root, bg=LIGHT_GREEN)
    content.pack(fill="both", expand=True, padx=40, pady=40)
    
    tk.Label(content, 
            text="Welcome to Sustainly", 
            font=FONT_TITLE, 
            bg=LIGHT_GREEN).pack(pady=(0, 20))
    
    tk.Label(content, 
            text="Track your carbon footprint and live sustainably", 
            font=FONT_MAIN, 
            bg=LIGHT_GREEN).pack(pady=(0, 40))
    
    # Sign Up/Login Buttons
    btn_frame = tk.Frame(content, bg=LIGHT_GREEN)
    btn_frame.pack(fill="x")
    
    ttk.Button(btn_frame, 
              text="Sign Up with Email", 
              command=show_email_signup,
              style="Gold.TButton").pack(fill="x", pady=5)
    
    ttk.Button(btn_frame, 
              text="Continue with Google", 
              command=lambda: oauth_login("Google"),
              style="Gold.TButton").pack(fill="x", pady=5)
    
    ttk.Button(btn_frame, 
              text="Continue with Apple", 
              command=lambda: oauth_login("Apple"),
              style="Gold.TButton").pack(fill="x", pady=5)
    
    ttk.Button(btn_frame, 
              text="Continue as Guest", 
              command=guest_login,
              style="White.TButton").pack(fill="x", pady=(20, 5))
    
    voice("Open.mp3")


# ======================
#  EMAIL SIGNUP FLOW
# ======================
def show_email_signup():
    clear_window()
    
    content = tk.Frame(root, bg=LIGHT_GREEN)
    content.pack(fill="both", expand=True, padx=40, pady=20)
    
    tk.Label(content, 
            text="Create Your Account", 
            font=FONT_TITLE, 
            bg=LIGHT_GREEN).pack(pady=(0, 20))
    
    # Form fields
    fields = [
        {"label": "Full Name", "type": "entry"},
        {"label": "Email", "type": "entry"},
        {"label": "Password", "type": "entry", "show": "*"},
        {"label": "Confirm Password", "type": "entry", "show": "*"}
    ]
    
    entries = []
    for field in fields:
        frame = tk.Frame(content, bg=LIGHT_GREEN)
        frame.pack(fill="x", pady=5)
        
        tk.Label(frame, 
                text=field["label"], 
                font=FONT_MAIN, 
                bg=LIGHT_GREEN, 
                width=20, 
                anchor="w").pack(side="left")
        
        if field.get("show"):
            entry = ttk.Entry(frame, show=field["show"])
        else:
            entry = ttk.Entry(frame)
        entry.pack(side="right", expand=True, fill="x")
        entries.append(entry)
    
    # Action buttons
    btn_frame = tk.Frame(content, bg=LIGHT_GREEN)
    btn_frame.pack(fill="x", pady=(20, 0))
    
    ttk.Button(btn_frame, 
              text="Create Account", 
              command=lambda: validate_signup(entries),
              style="Gold.TButton").pack(fill="x")
    
    ttk.Button(btn_frame, 
              text="Back", 
              command=show_welcome_screen,
              style="White.TButton").pack(fill="x", pady=5)

def validate_signup(entries):
    # Simple validation
    if not all(entry.get() for entry in entries):
        messagebox.showerror("Error", "All fields are required")
        return
    
    if entries[2].get() != entries[3].get():
        messagebox.showerror("Error", "Passwords don't match")
        return
    
    global current_user
    current_user = {
        "name": entries[0].get(),
        "email": entries[1].get(),
        "password": entries[2].get()
    }
    
    show_interest_selection()

# ======================
#  OAUTH & GUEST LOGIN
# ======================
def oauth_login(provider):
    messagebox.showinfo("Info", f"Redirecting to {provider} authentication...")
    # Simulate successful login
    global current_user
    current_user = {"name": f"{provider} User", "email": f"user@{provider.lower()}.com"}
    show_interest_selection()

def guest_login():
    global current_user
    current_user = {"name": "Guest User", "email": None}
    show_home_screen()

# ======================
#  INTEREST SELECTION
# ======================
def show_interest_selection():
    clear_window()
    
    content = tk.Frame(root, bg=LIGHT_GREEN)
    content.pack(fill="both", expand=True, padx=20, pady=20)
    
    tk.Label(content, 
            text="Select Your Interests", 
            font=FONT_TITLE, 
            bg=LIGHT_GREEN).pack(pady=(0, 20))
    
    tk.Label(content, 
            text="Choose at least one to personalize your experience", 
            font=FONT_MAIN, 
            bg=LIGHT_GREEN).pack(pady=(0, 20))
    
    # Interest checkboxes
    interests = [
        "Fashion", "Travel", "Sports", "Beauty",
        "Education & Awareness", "Technology",
        "Community Events", "Finance"
    ]
    
    interest_vars = []
    for interest in interests:
        var = tk.IntVar()
        frame = tk.Frame(content, bg=LIGHT_GREEN)
        frame.pack(fill="x", pady=2)
        
        ttk.Checkbutton(frame, 
                       text=interest, 
                       variable=var,
                       style="Green.TCheckbutton").pack(side="left")
        interest_vars.append((interest, var))
    
    # Continue button
    btn_frame = tk.Frame(content, bg=LIGHT_GREEN)
    btn_frame.pack(fill="x", pady=(30, 0))
    
    ttk.Button(btn_frame, 
              text="Continue", 
              command=lambda: save_interests(interest_vars),
              style="Gold.TButton").pack(fill="x")

def save_interests(interest_vars):
    global selected_interests
    selected_interests = [interest for interest, var in interest_vars if var.get()]
    
    if not selected_interests:
        messagebox.showerror("Error", "Please select at least one interest")
        return
    
    # In a real app, save to database here
    messagebox.showinfo("Success", f"Saved {len(selected_interests)} interest(s)!")
    show_home_screen()

# ======================
#  HOME SCREEN 
# ======================
def show_home_screen():
    clear_window()
    
    # Header with time
    # Header
    header = tk.Frame(root, bg=DARK_GREEN, height=80)
    header.pack(fill="x")
    tk.Label(header, text="♻️ Sustainly", 
                     font=("Helvetica", 20, "bold"), 
                     fg=WHITE, 
                     bg=DARK_GREEN,
                     padx=10,
                     pady=10).pack(pady=20)
    

    calculation_history = []
    def calculate():
        global footprint
        electricity_factor = 0.5
        fuel_factor = 2.3
        transport_factor = 0.5
        

        try:
            # Get values
            electricity = float( elec_entry.get())
            fuel = float( fuel_entry.get())
            transport = float( transport_entry.get())
            
            # Calculate
            elec_emission = electricity *  electricity_factor
            fuel_emission = fuel *  fuel_factor
            transport_emission = transport *  transport_factor
            total = elec_emission + fuel_emission + transport_emission
            footprint = f"{total} kg CO2"
            
            # Color coding
            if total < 5:
                color = DARK_GREEN
                advice = "(Excellent! Keep it up!)"
                voice("low.wav")
            elif total < 15:
                color = "#FFA500"
                advice = "(Moderate impact)"
                voice("mid.wav")
            else:
                color = "#FF4500"
                advice = "(High impact)"
                voice("high.wav")
            
            # Current result
            result_text = f"Carbon Footprint: {total:.2f} kg CO2\n{advice}"
            result_label.config(text=result_text, foreground=color)
            sgm = dice.randrange(20,80,5)
            cmp = sgm/100
            goal = f"Your goal: Use only {total*cmp} kg CO2"
            goal_label.config(text=goal)

            
            # Save to history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            history_entry = {
                "timestamp": timestamp,
                "values": (electricity, fuel, transport),
                "result": total
            }
            calculation_history.append(history_entry)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all fields")
    
    
    
    def reset():
         elec_entry.delete(0, tk.END)
         fuel_entry.delete(0, tk.END)
         transport_entry.delete(0, tk.END)
         result_label.config(text="Enter your values and click Calculate", 
                               foreground=DARK_GREEN)
         elec_entry.focus()
    
    def exit_app():
        if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
         root.destroy()

    
    # Main content
    main_frame = ttk.Frame( root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    # Input fields
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=10)
        
        # Electricity
    elec_frame = ttk.Frame(input_frame)
    elec_frame.pack(fill=tk.X, pady=5)
    ttk.Label(elec_frame, text="Electricity Usage (kWh):").pack(side=tk.LEFT)
    elec_entry = ttk.Entry(elec_frame, justify="center", width=15)
    elec_entry.pack(side=tk.RIGHT, padx=10)
        
        # Fuel
    fuel_frame = ttk.Frame(input_frame)
    fuel_frame.pack(fill=tk.X, pady=5)
    ttk.Label(fuel_frame, text="Fuel Consumption (L):").pack(side=tk.LEFT)
    fuel_entry = ttk.Entry(fuel_frame, justify="center", width=15)
    fuel_entry.pack(side=tk.RIGHT, padx=10)
        
        # Transport
    transport_frame = ttk.Frame(input_frame)
    transport_frame.pack(fill=tk.X, pady=5)
    ttk.Label(transport_frame, text="Transport Distance (km):").pack(side=tk.LEFT)
    transport_entry = ttk.Entry(transport_frame, justify="center", width=15)
    transport_entry.pack(side=tk.RIGHT, padx=10)
        
        # Button frame
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=20)
        
    ttk.Button(button_frame, 
                  text="Calculate", 
                  style="Gold.TButton",
                  command= calculate).pack(side=tk.LEFT, expand=True, padx=5)
        
    ttk.Button(button_frame, 
                  text="Reset", 
                  style="Green.TButton",
                  command= reset).pack(side=tk.LEFT, expand=True, padx=5)
        
    ttk.Button(button_frame, 
                  text="Exit", 
                  style="Green.TButton",
                  command= exit_app).pack(side=tk.LEFT, expand=True, padx=5)
        
        # Current result frame
    result_frame = ttk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=2)
    result_frame.pack(fill=tk.X, pady=(20, 10), ipady=10)
        
    result_label = ttk.Label(result_frame, 
                                    text="Enter your values and click Calculate",
                                    font=('Helvetica', 12),
                                    foreground=DARK_GREEN,
                                    anchor=tk.CENTER)
    result_label.pack(fill=tk.BOTH)
        
        # History section
    history_frame = ttk.Frame(main_frame, style='History.TFrame')
    history_frame.pack(fill=tk.BOTH, expand=False, pady=(10, 0))
        
    goal_label = ttk.Label(history_frame, 
                                    text="Your goal: [Based on your footprint]",
                                    font=('Helvetica', 12),
                                    foreground=DARK_GREEN,
                                    anchor=tk.CENTER)
    goal_label.pack(fill=tk.BOTH)
        
        # Set focus
    elec_entry.focus()
  
    
    # Navigation buttons
    nav_frame = tk.Frame(root, bg=DARK_GREEN, height=60)
    nav_frame.pack(fill="x", side="bottom")
    
    for tab in ["Home", "Interests", "Ask Sustainia", "Community"]:
        btn = tk.Label(nav_frame, 
                      text=tab, 
                      font=FONT_MAIN, 
                      bg=DARK_GREEN, 
                      fg=WHITE,
                      padx=20,
                      cursor="hand2")
        btn.pack(side="left")
        btn.bind("<Button-1>", lambda e, t=tab: show_tab(t))

# User interests display
    interest_frame = tk.Frame(root, bg=WHITE, padx=10, pady=10)
    interest_frame.pack(fill="x", padx=20, pady=10)
    
    tk.Label(interest_frame, 
            text="Your Interests:", 
            font=FONT_BOLD, 
            bg=WHITE).pack(anchor="w")
    
    if selected_interests:
        interests_text = ", ".join(selected_interests)
        tk.Label(interest_frame, 
                text=interests_text, 
                font=FONT_MAIN, 
                bg=WHITE).pack(anchor="w")
    else:
        tk.Label(interest_frame, 
                text="No interests selected", 
                font=FONT_MAIN, 
                bg=WHITE, 
                fg="#666").pack(anchor="w")


def sustaina():
    clear_window()
    
   
    # Header
    header = tk.Frame(root, bg=DARK_GREEN, height=80)
    header.pack(fill="x")
    tk.Label(header, text="♻️ Sustainly", 
                     font=("Helvetica", 20, "bold"), 
                     fg=WHITE, 
                     bg=DARK_GREEN,
                     padx=10,
                     pady=10).pack(pady=20)
    
    # Main content
    if selected_interests:
        chat_session.send_message(f"You are an AI named sustainia, your purpose is to give sustainable reccomendations to the user. The user is intrested in {selected_interests}. Do not exceed 200 words.")
    else:
        chat_session.send_message(f"You are an AI named sustainia, your purpose is to give sustainable reccomendations to the user. Do not exceed 200 words")
    
    response = chat_session.send_message(f"Greet the user, introduce yourself, and give them the reccomendations, their carbon footprint is {footprint}")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Scrollable Response Frame
    response_frame = ttk.Frame(main_frame)
    response_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Create Canvas and Scrollbar
    canvas = tk.Canvas(response_frame, bg=ACCENT_GOLD, highlightthickness=0)
    scrollbar = ttk.Scrollbar(response_frame, orient="vertical", command=canvas.yview)
    
    # Scrollable Frame inside Canvas
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Response Label inside scrollable frame
    response_label = tk.Label(
        scrollable_frame,
        text=response.text,
        font=FONT_MAIN,
        bg=ACCENT_GOLD,
        fg=DARK_GREEN,
        wraplength=450,
        justify="left",
        padx=10,
        pady=10
    )
    response_label.pack(fill="both", expand=True)
    
    # Input Frame (unchanged from your code)
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=5)
    
    user_frame = ttk.Frame(input_frame)
    user_frame.pack(fill=tk.X, pady=5)
    ttk.Label(user_frame, text="User Chat:").pack(side=tk.TOP)
    user_entry = ttk.Entry(user_frame, justify="center", width=100)
    user_entry.pack(side=tk.BOTTOM, padx=10)

    def respond():
        resp = user_entry.get()
        reply = chat_session.send_message(resp)  # Your chat function
        response_label.config(text=reply.text)
        # Auto-scroll to bottom after update
        canvas.yview_moveto(1.0)
        voice("notify.mp3")
    
    user_button = ttk.Button(
        user_frame, 
        text="Send", 
        command=respond,
        style='TButton'
    )
    user_button.pack(fill="x", pady=8, ipady=8, side=tk.RIGHT)

    # Navigation buttons
    nav_frame = tk.Frame(root, bg=DARK_GREEN, height=60)
    nav_frame.pack(fill="x", side="bottom")
    
    for tab in ["Home", "Interests", "Ask Sustainia", "Community"]:
        btn = tk.Label(nav_frame, 
                      text=tab, 
                      font=FONT_MAIN, 
                      bg=DARK_GREEN, 
                      fg=WHITE,
                      padx=20,
                      cursor="hand2")
        btn.pack(side="left")
        btn.bind("<Button-1>", lambda e, t=tab: show_tab(t))


def hub():
    clear_window()
    
   
    # Header
    header = tk.Frame(root, bg=DARK_GREEN, height=80)
    header.pack(fill="x")
    tk.Label(header, text="♻️ Sustainly", 
                     font=("Helvetica", 20, "bold"), 
                     fg=WHITE, 
                     bg=DARK_GREEN,
                     padx=10,
                     pady=10).pack(pady=20)
    
    def shop():
        if selected_interests:
            product = dice.choice(selected_interests)
            internet.open(f"https://www.amazon.ae/s?k=sustainable+{product}&crid=DUHH0CEQOPJY&sprefix=sustainable+products%2Caps%2C175&ref=nb_sb_noss_1")

        else:
            internet.open("https://www.amazon.ae/s?k=sustainable+products&crid=DUHH0CEQOPJY&sprefix=sustainable+products%2Caps%2C175&ref=nb_sb_noss_1")
  
    def news():
        sources = ["apnews.com","edition.cnn.com","www.bbc.com", "www.nbcnews.com", "www.aljazeera.com"]
        source = dice.choice(sources)
        internet.open(f"https://{source}/search?q=sustainable")

    def events():
        webs = ["geventm.com", "www.dmgevents.com"]
        web = dice.choice(webs)
        internet.open(f"https://{web}/search?q=sustainable")

    features = [
        ("Community Events", "🌐",events),
        ("News", "📡",news),
        ("Shop", "🎁", shop)
    ]

    content_frame = tk.Frame(root, bg=LIGHT_GREEN)
    content_frame.pack(padx=20, pady=10, fill="both", expand=True)


    for text, icon, command in features:
        btn = ttk.Button(content_frame, 
                    text=f"{icon}  {text}", 
                    command=command,
                    style='Green.TButton')
        btn.pack(fill="x", pady=8, ipady=8)


# User interests display
    interest_frame = tk.Frame(root, bg=WHITE, padx=10, pady=10)
    interest_frame.pack(fill="x", padx=20, pady=10)
    
    tk.Label(interest_frame, 
            text="Your Interests:", 
            font=FONT_BOLD, 
            bg=WHITE).pack(anchor="w")
    
    if selected_interests:
        interests_text = ", ".join(selected_interests)
        tk.Label(interest_frame, 
                text=interests_text, 
                font=FONT_MAIN, 
                bg=WHITE).pack(anchor="w")
    else:
        tk.Label(interest_frame, 
                text="No interests selected", 
                font=FONT_MAIN, 
                bg=WHITE, 
                fg="#666").pack(anchor="w")


# Navigation buttons
    nav_frame = tk.Frame(root, bg=DARK_GREEN, height=60)
    nav_frame.pack(fill="x", side="bottom")
        
    for tab in ["Home", "Interests", "Ask Sustainia", "Community"]:
        btn = tk.Label(nav_frame, 
                      text=tab, 
                      font=FONT_MAIN, 
                      bg=DARK_GREEN, 
                      fg=WHITE,
                      padx=20,
                      cursor="hand2")
        btn.pack(side="left")
        btn.bind("<Button-1>", lambda e, t=tab: show_tab(t))
# ======================
#  HELPER FUNCTIONS
# ======================
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def back_button():
    btn = ttk.Button(root, text="← Back", command=show_home_screen, style="White.TButton")
    btn.pack(anchor="nw", padx=10, pady=10)


def show_tab(tab_name):
    if tab_name == "Home":
        show_home_screen()

    elif tab_name == "Interests":
        show_interest_selection()

    elif tab_name == "Ask Sustainia":
        sustaina()

    elif tab_name == "Community":
        hub()
# ======================
#  MAIN APP SETUP
# ======================
root = tk.Tk()
root.title("Sustainly App")
root.geometry("500x700")
root.resizable(True, True)
root.configure(bg=LIGHT_GREEN)

# Custom styling
style = ttk.Style()
style.theme_use('clam')

style.configure("Gold.TButton", 
               background=ACCENT_GOLD, 
               foreground=BLACK,
               font=FONT_BOLD,
               padding=10)

style.map("Gold.TButton",
         background=[('active', DARK_GREEN), ('pressed', DARK_GREEN)],
         foreground=[('active', WHITE), ('pressed', WHITE)])

style.configure("White.TButton",
               background=WHITE,
               foreground=DARK_GREEN,
               font=FONT_MAIN)

style.configure("Green.TCheckbutton",
               background=LIGHT_GREEN,
               font=FONT_MAIN)

# Start with welcome screen
show_welcome_screen()

root.mainloop()
