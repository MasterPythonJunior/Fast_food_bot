import sqlite3

database = sqlite3.connect('deliverygo.db')
cursor = database.cursor()

def create_users_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT,
        location TEXT
    )
    ''')
    # INT - INTEGER -2147483648 до 2147483647
    # BIGINT -9223372036854775808 до 9223372036854775808
    # TINYINT -128 до 127


def create_cart_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) UNIQUE,
        total_products INTEGER DEFAULT 0,
        total_price DECIMAL(12, 2) DEFAULT 0
    )
    ''')

def create_cart_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_products(
        cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER REFERENCES carts(cart_id),
        product_name TEXT,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL,
        
        UNIQUE(cart_id, product_name)
    )
    ''')

def create_categories_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(30) NOT NULL UNIQUE
    )
    ''')


def insert_categories():
    cursor.execute('''
    INSERT OR IGNORE INTO categories(category_name) VALUES
    ('Лаваши'),
    ('Бургеры'),
    ('Хот-доги'),
    ('Салаты'),
    ('Сеты'),
    ('Пицца'),
    ('Напитки'),
    ('Снеки')
    ''')


def create_products_table():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            product_name VARCHAR(30) NOT NULL UNIQUE,
            price DECIMAL(12, 2) NOT NULL,
            description VARCHAR(150),
            image TEXT,
            
            FOREIGN KEY(category_id) REFERENCES categories(category_id)
        );
        '''
    )

def insert_products():
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image)
    VALUES (1, 'Мини лаваш', 20000, 'Мясо, тесто, помидоры', 'media/lavash/lavash_1.jpg'),(1, 'Лаваш говяжий', 23000, 'Мясо, тесто, помидоры', 'media/lavash/lavash_2.jpg'),(1, 'Лаваш BIG', 25000, 'Мясо, тесто, помидоры', 'media/lavash/lavash_3.jpg'),
    (2,'Чизбургер', 22000,'Мясо,тесто,помидоры','media/burger/burger_2.jpg'),
    (2,'Дабл Гамбургер', 25000,'Мясо,тесто,помидоры','media/burger/burger_3.jpg'),    (2,'Гамбургер', 20000,'Мясо,тесто,помидоры','media/burger/burger_1.jpg'),
    (3,'Хот-Дог с сыром', 18000,'сосиски,тесто,помидоры','media/hot-dog/hot-dog_1.jpg'),

    (3,'Хот-Дог по деревенски', 20000,'сосиски,тесто,помидоры','media/hot-dog/hot-dog_2.jpg'),
    (4,'Цезарь', 25000,'индейка,тесто,помидоры','media/salati/cezr.jpg'),
    (4,'Грузинский', 23000,'салат,тесто,помидоры','media/salati/gruz.jpg'),
    (4,'Греческий', 28000,'оливки,тесто,помидоры','media/salati/grech.jpg'),
    (5,'Сет Бург', 38000,'Pepsi 0,5L,картошка фри,гамбургер ','media/seti/burger_cola.jpg'),
    (5,'Сет лаш', 70000,'Pepsi 0,5L,салат цезарь,пицца пепирони ','media/seti/burger_cola.jpg'),
    (6,'Пепирони', 50000,'пепироони,тесто,сыр','media/pizza/pizza_2.jpg'),
    (6,'Говядина' , 60000,'пепироони,говядина,тесто,сыр','media/pizza/pizza_1.jpg'),
    (6,'Маргарита', 50000,'оливки,тесто,сыр','media/pizza/pizza_3.jpg'),
    (7,'Coca-Cola', 10000,'1L','media/water/water_1.jpg'),
    (7,'Fanta', 10000,'1L','media/water/water_2.jpg'),
    (7,'Sprite', 10000,'1L','media/water/water_3.jpg'),
    (8,'Картошка Фри S', 10000,'1L','media/fri/fri_1.jpg'),
    (8,'Картошка Фри L', 10000,'1L','media/fri/fri_2.jpg')''')


def create_orders_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT,
            cart_id INTEGER REFERENCES carts(cart_id),
            text TEXT,
            price TEXT,
            status TEXT NOT NULL DEFAULT 'nready'
        )
    ''')

#
# create_users_table()
# create_cart_table()
# create_cart_products_table()
# create_categories_table()
# insert_categories()
# create_products_table()
# insert_products()
# create_orders_table()

database.commit()
database.close()

















