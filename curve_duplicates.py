from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


def remove_dups():
    col_v = int(E1.get())
    duplicate_curve = col_v - 1
    curve_file = filedialog.askopenfilename(title="Select curve file", filetypes=(
        ("text files", "*.txt"), ("LAS files", "*.las"), ("all files", "*.*")))
    # open and read curve file lines to list

    with open(curve_file, 'r') as curves:
        # use a set to take first values for each based on the duplicate column
        seen = set()
        uniq = []
        for depth in curves:
            line = depth.strip().split()
            if len(line) > 0 and not line[0][0].isdigit():
                uniq.append(depth)
            elif len(line) > 0 and line[0][0].isdigit():
                depth_filter = float(line[duplicate_curve])
                if depth_filter not in seen:
                    uniq.append(depth)
                    seen.add(depth_filter)
                else:
                    pass
            else:
                pass

    os.remove(curve_file)
    with open(curve_file, 'a') as curves:
        for line in uniq:
            curves.write(line)
    messagebox.showinfo("Status", "Curve Successfully Processed")


root = Tk()
root.geometry('350x200')
root.title('Remove Duplicate Depths')
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

frame1 = Frame(frame)
frame1.pack(fill=X)

L1 = Label(frame1, text="Enter curve number with duplicate values")
L1.pack(side=TOP)
E1 = Entry(frame1)
E1.pack(side=BOTTOM)

frame2 = Frame(frame)
frame2.pack(fill=X)

b = Button(frame2, text="Select File", command = remove_dups)
b.pack()

root.mainloop()