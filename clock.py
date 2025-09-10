import tkinter as tk
from time import strftime, time


root = tk.Tk()
root.title("⏱️ Simple Time Tool")
root.geometry("500x550")
root.configure(bg='#2c3e50')
root.resizable(False, False)


stopwatch_running = False
stopwatch_start = 0
stopwatch_elapsed = 0

timer_running = False
timer_end_time = 0


def update_clock():
    clock_label.config(text=strftime('%H:%M:%S %p'))
    clock_label.after(1000, update_clock)


def update_stopwatch():
    if stopwatch_running:
        elapsed = time() - stopwatch_start + stopwatch_elapsed
        mins, secs = divmod(int(elapsed), 60)
        centisecs = int((elapsed - int(elapsed)) * 100)
        stopwatch_label.config(text=f"{mins:02}:{secs:02}:{centisecs:02}")
        stopwatch_label.after(50, update_stopwatch)

def start_stopwatch():
    global stopwatch_running, stopwatch_start
    if not stopwatch_running:
        stopwatch_running = True
        stopwatch_start = time() - stopwatch_elapsed
        update_stopwatch()
        sw_btn.config(text="⏸ PAUSE", bg='#f39c12')

def pause_stopwatch():
    global stopwatch_running, stopwatch_elapsed
    if stopwatch_running:
        stopwatch_running = False
        stopwatch_elapsed = time() - stopwatch_start
        sw_btn.config(text="▶ RESUME", bg='#27ae60')

def reset_stopwatch():
    global stopwatch_running, stopwatch_elapsed
    stopwatch_running = False
    stopwatch_elapsed = 0
    stopwatch_label.config(text="00:00:00")
    sw_btn.config(text="▶ START", bg='#27ae60')


def update_timer():
    global timer_running
    if timer_running:
        remaining = max(0, timer_end_time - time())
        if remaining <= 0:
            timer_running = False
            timer_label.config(text="00:00", fg='red')
            timer_status.config(text="⏰ TIME'S UP! Click RESET", fg='red')
            timer_btn.config(text="▶ START", bg='#27ae60')
            return
        mins, secs = divmod(int(remaining), 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        timer_label.after(500, update_timer)

def start_pause_timer():
    global timer_running, timer_end_time
    if timer_running:
       
        timer_running = False
        timer_btn.config(text="▶ RESUME", bg='#27ae60')
    else:
      
        try:
            mins = int(min_entry.get() or 0)
            secs = int(sec_entry.get() or 0)
            total_seconds = mins * 60 + secs
            if total_seconds <= 0:
                timer_status.config(text="Please enter minutes or seconds > 0", fg='red')
                return
            if not hasattr(start_pause_timer, 'initial_set') or not timer_running:
               
                timer_end_time = time() + total_seconds
                start_pause_timer.initial_set = True
            timer_running = True
            timer_status.config(text="⏳ Timer Running... Click button to PAUSE", fg='#27ae60')
            timer_btn.config(text="⏸ PAUSE", bg='#f39c12')
            update_timer()
        except ValueError:
            timer_status.config(text="Enter NUMBERS only (e.g., 5, 30)", fg='red')

def reset_timer():
    global timer_running
    timer_running = False
    timer_label.config(text="00:00", fg='#ecf0f1')
    timer_status.config(text="✅ Enter minutes & seconds, then click START", fg='#ecf0f1')
    timer_btn.config(text="▶ START", bg='#27ae60')
  
    min_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)
    min_entry.insert(0, "0")
    sec_entry.insert(0, "0")


tk.Label(root, text="🕒 LIVE CLOCK", font=('Helvetica', 16, 'bold'), bg='#2c3e50', fg='#ecf0f1').pack(pady=(20,5))
clock_label = tk.Label(root, font=('Courier', 24, 'bold'), bg='#34495e', fg='#27ae60', width=20)
clock_label.pack(pady=5)
update_clock()


tk.Label(root, text="⏱️ STOPWATCH", font=('Helvetica', 16, 'bold'), bg='#2c3e50', fg='#ecf0f1').pack(pady=(30,5))
stopwatch_label = tk.Label(root, text="00:00:00", font=('Courier', 24, 'bold'), bg='#34495e', fg='#ecf0f1', width=20)
stopwatch_label.pack(pady=5)

sw_frame = tk.Frame(root, bg='#2c3e50')
sw_frame.pack(pady=10)

sw_btn = tk.Button(sw_frame, text="▶ START", command=start_stopwatch, bg='#27ae60', fg='white', font=('Helvetica', 12, 'bold'), width=10)
sw_btn.pack(side='left', padx=5)
tk.Button(sw_frame, text="⏹ RESET", command=reset_stopwatch, bg='#e74c3c', fg='white', font=('Helvetica', 12, 'bold'), width=10).pack(side='left', padx=5)


tk.Label(root, text="⏰ COUNTDOWN TIMER", font=('Helvetica', 16, 'bold'), bg='#2c3e50', fg='#ecf0f1').pack(pady=(30,5))


input_frame = tk.Frame(root, bg='#2c3e50')
input_frame.pack(pady=5)

tk.Label(input_frame, text="Minutes:", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1').pack(side='left', padx=5)
min_entry = tk.Entry(input_frame, width=5, font=('Helvetica', 14), justify='center')
min_entry.pack(side='left', padx=5)
min_entry.insert(0, "0")

tk.Label(input_frame, text="Seconds:", font=('Helvetica', 12), bg='#2c3e50', fg='#ecf0f1').pack(side='left', padx=5)
sec_entry = tk.Entry(input_frame, width=5, font=('Helvetica', 14), justify='center')
sec_entry.pack(side='left', padx=5)
sec_entry.insert(0, "0")

timer_label = tk.Label(root, text="00:00", font=('Courier', 24, 'bold'), bg='#34495e', fg='#ecf0f1', width=20)
timer_label.pack(pady=10)


timer_status = tk.Label(root, text="✅ Enter minutes & seconds, then click START", font=('Helvetica', 10, 'bold'), bg='#2c3e50', fg='#ecf0f1', wraplength=400)
timer_status.pack(pady=5)


timer_btn = tk.Button(root, text="▶ START", command=start_pause_timer, bg='#27ae60', fg='white', font=('Helvetica', 12, 'bold'), width=15)
timer_btn.pack(pady=5)

tk.Button(root, text="⏹ RESET", command=reset_timer, bg='#e74c3c', fg='white', font=('Helvetica', 12, 'bold'), width=15).pack(pady=5)

tk.Label(root, text="All tools work independently. No installs needed.", font=('Helvetica', 9), bg='#2c3e50', fg='#bdc3c7').pack(side='bottom', pady=10)

root.mainloop()
