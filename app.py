import tkinter as tk
from tkinter import messagebox
from database import create_table, insert_product, fetch_products, update_product, delete_product

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciamento de Produtos')

        # Variáveis
        self.name_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.quantity_var = tk.IntVar()
        self.price_var = tk.DoubleVar()

        # Criar Widgets
        self.create_widgets()
        # Criar Tabela
        create_table()
        # Atualizar Lista de Produtos
        self.refresh_product_list()

    def create_widgets(self):
        # Labels e Entradas
        tk.Label(self.root, text='Nome').grid(row=0, column=0, padx=10, pady=5, sticky='e')
        tk.Label(self.root, text='Descrição').grid(row=1, column=0, padx=10, pady=5, sticky='e')
        tk.Label(self.root, text='Quantidade').grid(row=2, column=0, padx=10, pady=5, sticky='e')
        tk.Label(self.root, text='Preço').grid(row=3, column=0, padx=10, pady=5, sticky='e')

        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.description_var).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.quantity_var).grid(row=2, column=1, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.price_var).grid(row=3, column=1, padx=10, pady=5)

        # Botões
        tk.Button(self.root, text='Adicionar', command=self.add_product).grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text='Atualizar', command=self.update_product).grid(row=4, column=2, padx=10, pady=5)
        tk.Button(self.root, text='Excluir', command=self.delete_product).grid(row=4, column=3, padx=10, pady=5)

        # Lista de Produtos
        self.product_list = tk.Listbox(self.root, width=80, height=10)
        self.product_list.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

        # Evento de Seleção
        self.product_list.bind('<<ListboxSelect>>', self.on_product_select)

    def add_product(self):
        name = self.name_var.get()
        description = self.description_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()
        insert_product(name, description, quantity, price)
        self.refresh_product_list()
        self.clear_entries()

    def update_product(self):
        selected_product = self.product_list.curselection()
        if selected_product:
            product_id = self.product_list.get(selected_product[0]).split()[0]
            name = self.name_var.get()
            description = self.description_var.get()
            quantity = self.quantity_var.get()
            price = self.price_var.get()
            update_product(product_id, name, description, quantity, price)
            self.refresh_product_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Seleção", "Selecione um produto para atualizar")

    def delete_product(self):
        selected_product = self.product_list.curselection()
        if selected_product:
            product_id = self.product_list.get(selected_product[0]).split()[0]
            delete_product(product_id)
            self.refresh_product_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Seleção", "Selecione um produto para excluir")

    def refresh_product_list(self):
        self.product_list.delete(0, tk.END)
        products = fetch_products()
        for product in products:
            self.product_list.insert(tk.END, f'{product[0]} - {product[1]} - {product[2]} - {product[3]} - {product[4]}')

    def on_product_select(self, event):
        selected_product = self.product_list.curselection()
        if selected_product:
            product = self.product_list.get(selected_product[0]).split(' - ')
            self.name_var.set(product[1])
            self.description_var.set(product[2])
            self.quantity_var.set(product[3])
            self.price_var.set(product[4])

    def clear_entries(self):
        self.name_var.set('')
        self.description_var.set('')
        self.quantity_var.set(0)
        self.price_var.set(0.0)

if __name__ == '__main__':
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
