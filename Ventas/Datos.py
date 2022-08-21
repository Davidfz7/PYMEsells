import sqlite3

class Database:

    def _init_(self, datos):
        self.conn = sqlite3.connect(datos)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cliente(id INTEGER PRIMARY KEY, producto text, cliente text, vendedor text, precio text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM cliente")
        rows = self.cur.fetchall()
        return rows

    def insert(self, producto, cliente, vendedor, precio):
        self.cur.execute("INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)", (producto, cliente, vendedor, precio))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM cliente WHere id=?", (id,))
        self.conn.commit()

    def update(self, id, producto, cliente, vendedor, precio):
        self.cur.execute("UPDATE cliente SET producto = ?, cliente = ?, vendedor = ?, precio = ? WHERE id = ?", (producto, cliente, vendedor, precio, id))
        self.conn.commit()

    def _del_(self):
        self.conn.close()


datos = Database('ventas.db')
#datos.insert("Martillo", "Luis Gomez" "EPA" , "18.900")
#datos.insert("Carretillo", "Kisha", "El Colono", "32.000")
#datos.insert("Taladro", "David Perez", "Stark Industries", "59.995")
