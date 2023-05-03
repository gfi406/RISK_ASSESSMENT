# -*- coding: cp1251 -*- 
 
from operator import length_hint
import tkinter as tk
from turtle import window_width
from itertools import product
import matplotlib.pyplot as plt 
import math 
import statistics




class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.num_rows = 3
        self.num_cols = 3
        self.matrix = [[None for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.create_widgets()
        
    def create_widgets(self):
        self.matrix_frame = tk.Frame(self.master,width=10,height=5)
        self.matrix_frame.pack(anchor="nw")
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.matrix[i][j] = tk.Entry(self.matrix_frame, width=5)
                self.matrix[i][j].grid(row=i, column=j)
        
        self.row_spinbox_label = tk.Label(self.master, text="Rows:")
        self.row_spinbox = tk.Spinbox(self.master, from_=3, to=6, command=self.update_matrix_size)
        self.col_spinbox_label = tk.Label(self.master, text="Cols:")
        self.col_spinbox = tk.Spinbox(self.master, from_=3, to=6, command=self.update_matrix_size)
        
        
        self.formula_input = tk.Entry()
        self.formula_input.pack(anchor="ne")

        self.row_spinbox_label.pack(side=tk.BOTTOM,anchor="nw")
        self.row_spinbox.pack(side=tk.BOTTOM,anchor="nw")
        self.col_spinbox_label.pack(side=tk.BOTTOM,anchor="nw")
        self.col_spinbox.pack(side=tk.BOTTOM,anchor="nw")
        
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_matrix)
        self.reset_button.pack(side=tk.BOTTOM,anchor="nw")

        self.get_button = tk.Button(self.master, text="Get", command=self.all_combinations   )

        self.get_button = tk.Button(self.master, text="Get", command=self.do_some_magic )

        self.get_button.pack(side=tk.BOTTOM,anchor="nw")
        
        
    def update_matrix_size(self):
        new_rows = int(self.row_spinbox.get())
        new_cols = int(self.col_spinbox.get())
        
        
        if new_rows > 6 or new_cols > 6 or new_rows <3 or new_cols < 3:
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
        
        return(data)
    

    def all_combinations(self):
        arr = self.get_matrix_data ()
        rows = len(arr)
        cols = len(arr[0])
        #print ([list(comb) for comb in product(*arr)])
        return [list(comb) for comb in product(*arr)]


    def multiplicate_matrix(self):
        arr = self.all_combinations()
        getter_arr = []
        for i in range(0,len(arr)) :
            for j in range(arr[i]) :
                g+=arr[i[j]]
            getter_arr.append(g)
        print(getter_arr)

    

        return [list(comb) for comb in product(*arr)]
    def multiplicate_matrix(self):
        matrix = self.all_combinations()
        row_products = []
        for row in matrix:
            row_product = 1
            for num in row:
                row_product *= num
            row_products.append(row_product)
       # print("*",row_products)
        return row_products
    
    
    def plus_matrix(self):
        matrix = self.all_combinations()
        row_products = []
        for row in matrix:
            row_product = 0
            for num in row:
                row_product += num
            row_products.append(row_product)
        #print("+",row_products)
        return row_products
    def formul_manager(self):
        
        arr = self.all_combinations()
        
        len_arr = len (arr[0])
        
        result =[]

        for i in range(0,len(arr)):
            formula = self.formula_input.get()
            formula = formula.replace('p1', str(arr[i][0])) 
            formula = formula.replace('p2',str(arr[i][1]))
            formula = formula.replace('p3',str(arr[i][2]))
            
            if len_arr >= 4:
                formula = formula.replace('p4',str(arr[i][3]))
            if len_arr >= 5:
                formula = formula.replace('p5',str(arr[i][4]))
            if len_arr >= 6:
                formula = formula.replace('p6',str(arr[i][5]))

            result.append(eval(formula))
        print(result)    
        return(result)
    def give_gistogram(self):
        data = self.plus_matrix()
        x = sorted(data)
        arr = self.all_combinations()
        len_arr = len(arr[0])
        min_x = min(x)
        max_x = max(x)
        h = (max_x - min_x)/(1+3.3*math.log1p(len_arr))
        ticks = []
        i = 0

        while (i+h) < max_x:
            ticks.append(float("{:.2f}".format((i+h))))
            i += h

        plt.hist(x)
        plt.xticks(ticks, ticks)
        plt.locator_params(axis='y', integer=True) 
        
        plt.title("Risk values")        
        plt.show()
        
    def do_some_magic(self):
        
        
        self.mediana() 
                    
        self.give_gistogram()
        self.formul_manager()
    def mediana(self):
        data = 0
        arr = self.all_combinations()
        flat_arr = [i for sublist in arr for i in sublist]
        data =  flat_arr
        mode = statistics.mode(data)
        median = statistics.median(data)
        more_med = less_med = more_mod = less_mod = final_med = final_mod = 0
        for elem in data:
            if elem > median:
                more_med += 1
            elif elem < median:
                less_med += 1
            if elem > mode:
                more_mod += 1
            elif elem < mode:
                less_mod += 1
            if (more_mod == 0) or (less_mod == 0):
                final_mod = 0
            elif (more_med == 0) or (less_med == 0):
                final_med = 0
            else:                                                                                          
                final_med = less_med / more_med
                final_mod = less_mod / more_mod
        print("Mode risk:", final_med)
        print("Median risk:", final_mod, end=' ')
    
class App_data:
    
  
    def _launch_win() :                                               
         
        import tkinter as tk

        root = tk.Tk()
                                                                                                    
       # photo = tk.PhotoImage(file='data/icon.png')

        #root.iconphoto(False,photo)

        root.config(bg='white')

        

        root.title("RISK_ASSESSMENT")
        root.geometry('600x350+200+100')
        app = MatrixApp(root)
        #print ("1")

        
        root.mainloop()
    


