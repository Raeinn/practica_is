from mysql import connector

class Model:
    """
    ************ Database methods ************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        db_conf = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                db_conf[key] = val
        return db_conf

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
        self.cursor.execute("SET time_zone='-05:00'")

    def close_db(self):
        self.cnx.close()
    
    """
    ************ Users methods ************
    """
    def create_user(self, u_id, u_pass, u_admin):
        try:
            sql = "INSERT INTO usuarios(u_id, u_password, is_admin) VALUES(%s, %s, %s);"
            values = (u_id, u_pass, u_admin)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def log_in(self, u_id, u_pass):
        try:
            sql = "SELECT u_id, is_admin FROM usuarios WHERE u_id = %s AND u_password = %s;"
            values = (u_id, u_pass)
            self.cursor.execute(sql, values)
            user = self.cursor.fetchone()
            return user
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_user(self, u_id):
        try:
            sql = "SELECT u_id, is_admin FROM usuarios WHERE u_id = %s;"
            values = (u_id,)
            self.cursor.execute(sql, values)
            user = self.cursor.fetchone()
            return user
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_all_users(self):
        try:
            sql = "SELECT u_id, is_admin FROM usuarios;"
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_user(self, u_id, u_pass, u_admin):
        fields = []
        values = []
        if u_pass != '':
            values.append(u_pass)
            fields.append('u_password = %s')
        if u_admin != '':
            values.append(u_admin)
            fields.append('is_admin = %s')
        values.append(u_id)
        values = tuple(values)
        try:
            sql = "UPDATE usuarios SET "+",".join(fields)+" WHERE u_id = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_user(self, u_id):
        try:
            sql = "DELETE FROM usuarios WHERE u_id = %s;"
            values = (u_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    """
    ************ Movies methods ************
    """
    def create_movie(self, p_name, p_genre, p_class):
        try:
            sql = "INSERT INTO peliculas(nombre, genero, clasificacion) VALUES(%s, %s, %s);"
            values = (p_name, p_genre, p_class)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_movie(self, p_id):
        try:
            sql = "SELECT * FROM peliculas WHERE p_id = %s;"
            values = (p_id,)
            self.cursor.execute(sql, values)
            mv = self.cursor.fetchone()
            return mv
        except connector.Error as err:
            print(err)
            return (err)

    def read_movie_name(self, p_name):
        try:
            sql = "SELECT * FROM peliculas WHERE nombre LIKE '%"+p_name+"%';"
            self.cursor.execute(sql)
            mvs = self.cursor.fetchall()
            return mvs
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_all_movies(self):
        try:
            sql = "SELECT * FROM peliculas;"
            self.cursor.execute(sql)
            mvs = self.cursor.fetchall()
            return mvs
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_movie(self, p_id, p_name, p_genre, p_class):
        fields = []
        values = []
        if p_name != '':
            values.append(p_name)
            fields.append('nombre = %s')
        if p_genre != '':
            values.append(p_genre)
            fields.append('genero = %s')
        if p_class != '':
            values.append(p_class)
            fields.append('clasificacion = %s')
        values.append(p_id)
        values = tuple(values)
        try:
            sql = "UPDATE peliculas SET "+",".join(fields)+" WHERE p_id = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_movie(self, p_id):
        try:
            sql = "DELETE FROM peliculas WHERE p_id = %s;"
            values = (p_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    """
    ************ Halls methods ************
    """
    def create_hall(self, s_id, s_desc):
        try:
            sql = "INSERT INTO salas(s_id, descripcion) VALUES(%s, %s);"
            values = (s_id, s_desc)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_hall(self, s_id):
        try:
            sql = "SELECT * FROM salas WHERE s_id = %s;"
            values = (s_id,)
            self.cursor.execute(sql, values)
            sala = self.cursor.fetchone()
            return sala
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_all_halls(self):
        try:
            sql = "SELECT * FROM salas;"
            self.cursor.execute(sql)
            salas = self.cursor.fetchall()
            return salas
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_hall(self, s_id, s_desc):
        if s_desc == '':
            return False
        values = (s_desc, s_id)
        try:
            sql = "UPDATE salas SET descripcion = %s WHERE s_id = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_hall(self, s_id):
        try:
            sql = "DELETE FROM salas WHERE s_id = %s;"
            values = (s_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    """
    ************ Seats methods ************
    """
    def create_seat(self, a_id, s_id):
        try:
            sql = "INSERT INTO asientos(a_id, sala) VALUES(%s, %s);"
            values = (a_id, s_id)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_seat(self, a_id):
        try:
            sql = "SELECT * FROM asientos WHERE a_id = %s;"
            values = (a_id,)
            self.cursor.execute(sql, values)
            sala = self.cursor.fetchone()
            return sala
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_seats_hall(self, s_id):
        try:
            sql = "SELECT * FROM asientos WHERE sala = %s;"
            values = (s_id,)
            self.cursor.execute(sql, values)
            sala = self.cursor.fetchall()
            return sala
        except connector.Error as err:
            print(err)
            return (err)
    
    def delete_seat(self, a_id):
        try:
            sql = "DELETE FROM asientos WHERE a_id = %s;"
            values = (a_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    """
    ************ Schedules methods ************
    """
    def create_func(self, p_id, s_id, emision):
        try:
            sql = "INSERT INTO funciones(pelicula, sala, fecha_emision) VALUES(%s, %s, %s);"
            values = (p_id, s_id, emision)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_func(self, f_id):
        try:
            sql = "SELECT * FROM funciones WHERE f_id = %s;"
            values = (f_id,)
            self.cursor.execute(sql, values)
            func = self.cursor.fetchone()
            return func
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_func_date(self, emision):
        try:
            sql = "SELECT * FROM funciones WHERE fecha_emision LIKE '"+emision+"%';"
            self.cursor.execute(sql)
            func = self.cursor.fetchall()
            return func
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_func_movie(self, p_id):
        try:
            sql = "SELECT * FROM funciones WHERE pelicula = %s;"
            values = (p_id,)
            self.cursor.execute(sql, values)
            func = self.cursor.fetchall()
            return func
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_all_funcs(self):
        try:
            sql = "SELECT * FROM funciones;"
            self.cursor.execute(sql)
            funcs = self.cursor.fetchall()
            return funcs
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_func(self, f_id, p_id, s_id, emision):
        fields = []
        values = []
        if p_id != '':
            values.append(p_id)
            fields.append('pelicula = %s')
        if s_id != '':
            values.append(s_id)
            fields.append('sala = %s')
        if emision != '':
            values.append(emision)
            fields.append('fecha_emision = %s')
        values.append(f_id)
        values = tuple(values)
        try:
            sql = "UPDATE funciones SET "+','.join(fields)+" WHERE f_id = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_func(self, f_id):
        try:
            sql = "DELETE FROM funciones WHERE f_id = %s;"
            values = (f_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    """
    ************ Tickets methods ************
    """
    def create_tic(self, f_id, a_id):
        try:
            sql = "INSERT INTO boletos(funcion, asiento) VALUES(%s, %s);"
            values = (f_id, a_id)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_tic(self, b_id):
        try:
            sql = "SELECT b.b_id, b.funcion, b.asiento, bu.usuario FROM boletos b, boletos_usuarios bu WHERE b.b_id = bu.boleto AND b.b_id = %s;"
            values = (b_id,)
            self.cursor.execute(sql, values)
            tic = self.cursor.fetchone()
            return tic
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_tic_fun(self, f_id):
        try:
            sql = "SELECT b.b_id, b.funcion, b.asiento, bu.usuario FROM (boletos b JOIN boletos_usuarios bu ON b.b_id = bu.boleto) WHERE b.funcion = %s;"
            values = (f_id,)
            self.cursor.execute(sql, values)
            tic = self.cursor.fetchall()
            return tic
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_detailed_tic(self, f_id, a_id):
        try:
            sql = "SELECT * FROM boletos WHERE funcion = %s AND asiento = %s;"
            values = (f_id, a_id)
            self.cursor.execute(sql, values)
            tic = self.cursor.fetchone()
            return tic
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_tic(self, b_id, f_id, a_id):
        fields = []
        values = []
        if f_id != '':
            values.append(f_id)
            fields.append('funcion = %s')
        if a_id != '':
            values.append(a_id)
            fields.append('asiento = %s')
        values.append(b_id)
        try:
            sql = "UPDATE boletos SET "+','.join(fields)+" WHERE b_id = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_tic(self, b_id):
        try:
            sql = "DELETE FROM boletos WHERE b_id = %s;"
            values = (b_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    """
    ************ Purchases (users-tickets) methods ************
    """
    def create_tic_det(self, b_id, u_id):
        try:
            sql = "INSERT INTO boletos_usuarios(boleto, usuario) VALUES(%s, %s);"
            values = (b_id, u_id)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def read_tic_user(self, u_id):
        try:
            sql = "SELECT b.b_id, b.funcion, b.asiento, bu.usuario FROM (boletos_usuarios bu JOIN boletos b ON bu.boleto = b.b_id) WHERE bu.usuario = %s;"
            values = (u_id,)
            self.cursor.execute(sql, values)
            tic = self.cursor.fetchall()
            return tic
        except connector.Error as err:
            print(err)
            return (err)
    
    def update_tic_det(self, b_id, u_id):
        if u_id == '':
            return False
        values = (u_id, b_id)
        try:
            sql = "UPDATE boletos_usuarios SET usuario = %s WHERE boleto = %s;"
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)
    
    def delete_tic_det(self, b_id):
        try:
            sql = "DELETE FROM boletos_usuarios WHERE boleto = %s;"
            values = (b_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            cnt = self.cursor.rowcount
            return cnt
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)