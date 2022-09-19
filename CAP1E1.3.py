#Se você correr 10 quilômetros em 42 minutos e 42 segundos,
# qual é o seu passo médio (tempo por milha em minutos e segundos)?
# Qual é a sua velocidade média em milhas por hora?

tempo = str(input('Convertendo minutos e segundos em horas'))
sec = 42 / 60
mim = (42 + sec) / 60
print('Convertido temos {} horas'.format(mim))

distancia = str(input('Convertendo km em milhas'))
km = 10 * 0.6213
print('Temos {} milhas em 10km'.format(km))

pm = str(input('Passo médio de milhas por minuto'))
p = (km / mim) / 60
print('O passo médio será {} milhas/segundos '.format(p))



