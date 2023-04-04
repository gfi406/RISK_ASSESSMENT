import tkinter as tk

class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.num_rows = 3
        self.num_cols = 3
        self.matrix = [[None for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.create_widgets()
        
    def create_widgets(self):
        self.matrix_frame = tk.Frame(self.master)
        self.matrix_frame.pack(anchor="nw")
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.matrix[i][j] = tk.Entry(self.matrix_frame, width=5)
                self.matrix[i][j].grid(row=i, column=j)
        
        self.row_spinbox_label = tk.Label(self.master, text="Rows:")
        self.row_spinbox = tk.Spinbox(self.master, from_=1, to=6, command=self.update_matrix_size)
        self.col_spinbox_label = tk.Label(self.master, text="Cols:")
        self.col_spinbox = tk.Spinbox(self.master, from_=1, to=6, command=self.update_matrix_size)
        
        self.row_spinbox_label.pack(side=tk.TOP,anchor="nw")
        self.row_spinbox.pack(side=tk.TOP,anchor="nw")
        self.col_spinbox_label.pack(side=tk.TOP,anchor="nw")
        self.col_spinbox.pack(side=tk.TOP,anchor="nw")
        
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_matrix)
        self.reset_button.pack(side=tk.BOTTOM,anchor="nw")
        
    def update_matrix_size(self):
        new_rows = int(self.row_spinbox.get())
        new_cols = int(self.col_spinbox.get())
        
        
        if new_rows > 6 or new_cols > 6:
            return
        
        # добавляем или удаляем строки
        while self.num_rows < new_rows:
            row = [None for j in range(self.num_cols)]
            for j in range(self.num_cols):
                row[j] = tk.Entry(self.matrix_frame, width=5)
                row[j].grid(row=self.num_rows, column=j)
            self.matrix.append(row)
            self.num_rows += 1
        while self.num_rows > new_rows:
            row = self.matrix.pop()
            for entry in row:
                entry.destroy()
            self.num_rows -= 1
        
        # добавляем или удаляем столбцы
        while self.num_cols < new_cols:
            for i in range(self.num_rows):
                entry = tk.Entry(self.matrix_frame, width=5)
                entry.grid(row=i, column=self.num_cols)
                self.matrix[i].append(entry)
            self.num_cols += 1
        while self.num_cols > new_cols:
            for i in range(self.num_rows):
                entry = self.matrix[i].pop()
                entry.destroy()
            self.num_cols -= 1
        
    def reset_matrix(self):
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.matrix[i][j].delete(0, tk.END)
                self.matrix[i][j].insert(0, "")
    def get_matrix_data(self):
        data = []
        for i in range(self.num_rows):
            row_data = []
            for j in range(self.num_cols):
                value = self.matrix[i][j].get()
                if value:
                    try:
                        value = float(value)
                        row_data.append(value)
                    except ValueError:
                        pass 
            data.append(row_data)
        print(data)
class App_data:
    
  
    def _launch_win() :
         
        import tkinter as tk

        root = tk.Tk()

        photo = tk.PhotoImage(file='data/icon.png')

        root.config(bg='white')

        root.iconphoto(False,photo)

        root.title("RISK_ASSESSMENT")
        root.geometry('600x400+200+100')
        app = MatrixApp(root)

        
        root.mainloop()
    


