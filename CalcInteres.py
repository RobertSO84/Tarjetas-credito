# Crear Tarjeta
#nombreTarjeta, interesAnual, deuda, pagoRealizar
tarjeta = {}
def crea_tarjeta ():
    
    print("Ingresa el nombre de tu tarjeta:")
    tarjeta['nombre'] = input()
    print("Ingresa la tasa de interés anual:")
    tarjeta['tasa'] = int(input())
    print("Ingresa el monto de tu deuda:")
    tarjeta['deuda'] = int(input())
    print("Ingresa el pago a realizar:")
    tarjeta['pagos'] = int(input())

    while tarjeta['pagos'] > tarjeta['deuda']:
        print("No puede realizar un pago mayor a su deuda")
        print("Ingrese su pago de nuevo:")
        tarjeta['pagos'] = int(input())
    
    print("Ingresa el monto de nuevos cargos:")
    tarjeta['cargos'] = int(input())
    print("Gracias")
    print(tarjeta)
    return tarjeta

crea_tarjeta()
print(tarjeta)

# Calptura y calcula nueva deuda

def captura_nueva_deuda ( tarjeta ):

    interesMensual = tarjeta['tasa'] / 12
    deudaRecalculada = (tarjeta['deuda'] - tarjeta['pagos'])*(1+(interesMensual/12/100))
    tarjeta['nueva_deuda'] = deudaRecalculada + tarjeta['cargos']
    return tarjeta

def imprime_reporte ( tarjeta ):
    tarjeta = captura_nueva_deuda(tarjeta)
    print("El resumen de su información es:")
    print("Nombre de la tarjeta: {}".format(tarjeta['nombre']))
    print("Su tasa de interes mensual es: {}".format(tarjeta['tasa']))
    print("Su deuda era de: {}".format(tarjeta['deuda']))
    print("Su pago fue de: {}".format(tarjeta['pagos']))
    print("Sus nuevos cargos del mes son: {}".format(tarjeta['cargos']))
    print("Su deuda actual es: {}".format(tarjeta['nueva_deuda']))

def multiples_reportes(tarjetas):
    for tarjeta in tarjetas:
        imprime_reporte(tarjeta)
    
t1 = {'nombre': 'oro', 'tasa': 40.0, 'deuda': 6000, 'pagos': 5000, 'cargos': 1000}
t2 = {'nombre': 'oro2', 'tasa': 30.0, 'deuda': 6000, 'pagos': 5000, 'cargos': 1000}
print(t1)
multiples_reportes([t1,t2])

def pago_recurrente(tarjeta, monto):
    tarjeta['pagos'] = monto
    tarjeta['cargos'] = 0
    while tarjeta['deuda'] > 0:
        if tarjeta['deuda'] < tarjeta['pagos']:
            tarjeta['pagos'] = tarjeta['deuda']
        imprime_reporte(tarjeta)
        tarjeta['deuda'] = tarjeta['nueva_deuda']

t3 = {'nombre': 'recurrente', 'tasa': 40.0, 'deuda': 60000, 'pagos': 5000, 'cargos': 1000}

pago_recurrente(t3, 5000)

#lista_tarjeta = [crea_tarjeta(), crea_tarjeta(), crea_tarjeta()]