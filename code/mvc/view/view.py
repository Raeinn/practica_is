class View:
    """
    ************ General views ************
    """
    def start(self):
        print("\033[94m**********************************\033[0m")
        print("\033[94m==================================\033[0m")
        print("    \033[92mBienvenido al Sistema de Cine\033[0m     ")
        print("\033[94m==================================\033[0m")
        print("\033[94m**********************************\033[0m")
        
    def end(self):
        print("\n\033[94m----------------------------------\033[0m")
        print("\033[92m    ¡Vuelva pronto!    \033[0m")
        print("\033[94m----------------------------------\033[0m")
    
    def select_option(self):
        print("Seleccione una opción: ", end = '')

    def option_invalid(self):
        print("¡Opción inválida! Reintente.") 

    def ask(self, output):
        print(output, end = '')   

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('\033[92m+'*(len(str(id))+len(op)+24)+'\033[0m')
        print('\033[92m+ ¡'+str(id)+' se ha '+op+' correctamente! +\033[0m')
        print('\033[92m+'*(len(str(id))+len(op)+24)+'\033[0m')

    def error(self, err):
        print('\033[91m ¡ERROR! \033[0m'.center(len(err)+4,'-'))
        print('\033[91m- '+err+' -\033[0m')
        print('\033[91m-\033[0m'*(len(err)+4)) 
        
    def success(self):    
        print("\033[94mOperación exitosa.\033[0m")
    
    def invalid_id(self):
        print("\033[93mEsta ID es inválida.\033[0m") 

    def show_update(self):
        print("Actualize los campos necesarios.")
    
    def show_header(self, header):
        print(header.center(113,'*'))
        print('-'*113)
    
    def show_midder(self):
        print('-'*113)

    def show_footer(self):
        print('*'*113)
    
    """
    ************ User views ************
    """
    def log_in(self):
        print("\n\033[94m----------------------------------\033[0m")
        print("\033[94m        Introduzca sus credenciales        \033[0m")
        print("\033[94m----------------------------------\033[0m")

    def login_ok(self, id):
        print('\033[92m+ ¡'+str(id)+' ha ingresado correctamente! +\033[0m') 
    
    def admin_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú principal:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Menú de usuarios")
        print("2. Menú de películas") 
        print("3. Menú de salas")
        print("4. Menú de asientos")
        print("5. Menú de funciones")
        print("6. Menú de boletos")
        print("0. Log out")

    def general_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú principal:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Menú de películas") 
        print("2. Menú de funciones")
        print("3. Menú de boletos")
        print("0. Log out")
    
    def user_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de usuarios:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar usuario")
        print("2. Buscar usuario") 
        print("3. Lista de usuarios")
        print("4. Editar usuario")
        print("5. Borrar usuario")
        print("0. Regresar al menú anterior")
    
    def show_user(self, user):
        print('Usuario:', user[0])
        print('Privilegios de Admin:', bool(user[1]))
    
    def show_all_users(self, users):
        print('\n' + 'Usuario'.ljust(12) + '|' + '¿Admin?'.ljust(5) + '|')   
        print('-'*113)
        for record in users:
            if bool(record[1]):
                print(f'{record[0]:<12}|{bool(record[1])}   |')
            else:
                print(f'{record[0]:<12}|{bool(record[1])}  |')
        print('-'*113)
    
    """
    ************ Movie views ************
    """
    def movie_menu_adm(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de películas:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar película")
        print("2. Buscar película por ID") 
        print("3. Buscar película por título")
        print("4. Lista de películas")
        print("5. Editar película")
        print("6. Borrar película")
        print("0. Regresar al menú anterior")
    
    def movie_menu_usr(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de películas:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Buscar película por título")
        print("2. Lista de películas")
        print("0. Regresar al menú anterior")
    
    def show_movie(self, movie):
        print('ID:', movie[0])
        print('Título:', movie[1])
        print('Género:', movie[2])
        print('Clasificación:', movie[3])
    
    def show_all_movies(self, movies):
        print('\n' + 'ID'.ljust(3) + '|' + 'Título'.ljust(20) + '|' + 'Género'.ljust(12) + '|' + 'Clasificación'.ljust(5) + '|')   
        print('-'*113)
        for record in movies:
            print(f'{record[0]:<3}|{record[1]:<20}|{record[2]:<12}|{record[3]:<13}|')
        print('-'*113)
    
    """
    ************ Halls views ************
    """
    def hall_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de salas:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar sala")
        print("2. Buscar sala") 
        print("3. Lista de salas")
        print("4. Editar sala")
        print("5. Borrar sala (!)")
        print("0. Regresar al menú anterior")
    
    def show_hall(self, hall):
        print('ID:', hall[0])
        print('Descripción:', hall[1])
    
    def show_all_halls(self, halls):
        print('\n' + 'ID'.ljust(1) + '|' + 'Título'.ljust(12) + '|')   
        print('-'*113)
        for record in halls:
            print(f'{record[0]:<2}|{record[1]:<12}|')
        print('-'*113)
    
    """
    ************ Seats views ************
    """
    def seat_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de asientos:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar asiento")
        print("2. Buscar asiento por ID") 
        print("3. Buscar asientos por sala") 
        print("4. Borrar asiento(s)")
        print("0. Regresar al menú anterior")
    
    def show_seat(self, seat):
        print('ID:', seat[0])
        print('Sala:', seat[1])
    
    def show_all_seats(self, seats):
        print('\n' + 'ID'.ljust(4) + '|' + 'Sala'.ljust(1) + '|')   
        print('-'*113)
        for record in seats:
            print(f'{record[0]:<4}|{record[1]:<4}|')
        print('-'*113)
    
    """
    ************ Schedules views ************
    """
    def fun_menu_adm(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de funciones:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar función")
        print("2. Buscar función por ID") 
        print("3. Buscar función por fecha de emisión") 
        print("4. Buscar función por película") 
        print("5. Cartelera completa")
        print("6. Editar función")
        print("7. Borrar función")
        print("0. Regresar al menú anterior")
    
    def fun_menu_usr(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de funciones:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Buscar función por fecha de emisión") 
        print("2. Buscar función por película") 
        print("3. Cartelera completa")
        print("0. Regresar al menú anterior")
    
    def show_func(self, func):
        print('ID de función:', func[0])
        print('ID de película:', func[1])
        print('Sala:', func[2])
        print('Fecha de emisión:', func[3])
    
    def show_all_funcs(self, funcs):
        print('\n' + 'ID Función'.ljust(3) + '|' + 'ID Película'.ljust(3) + '|' + 'Sala'.ljust(1) + '|' + 'Fecha'.ljust(19) + '|')   
        print('-'*113)
        for record in funcs:
            print(f'{record[0]:<10}|{record[1]:<11}|{record[2]:<4}|{record[3]}|')
        print('-'*113)
    
    """
    ************ Tickets views ************
    """
    def tic_menu_adm(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de boletos:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Registrar boleto")
        print("2. Buscar boleto por ID") 
        print("3. Buscar boleto por función") 
        print("4. Buscar boletos de un usuario")
        print("5. Editar boleto")
        print("6. Borrar boleto")
        print("0. Regresar al menú anterior")
    
    def tic_menu_usr(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m           Menú de boletos:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("1. Comprar boleto")
        print("2. Historial de compras")
        print("0. Regresar al menú anterior")
    
    def show_tic(self, tic):
        print('ID:', tic[0])
        print('Función:', tic[1])
        print('Asiento:', tic[2])
        print('Usuario:', tic[3])
    
    def show_all_tics(self, tics):
        print('\n' + 'ID'.ljust(3) + '|' + 'Función'.ljust(3) + '|' + 'Asiento'.ljust(4) + '|' + 'Usuario'.ljust(12) + '|')   
        print('-'*113)
        for record in tics:
            print(f'{record[0]:<3}|{record[1]:<7}|{record[2]:<7}|{record[3]:<12}|')
        print('-'*113)
