from Checkpoint.credito.tarjeta_sinclases import crea_tarjeta, pagos_distintos

from credito.usuario import multiples_reportes

t1 = crea_tarjeta()
t2 = crea_tarjeta()
t3 = crea_tarjeta()

tarjetas = [t1, t2, t3]

multiples_reportes(tarjetas)

pagos_distintos(t1, 100, 200, 1000)
