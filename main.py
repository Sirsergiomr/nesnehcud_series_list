import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
def main():
    raiz = Tk()
    raiz.title("nesnehcud")
    raiz.configure(bg="#3a4241")
    raiz.geometry("+250+80")
    raiz.resizable(False,False)
    Listado(raiz)
    raiz.mainloop()

class Listado():
    def __init__(self, raiz):
        self.window = raiz
        panelA = LabelFrame(self.window, bg= "#3a4241")
        panelA.grid(row=0, column=0)
        Label(panelA, text = 'Nombre Serie',bg="#3a4241", fg = "#33a4f5", font = ("Comic Sans MS", "11", "normal")).grid(row = 0, column = 0)
        cuadro_nombre = Entry(panelA, font = ("Comic Sans MS", "11", "normal"), width = 35)
        cuadro_nombre.grid(row = 0, column = 1)
        cuadro_nombre.focus()

        Label(panelA, text = 'Duracion',bg="#3a4241", fg = "#33a4f5", font = ("Comic Sans MS", "11", "normal")).grid(row = 1, column = 0)
        cuadro_duracion = Entry(panelA, font = ("Comic Sans MS", "11", "normal"), width = 35)
        cuadro_duracion.grid(row = 1, column = 1)
        cuadro_duracion.focus()

        Label(panelA, text = 'Autor',bg="#3a4241", fg = "#33a4f5", font = ("Comic Sans MS", "11", "normal")).grid(row = 2, column = 0)
        cuadro_autor = Entry(panelA, font = ("Comic Sans MS", "11", "normal"), width = 35)
        cuadro_autor.grid(row = 2, column = 1)
        cuadro_autor.focus()

        buttonAñadir = Button(panelA,command=lambda:Añadir(), text='Añadir', width=20)
        buttonAñadir.configure(bg="#3a4241",fg="#f7fffe", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        buttonAñadir.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)

        buttonBorrar = Button(panelA,command=lambda:Borrar(), text='Borrar', width=20)
        buttonBorrar.configure(bg="#3a4241",fg="#f7fffe", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        buttonBorrar.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        buttonModificar = Button(panelA,command= lambda:Modificar(),text='Modificar', width=20)
        buttonModificar.configure(bg="#3a4241",fg="#f7fffe", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        buttonModificar.grid(row=2, column=2, padx=2, pady=3, sticky=W + E)

        buttonBuscar = Button(panelA,command=lambda:Buscador(), text='Buscar', width=20)
        buttonBuscar.configure(bg="#3a4241",fg="#f7fffe", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        buttonBuscar.grid(row=3, column=2, padx=2, pady=3, sticky=W + E)
        Panel_Tabla = LabelFrame(self.window, bg="#3a4241")
        Panel_Tabla.grid(row = 4, column = 0)


        self.tree = ttk.Treeview(Panel_Tabla, height=2, columns=("one", "two"))
        self.tree.grid(padx=2, pady=2, row=4, column=0, columnspan=1)
        self.tree.heading("#0", text='Serie', anchor=CENTER)
        self.tree.heading("one", text='Duracion', anchor=CENTER)
        self.tree.heading("two", text='Autor', anchor=CENTER)

        scrollVert = Scrollbar(Panel_Tabla, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=4, column=1, sticky="nsew")

        scroll_x = Scrollbar(Panel_Tabla, command=self.tree.xview, orient=HORIZONTAL)
        self.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=6, column=0, columnspan=1, sticky="nsew")

        def Abrir_csv():
            with open('nesnehcud_list.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    serie = str(row[0])
                    duracion = str(row[1])
                    autor = str(row[2])
                    self.tree.insert("", 0, text = serie, values = (duracion, autor))

        def Limpia_Cuadro_Texto():
            # Delete from first position (0) to the last position ('end')
            cuadro_nombre.delete(0, 'end')
            cuadro_duracion.delete(0, 'end')
            cuadro_autor.delete(0, 'end')
        def BorrarTabla():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)
        def guardar(serie, duracion, autor):
            s_serie = serie
            s_duracion = duracion
            s_autor = autor
            with open('nesnehcud_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_serie, s_duracion, s_autor))
        def Añadir():
            BorrarTabla()
            Abrir_csv()
            serie = cuadro_nombre.get()
            duracion = cuadro_duracion.get()
            autor = cuadro_autor.get()
            chequeaLista = [serie, duracion, autor]
            if Existir(_busqueda(serie,0)) == False:
                if chequeaLista == ['', '', '']:
                     FaltanCampos()
                else:
                    if serie == '':
                        serie = '<Default>'
                    if duracion == '':
                        duracion = '<Default>'
                    if autor == '':
                        autor = '<Default>'
                    guardar(serie, duracion, autor)

        def FaltanCampos():
            MessageBox.showinfo("Advertencia", "Faltan campos")

        def _busqueda(var_texto, posicion):
            Lista = []
            var_possition = int(posicion)
            s_var_texto = str(var_texto)
            with open('nesnehcud_list.csv', 'r') as d:
                reader = csv.reader(d)
                for i, row in enumerate(reader):
                    if s_var_texto == row[var_possition]:
                      Lista = [row[0], row[1], row[2]]
                      break
                    else:
                        continue
            return Lista
        def Existir(Lista):
            if Lista == []:
                print("No existe")
                existir = False
            else:
                existir = True
                YaExiste()
            return existir
        def YaExiste():
            MessageBox.showinfo("Mensaje", "Esa serie ya existe en la lista")

        def Buscador():
            BorrarTabla()
            var_serie = cuadro_nombre.get()

            lista = _busqueda(var_serie, 0)
            if lista == []:
                Abrir_csv()
                NoExiste()
            else:
                serie = str(lista[0])
                duracion = str(lista[1])
                autor = str(lista[2])
                self.tree.insert("", 0, text=serie, values=(duracion, autor))

        def NoExiste():
            MessageBox.showinfo("Mensaje", "Esa serie no existe en la lista")

        def Borrar():
            var_serie = cuadro_nombre.get()
            lista = _busqueda(var_serie,0)
            if lista == []:
                NoExiste()
            else:
                with open('nesnehcud_list.csv', 'r') as d:
                    reader = list(csv.reader(d))
                with open('nesnehcud_list.csv', 'w') as d:
                    writer = csv.writer(d , lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if var_serie != row[0]:
                            writer.writerow(row)
            BorrarTabla()
            Abrir_csv()
        def Modificar():
            serie = cuadro_nombre.get()
            duracion = cuadro_duracion.get()
            autor = cuadro_autor.get()
            chequeocuadros = [serie,duracion,autor]
            if chequeocuadros==[serie,'','']:
                FaltanCampos()
            elif Existir(_busqueda(serie, 0)) == True:
                        Borrar()
                        guardar(serie,duracion,autor)
            BorrarTabla()
            Buscador()

if __name__ == '__main__':
    main()