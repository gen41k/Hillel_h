from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from meregesort import merge_sort

#Окно
root = Tk()
root.title('Визуализации сортировок')
root.maxsize(900, 600)
root.config(bg='black')
UI_frame = Frame(root, width= 600, height=200, bg='purple')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=650, height=380, bg='gold')
canvas.grid(row=1, column=0, padx=10, pady=5)


selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])



#Кнопки
Label(UI_frame, text="Algorithm: ", bg='pink').grid(row=0, column=0, padx=5, pady=5, sticky=W)

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0, to=3.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Скость [s]",bg='pink')
speedScale.grid(row=0, column=2, padx=5, pady=5, sticky=W)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)
sizeEntry = Scale(UI_frame, from_=3, to=100, resolution=1, orient=HORIZONTAL, label="N Элементов", bg='pink')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Мин. Элемент", bg='pink')
minEntry.grid(row=1, column=1, padx=5, pady=5)
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Макс. Элемент", bg='pink')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='pink').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()