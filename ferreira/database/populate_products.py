import sqlite3

DATABASE = 'database/app.db'

def populate_products():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Optional: Clean old products
    c.execute('DELETE FROM products')

    sample_products = [
        # Produtos para consumidores
        ("Pacote de Bolachas Maria", 30, "2025-12-31", 1.49, "bolacha.jpg", "Armazém A", "Continente Marcas", "consumer"),
        ("Garrafa de Leite Meio-Gordo", 50, "2025-06-15", 0.99, "leite.jpg", "Armazém B", "Agros", "consumer"),
        ("Shampoo Anticaspa", 20, "2026-01-20", 3.49, "detergente.jpg", "Armazém C", "Continente Saúde", "consumer"),  # Using detergent.jpg as placeholder
        ("Iogurte Natural Pack 4", 40, "2025-05-10", 2.19, "iogurte.jpg", "Armazém A", "Danone", "consumer"),
        ("Pacote de Massa Esparguete", 35, "2026-08-30", 1.29, "arroz.jpg", "Armazém D", "Milaneza", "consumer"), # Using arroz.jpg as placeholder for now
        ("Saco de Maçãs Golden", 25, "2025-05-20", 2.99, "macas.jpg", "Armazém E", "Frutas Continente", "consumer"),

        # Produtos para organizações
        ("Saco de Batatas 20kg", 10, "2025-10-15", 14.90, "sacobatatas.jpg", "Armazém Central", "Agrícola Nacional", "organization"),
        ("Caixa de Águas 24x0.5L", 8, "2025-07-01", 5.99, "agua.jpg", "Armazém Central", "Águas Luso", "organization"),
        ("Palete de Arroz Agulha 1kg", 5, "2026-01-01", 249.99, "arroz.jpg", "Armazém Industrial", "Orivárzea", "organization"),
        ("Caixa de Detergente Industrial", 12, "2027-03-12", 39.99, "detergente.jpg", "Armazém Industrial", "Continente Limpeza", "organization"),
        ("Palete de Papel Higiénico", 6, "2027-06-01", 199.99, "papel.jpg", "Armazém Logístico", "Renova", "organization"),
        ("Saco de Cebolas 25kg", 7, "2025-09-15", 17.90, "cebolas.jpg", "Armazém Central", "Hortícolas do Oeste", "organization"),
    ]
    c.executemany('''
        INSERT INTO products (name, quantity, expiration_date, price, image, location, supplier, target_user_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_products)

    conn.commit()
    conn.close()
    print("Produtos populados com sucesso!")

if __name__ == "__main__":
    populate_products()
