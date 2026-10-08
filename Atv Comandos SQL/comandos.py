import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

print(
    "Países com população entre 50 e 100 milhões OU com área maior que 5.000.000 km²:"
)

cursor.execute(
    """
    SELECT nome, populacao, area 
    FROM country 
    WHERE (populacao BETWEEN 50000000 AND 100000000) 
       OR (area > 5000000)
    ORDER BY populacao DESC
"""
)

for linha in cursor.fetchall():
    print(
        f"País: {linha[0]} | População: {linha[1]:,}".replace(",", ".")
        + f" | Área: {linha[2]:,}".replace(",", ".")
        + " km²"
    )

conexao.close()