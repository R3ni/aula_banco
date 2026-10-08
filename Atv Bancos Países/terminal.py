import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# 1. Criar a tabela country
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS country (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        populacao INT NOT NULL,
        area INT NOT NULL
    )
"""
)

# 2. Criar a tabela City com chave estrangeira para country
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS City (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        country_id INTEGER NOT NULL,
        populacao INT NOT NULL,
        rating INTEGER CHECK(rating BETWEEN 0 AND 5),
        FOREIGN KEY (country_id) REFERENCES country(id)
    )
"""
)

# 3. Lista com 30 países e suas respectivas capitais (Nome, População País, Área, Capital, População Capital, Rating)
dados_mundiais = [
    ("Brasil", 215000000, 8514876, "Brasília", 3055000, 4),
    ("Estados Unidos", 331000000, 9833520, "Washington, D.C.", 689545, 4),
    ("China", 1412000000, 9596961, "Pequim", 21540000, 5),
    ("Japão", 125700000, 377975, "Tóquio", 13960000, 5),
    ("Alemanha", 83200000, 357022, "Berlim", 3850809, 4),
    ("Reino Unido", 67000000, 242495, "Londres", 8982000, 5),
    ("França", 67750000, 551695, "Paris", 2165423, 5),
    ("Canadá", 38250000, 9984670, "Ottawa", 1017449, 4),
    ("Argentina", 45800000, 2780400, "Buenos Aires", 3075646, 4),
    ("Itália", 59100000, 301340, "Roma", 2860009, 5),
    ("Austrália", 25600000, 7692024, "Camberra", 456652, 3),
    ("Índia", 1408000000, 3287263, "Nova Deli", 32941000, 3),
    ("México", 128900000, 1964375, "Cidade do México", 9209944, 4),
    ("Espanha", 47400000, 505992, "Madri", 3332035, 5),
    ("Rússia", 143400000, 17098246, "Moscou", 13010112, 4),
    ("África do Sul", 59390000, 1221037, "Pretória", 741651, 3),
    ("Coreia do Sul", 51780000, 100210, "Seul", 9776000, 5),
    ("Colômbia", 51520000, 1141748, "Bogotá", 7181469, 3),
    ("Chile", 19490000, 756102, "Santiago", 6257516, 4),
    ("Portugal", 10330000, 92212, "Lisboa", 545923, 5),
    ("Peru", 33350000, 1285216, "Lima", 9674755, 3),
    ("Egito", 104250000, 1010408, "Cairo", 10230350, 3),
    ("Turquia", 84680000, 783356, "Ancara", 5663322, 3),
    ("Grécia", 10640000, 131957, "Atenas", 664046, 4),
    ("Suécia", 10420000, 450295, "Estocolmo", 978770, 4),
    ("Noruega", 5400000, 323802, "Oslo", 697549, 4),
    ("Países Baixos", 17530000, 41543, "Amsterdã", 921468, 5),
    ("Suíça", 8700000, 41285, "Berna", 133115, 4),
    ("Nova Zelândia", 5120000, 268021, "Wellington", 212700, 4),
    ("Tailândia", 71600000, 513120, "Bangcoc", 10539000, 4),
]

# 4. Inserir dados nas tabelas
for pais, pop_pais, area, capital, pop_capital, rating in dados_mundiais:
    # Insere o país e recupera o ID gerado automaticamente
    cursor.execute(
        """
        INSERT INTO country (nome, populacao, area)
        VALUES (?, ?, ?)
    """,
        (pais, pop_pais, area),
    )

    pais_id = cursor.lastrowid

    # Insere a cidade associada ao ID do país correspondente
    cursor.execute(
        """
        INSERT INTO City (nome, country_id, populacao, rating)
        VALUES (?, ?, ?, ?)
    """,
        (capital, pais_id, pop_capital, rating),
    )

conexao.commit()
conexao.close()

print("30 países e suas capitais foram adicionados com sucesso!")