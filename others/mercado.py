precio_menu = [1000, 2000, 3000, 4000, 5000]
opciones_clientes = []


def get_num_clientes():
    try:
        num_clientes = int(input('Ingrese la cantidad de clientes en la mesa: '))
        if num_clientes > 5 or num_clientes < 1:
            print('Solo se permiten de 1 a 5 clientes')
            get_num_clientes()
        return num_clientes
    except Exception as e:
        print(e)
        get_num_clientes()


def get_menu_clientes(num_clientes):
    for num in range(num_clientes):
        print()
        count = 0
        for menu in precio_menu:
            print(f'Menu #{count+1} = {menu}')
            count += 1
        get_menu_cliente(num)


def get_menu_cliente(cliente):
    try:
        menu_cliente= int(input(f'Ingrese el numero del menu para el cliente #{cliente+1}: '))
        if menu_cliente > 5 or menu_cliente < 1:
            print('Solo tenemos 5 menus')
            return get_menu_cliente(cliente)
        opciones_clientes.append(menu_cliente)
    except Exception as e:
        print(e)
        get_menu_cliente(cliente)


def get_info_pedidos(num_clientes):
    print('Cliente      Menu        Total')
    for num in range(num_clientes):
        print(f'{num+1}             {opciones_clientes[num]}            {precio_menu[opciones_clientes[num]-1]}')
    precio_total = 0
    for opcion in opciones_clientes:
        precio_total += precio_menu[opcion-1]
    print(f'Precio total: {precio_total}')


if __name__ == '__main__':
    numero_clientes = get_num_clientes()
    get_menu_clientes(numero_clientes)
    get_info_pedidos(numero_clientes)
