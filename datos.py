from credito.tarjeta import Tarjeta_de_credito
from credito.servicios import Tarjeta_de_servicios
from credito.usuario import Usuario


t1 = Tarjeta_de_servicios(nombre='BBVA Oro', deuda=30000)
t1.imprime_reporte()

t2 = Tarjeta_de_credito(nombre='Banamex Platino', tasa=24, deuda=2500, pagos=1300)
t2.imprime_reporte()

usuario1 = Usuario(nombre='Roberto Sánchez', tarjetas=[t1,t2])

t2.crea_json()
t5 = Tarjeta_de_credito()
t5.lee_json('tarjeta_platino.json')

usuario2 = Usuario(nombre='Arturo Álvarez', tarjetas=[t5])

t3 = Tarjeta_de_credito(nombre='Santander Free', deuda=20000, pagos=1200, cargos=100, tasa = 22)
usuario3 = Usuario(nombre='Ana Martínez', tarjetas=[t3])

t6 = Tarjeta_de_credito(nombre='Scotiabank Gold', tasa=20, deuda=100000, pagos=1300)
t6.imprime_reporte()
usuario4 = Usuario(nombre='Ana Vázquez', tarjetas=[t6])

base_de_usuarios = [usuario1,usuario2,usuario3,usuario4]