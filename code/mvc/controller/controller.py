from model.model import Model
from view.view import View
from string import ascii_lowercase
import getpass

class Controller:
    """
    ************ General methods ************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.user = None
        self.numberToLetter = [[index, letter] for index, letter in enumerate(ascii_lowercase, start=1)]
        self.letterToNumber = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
    
    def start(self):
        self.view.start()
        log_flag = False
        while not log_flag:
            self.user, log_flag, exit_flag = self.log_in()
            if exit_flag:
                self.view.end()
                self.model.close_db()
                return
        if bool(self.user[1]):
            self.admin_menu()
        else:
            self.general_menu()

    """
    ************ Users methods ************
    """
    def log_in(self):
        self.view.log_in()
        self.view.ask("Usuario (deje en blanco para cerrar programa): ")
        u_id = input()
        if u_id == '':
            return None, False, True
        user = self.model.read_user(u_id)
        if type(user) == tuple:
            u_pass = getpass.getpass("Contraseña: ")
            user = self.model.log_in(u_id, u_pass)
            if type(user) == tuple:
                self.view.login_ok(user[0])
                return user, True, False
            else:
                self.view.msg("Credenciales incorrectas. Reintente.")
                return None, False, False
        else:
            self.view.invalid_id()
            self.view.msg("Reintente.")
            return None, False, False
    
    def admin_menu(self):
        while True:
            self.view.admin_menu()
            self.view.select_option()
            op = input()
            if op == '1':
                self.user_menu()
            elif op == '2':
                self.movie_menu_adm()
            elif op == '3':
                self.hall_menu()
            elif op == '4':
                self.seat_menu()
            elif op == '5':
                self.fun_menu_adm()
            elif op == '6':
                self.tic_menu_adm()
            elif op == '0':
                self.model.close_db()
                self.view.end()
                return
            else:
                self.view.option_invalid()
    
    def general_menu(self):
        while True:
            self.view.general_menu()
            self.view.select_option()
            op = input()
            if op == '1':
                self.movie_menu_usr()
            elif op == '2':
                self.fun_menu_usr()
            elif op == '3':
                self.tic_menu_usr()
            elif op == '0':
                self.model.close_db()
                self.view.end()
                return
            else:
                self.view.option_invalid()
    
    def user_menu(self):
        while True:
            self.view.user_menu()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_user()
            elif op == '2':
                self.read_user()
            elif op == '3':
                self.read_all_users()
            elif op == '4':
                self.update_user()
            elif op == '5':
                self.delete_user()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def insert_user(self):
        self.view.ask("Nombre de usuario: ")
        u_id = input()
        while True:
            u_pass = getpass.getpass("Contraseña: ")
            u_conf = getpass.getpass("Confirme contraseña: ")
            if u_pass == u_conf:
                break
            else:
                self.view.msg("Las contraseñas no son idénticas. Reintente.")
        self.view.ask("¿Desea otorgar privilegios de admin? (0=No, 1=Sí): ")
        u_admin = input()
        return [u_id, u_pass, u_admin]
    
    def read_update_user(self):
        while True:
            u_pass = getpass.getpass("Contraseña: ")
            if u_pass == '':
                break
            u_conf = getpass.getpass("Confirme contraseña: ")
            if u_pass == u_conf:
                break
            else:
                self.view.msg("Las contraseñas no son idénticas. Reintente.")
        self.view.ask("¿Desea otorgar privilegios de admin? (0=No, 1=Sí): ")
        u_admin = input()
        return [u_pass, u_admin]

    def create_user(self):
        u_id, u_pass, u_admin = self.insert_user()
        out = self.model.create_user(u_id, u_pass, u_admin)
        if out == True:
            self.view.ok(u_id, "agregado")
        else:
            self.view.error("No se pudo agregar a este usuario.")
        return
    
    def read_user(self):
        self.view.ask("Nombre de usuario: ")
        u_id = input()
        user = self.model.read_user(u_id)
        if type(user) == tuple:
            self.view.show_header(' Datos de '+u_id+' ')
            self.view.show_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if user == None:
                self.view.error('Este usuario no existe.')
            else:
                self.view.error('No se puede leer este usuario.')
        return
    
    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_all_users(users)
        else:
            self.view.error("No se pudo recuperar la lista de usuarios.")
        return
    
    def update_user(self):
        self.view.ask("Nombre de usuario: ")
        u_id = input()
        user = self.model.read_user(u_id)
        if type(user) == tuple:
            self.view.show_header(' Datos de '+u_id+' ')
            self.view.show_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if user == None:
                self.view.error('Este usuario no existe.')
            else:
                self.view.error('No se puede leer este usuario.')
            return
        self.view.msg("Introduzca datos a actualizar. Deje en blanco para mantener igual.")
        u_pass, u_admin = self.read_update_user()
        out = self.model.update_user(u_id, u_pass, u_admin)
        if out == True:
            self.view.ok(u_id, 'actualizó')
        else:
            self.view.error('No se pudo actualizar usuario.')
        return
    
    def delete_user(self):
        self.view.ask('Nombre de usuario: ')
        u_id = input()
        self.view.ask('¿Seguro que desea proceder? (S=Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_user(u_id)
            if count != 0:
                self.view.ok(u_id, 'borrado')
            else:
                if count == 0:
                    self.view.error('Este usuario no existe.')
                else:
                    self.view.error('Error al borrar usuario.')
        else:
            self.view.msg("Cancelando operación...")
        return
    
    """
    ************ Movies methods ************
    """
    def movie_menu_adm(self):
        while True:
            self.view.movie_menu_adm()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_movie()
            elif op == '2':
                self.read_movie()
            elif op == '3':
                self.read_movie_name()
            elif op == '4':
                self.read_all_movies()
            elif op == '5':
                self.update_movie()
            elif op == '6':
                self.delete_movie()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def movie_menu_usr(self):
        while True:
            self.view.movie_menu_usr()
            self.view.select_option()
            op = input()
            if op == '1':
                self.read_movie_name()
            elif op == '2':
                self.read_all_movies()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def movie_data(self):
        self.view.ask("Nombre de película: ")
        p_name = input()
        self.view.ask("Género: ")
        p_genre = input()
        self.view.ask("Clasificación: ")
        p_class = input()
        return [p_name, p_genre, p_class]

    def create_movie(self):
        p_name, p_genre, p_class = self.movie_data()
        out = self.model.create_movie(p_name, p_genre, p_class)
        if out == True:
            self.view.ok(p_name, "agregado")
        else:
            self.view.error("No se pudo agregar la película.")
        return
    
    def read_movie(self):
        self.view.ask("ID de película: ")
        p_id = input()
        movie = self.model.read_movie(p_id)
        if type(movie) == tuple:
            self.view.show_header(' Datos de '+p_id+' ')
            self.view.show_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('La película no existe.')
            else:
                self.view.error('No se puede leer esta película.')
        return
    
    def read_movie_name(self):
        self.view.ask("Título: ")
        p_name = input()
        movies = self.model.read_movie_name(p_name)
        if type(movies) == list:
            self.view.show_header(' Películas llamadas \"'+p_name+'\" ')
            self.view.show_all_movies(movies)
            self.view.show_footer()
        else:            
            self.view.error('Error al recuperar películas.')
        return
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_all_movies(movies)
        else:
            self.view.error("No se pudo recuperar la lista de películas.")
        return
    
    def update_movie(self):
        self.view.ask("ID de película: ")
        p_id = input()
        movie = self.model.read_movie(p_id)
        if type(movie) == tuple:
            self.view.show_header(' Datos de '+p_id+' ')
            self.view.show_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('La película no existe.')
            else:
                self.view.error('No se puede leer esta película.')
            return
        self.view.msg("Introduzca datos a actualizar. Deje en blanco para mantener igual.")
        p_name, p_genre, p_class = self.movie_data()
        out = self.model.update_movie(p_id, p_name, p_genre, p_class)
        if out == True:
            self.view.ok(p_id, 'actualizó')
        else:
            self.view.error('No se pudo actualizar película.')
        return
    
    def delete_movie(self):
        self.view.ask('ID de película: ')
        p_id = input()
        self.view.ask('¿Seguro que desea proceder? (S=Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_movie(p_id)
            if count != 0:
                self.view.ok(p_id, 'borrado')
            else:
                if count == 0:
                    self.view.error('Esta película no existe.')
                else:
                    self.view.error('Error al borrar película.')
        else:
            self.view.msg("Cancelando operación...")
        return
    
    """
    ************ Halls methods ************
    """
    def hall_menu(self):
        while True:
            self.view.hall_menu()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_hall()
            elif op == '2':
                self.read_hall()
            elif op == '3':
                self.read_all_halls()
            elif op == '4':
                self.update_hall()
            elif op == '5':
                self.delete_hall()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def insert_hall(self):
        self.view.ask("ID de sala: ")
        s_id = input()
        self.view.ask("Descripción: ")
        s_desc = input()
        return [s_id, s_desc]

    def create_hall(self):
        s_id, s_desc = self.insert_hall()
        out = self.model.create_hall(s_id, s_desc)
        if out == True:
            self.view.ok(s_id, "agregado")
        else:
            self.view.error("No se pudo agregar la sala.")
        return
    
    def read_hall(self):
        self.view.ask("ID de sala: ")
        s_id = input()
        hall = self.model.read_hall(s_id)
        if type(hall) == tuple:
            self.view.show_header(' Datos de '+s_id+' ')
            self.view.show_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe.')
            else:
                self.view.error('No se puede leer esta sala.')
        return
    
    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_all_halls(halls)
        else:
            self.view.error("No se pudo recuperar la lista de salas.")
        return
    
    def update_hall(self):
        self.view.ask("ID de sala: ")
        s_id = input()
        hall = self.model.read_hall(s_id)
        if type(hall) == tuple:
            self.view.show_header(' Datos de '+s_id+' ')
            self.view.show_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe.')
            else:
                self.view.error('No se puede leer esta sala.')
            return
        self.view.msg("Introduzca datos a actualizar. Deje en blanco para mantener igual.")
        self.view.ask("Descripción: ")
        s_desc = input()
        out = self.model.update_hall(s_id, s_desc)
        if out == True:
            self.view.ok(s_id, 'actualizó')
        elif out == False:
            self.view.msg("Cancelando operación...")
        else:
            self.view.error('No se pudo actualizar sala.')
        return
    
    def delete_hall(self):
        self.view.msg("Bajo condiciones normales no debe borrar una sala. Solo si existe una condición extraordinaria debería avanzar.")
        self.view.ask("¿Desea proceder? (S=Sí) ")
        confirm = input()
        if confirm.lower() == 's':
            self.view.ask('ID de sala: ')
            s_id = input()
            self.view.ask('¿Está completamente seguro de querer continuar? (S=Sí) ')
            confirm = input()
            if confirm.lower() == 's':
                count = self.model.delete_hall(s_id)
                if count != 0:
                    self.view.ok(s_id, 'borrado')
                else:
                    if count == 0:
                        self.view.error('Esta sala no existe.')
                    else:
                        self.view.error('Error al borrar sala.')
            else:
                self.view.msg("Cancelando operación...")
                return
        else:
            self.view.msg("Cancelando operación...")
            return
    
    """
    ************ Seats methods ************
    """
    def seat_menu(self):
        while True:
            self.view.seat_menu()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_seat()
            elif op == '2':
                self.read_seat()
            elif op == '3':
                self.read_seats_hall()
            elif op == '4':
                self.delete_seat()
            elif op == '0':
                return
            else:
                self.view.option_invalid()

    def seat_data(self):
        self.view.ask("ID del asiento: ")
        a_id = input()
        self.view.ask("ID de la sala: ")
        s_id = input()
        return [a_id, s_id]

    def create_seat(self):
        a_id, s_id = self.seat_data()
        out = self.model.create_seat(a_id, s_id)
        if out == True:
            self.view.ok(a_id, "agregado")
        else:
            self.view.error("No se pudo agregar el asiento.")
        return
    
    def read_seat(self):
        self.view.ask("ID de asiento: ")
        a_id = input()
        seat = self.model.read_seat(a_id)
        if type(seat) == tuple:
            self.view.show_header(' Datos de '+a_id+' ')
            self.view.show_seat(seat)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if seat == None:
                self.view.error('El asiento no existe.')
            else:
                self.view.error('No se puede leer este asiento.')
        return
    
    def read_seats_hall(self):
        self.view.ask("ID de sala: ")
        s_id = input()
        seats = self.model.read_seats_hall(s_id)
        if type(seats) == list:
            self.view.show_header(' Asientos de la sala '+s_id+' ')
            self.view.show_all_seats(seats)
            self.view.show_footer()
        else:
            self.view.error("No se pudo recuperar la lista de asientos.")
        return
    
    def delete_seat(self):
        self.view.ask('ID de asiento: ')
        a_id = input()
        self.view.ask('¿Seguro que desea proceder? (S=Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_seat(a_id)
            if count != 0:
                self.view.ok(a_id, 'borrado')
            else:
                if count == 0:
                    self.view.error('Este asiento no existe.')
                else:
                    self.view.error('Error al borrar asiento.')
        else:
            self.view.msg("Cancelando operación...")
        return
    
    """
    ************ Schedules methods ************
    """
    def fun_menu_adm(self):
        while True:
            self.view.fun_menu_adm()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_func()
            elif op == '2':
                self.read_func()
            elif op == '3':
                self.read_func_date()
            elif op == '4':
                self.read_func_movie()
            elif op == '5':
                self.read_all_funcs()
            elif op == '6':
                self.update_func()
            elif op == '7':
                self.delete_func()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def fun_menu_usr(self):
        while True:
            self.view.fun_menu_usr()
            self.view.select_option()
            op = input()
            if op == '1':
                self.read_func_date()
            elif op == '2':
                self.read_func_movie()
            elif op == '3':
                self.read_all_funcs()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def func_data(self):
        self.view.ask("ID de película: ")
        p_id = input()
        self.view.ask("ID de sala: ")
        s_id = input()
        self.view.ask("Fecha y hora de emisión (AAAA-MM-DD HH:MM:SS): ")
        f_date = input()
        return [p_id, s_id, f_date]

    def create_func(self):
        p_id, s_id, f_date = self.func_data()
        out = self.model.create_func(p_id, s_id, f_date)
        if out == True:
            self.view.ok("Función para {}, sala {}".format(f_date, s_id), "agregado")
        else:
            self.view.error("No se pudo agregar la función.")
        return
    
    def read_func(self):
        self.view.ask("ID de función: ")
        f_id = input()
        func = self.model.read_func(f_id)
        if type(func) == tuple:
            self.view.show_header(' Datos de '+f_id+' ')
            self.view.show_func(func)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if func == None:
                self.view.error('La función no existe.')
            else:
                self.view.error('No se puede leer esta función.')
        return
    
    def read_func_date(self):
        self.view.ask("Fecha y hora de función (AAAA-MM-DD HH:MM): ")
        f_date = input()
        f_date = f_date+":00"
        funcs = self.model.read_func_date(f_date)
        if type(funcs) == list:
            self.view.show_header(' Funciones proyectadas en '+f_date+' ')
            self.view.show_all_funcs(funcs)
            self.view.show_footer()
        else:
            self.view.error("No se pudo recuperar la lista de funciones.")
        return
    
    def read_func_movie(self):
        self.view.ask("ID de película: ")
        p_id = input()
        funcs = self.model.read_func_movie(p_id)
        if type(funcs) == list:
            self.view.show_header(' Funciones proyectando '+p_id+' ')
            self.view.show_all_funcs(funcs)
            self.view.show_footer()
        else:
            self.view.error("No se pudo recuperar la lista de funciones.")
        return
    
    def read_all_funcs(self):
        funcs = self.model.read_all_funcs()
        if type(funcs) == list:
            self.view.show_all_funcs(funcs)
        else:
            self.view.error("No se pudo recuperar la lista de funciones.")
        return
    
    def update_func(self):
        self.view.ask("ID de función: ")
        f_id = input()
        func = self.model.read_func(f_id)
        if type(func) == tuple:
            self.view.show_header(' Datos de '+f_id+' ')
            self.view.show_func(func)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if func == None:
                self.view.error('La función no existe.')
            else:
                self.view.error('No se puede leer esta función.')
            return
        self.view.msg("Introduzca datos a actualizar. Deje en blanco para mantener igual.")
        p_id, s_id, f_date = self.func_data()
        out = self.model.update_func(f_id, p_id, s_id, f_date)
        if out == True:
            self.view.ok(s_id, 'actualizó')
        else:
            self.view.error('No se pudo actualizar función.')
        return
    
    def delete_func(self):
        self.view.ask('ID de función: ')
        f_id = input()
        self.view.ask('¿Seguro que desea proceder? (S=Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_func(f_id)
            if count != 0:
                self.view.ok(f_id, 'borrado')
            else:
                if count == 0:
                    self.view.error('Esta función no existe.')
                else:
                    self.view.error('Error al borrar función.')
        else:
            self.view.msg("Cancelando operación...")
        return
    
    """
    ************ Tickets methods ************
    """
    def tic_menu_adm(self):
        while True:
            self.view.tic_menu_adm()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_tic()
            elif op == '2':
                self.read_tic()
            elif op == '3':
                self.read_tic_fun()
            elif op == '4':
                self.read_tic_user()
            elif op == '5':
                self.update_tic()
            elif op == '6':
                self.delete_tic()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def tic_menu_usr(self):
        while True:
            self.view.tic_menu_usr()
            self.view.select_option()
            op = input()
            if op == '1':
                self.create_tic()
            elif op == '2':
                self.read_tic_user()
            elif op == '0':
                return
            else:
                self.view.option_invalid()
    
    def tic_data(self):
        self.view.ask("ID de función: ")
        f_id = input()
        self.view.ask("Asiento: ")
        a_id = input()
        if bool(self.user[1]):
            self.view.ask("Usuario a recibir boleto: ")
            u_id = input()
            return [f_id, a_id, u_id]
        return [f_id, a_id, self.user[0]]

    def create_tic(self):
        f_id, a_id, u_id = self.tic_data()
        out = self.model.create_tic(f_id, a_id)
        if out == True:
            tic = self.model.read_detailed_tic(f_id, a_id)
            out = self.model.create_tic_det(tic[0], u_id)
            if out == True:
                self.view.ok("Boleto para {}, función {}, asiento {}".format(u_id, f_id, a_id), "agregado")
            else:
                self.view.error("Su boleto no se registró correctamente. Contacte a soporte técnico para arreglar la situación.")
        else:
            self.view.error("No se pudo agregar el boleto.")
        return

    def read_tic(self):
        self.view.ask("ID de boleto: ")
        b_id = input()
        tic = self.model.read_tic(b_id)
        if type(tic) == tuple:
            self.view.show_header(' Datos de '+b_id+' ')
            self.view.show_tic(tic)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if tic == None:
                self.view.error('El boleto no existe.')
            else:
                self.view.error('No se puede leer este boleto.')
        return
    
    def read_tic_fun(self):
        self.view.ask("ID de función: ")
        f_id = input()
        tics = self.model.read_tic_fun(f_id)
        if type(tics) == list:
            self.view.show_header(' Boletos para función '+f_id+' ')
            self.view.show_all_tics(tics)
            self.view.show_footer()
        else:
            self.view.error('No se puede leer lista de boletos.')
        return
    
    def read_tic_user(self):
        if bool(self.user[1]):
            self.view.ask("Nombre de usuario: ")
            u_id = input()
        else:
            u_id = self.user[0]
        tics = self.model.read_tic_fun(u_id)
        if type(tics) == list:
            self.view.show_header(' Boletos de '+u_id+' ')
            self.view.show_all_tics(tics)
            self.view.show_footer()
        else:
            self.view.error('No se puede leer lista de boletos.')
        return
    
    def update_tic(self):
        self.view.ask("ID de boleto: ")
        b_id = input()
        tic = self.model.read_tic(b_id)
        if type(tic) == tuple:
            self.view.show_header(' Datos de '+b_id+' ')
            self.view.show_tic(tic)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if tic == None:
                self.view.error('El boleto no existe.')
            else:
                self.view.error('No se puede leer este boleto.')
            return
        self.view.msg("Introduzca datos a actualizar. Deje en blanco para mantener igual.")
        f_id, a_id, u_id = self.tic_data()
        out = self.model.update_tic(b_id, f_id, a_id)
        if out == True:
            if u_id == '' or (u_id == self.user[0] and not bool(self.user[1])):
                self.view.ok(b_id, 'actualizó')
            else:
                out = self.model.update_tic_det(b_id, u_id)
                if out == True:
                    self.view.ok(b_id, 'actualizó')
                else:
                    self.view.error('El usuario asociado no se actualizó correctamente. Verifique su información, y en caso de errores contacte a soporte.')
        else:
            self.view.error('No se pudo actualizar boleto.')
        return
    
    def delete_tic(self):
        self.view.ask('ID de boleto: ')
        b_id = input()
        self.view.ask('¿Seguro que desea proceder? (S=Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_tic_det(b_id)
            if count != 0:
                count = self.model.delete_tic(b_id)
                if count != 0:
                    self.view.ok(b_id, 'borrado')
                else:
                    if count == 0:
                        self.view.error("El boleto no se eliminó correctamente. Contacte a soporte para resolver el problema.")
                    else:
                        self.view.error("Error al borrar boleto.")
            else:
                if count == 0:
                    self.view.error('Este boleto no está asociado a un usuario o no existe. Si está seguro de que existe, contacte a soporte.')
                else:
                    self.view.error('Error al borrar boleto.')
        else:
            self.view.msg("Cancelando operación...")
        return