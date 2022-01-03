from credito.tarjeta import Tarjeta_de_credito
from credito.usuario import Usuario

t1 = Tarjeta_de_credito(nombre='oro', tasa=24, deuda=20000, pagos=13000)
t1.imprime_reporte()

t2 = Tarjeta_de_credito(nombre='platino', tasa=20, deuda=50000, pagos=20000)
t2.imprime_reporte()

usuario1 = Usuario(nombre='Juan', tarjetas=[t1])
usuario1.agrega_tarjeta(t2)
usuario1.multiples_reportes()

usuario1.cancela_tarjeta('oro')
usuario1.multiples_reportes()



