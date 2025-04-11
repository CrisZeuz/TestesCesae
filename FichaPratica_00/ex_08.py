#inputs das musicas

mus1min=int(input("minmusica1 ="))
music1seg=int(input("segmusic1 ="))
mus2min=int(input("minmusica2 ="))
music2seg=int(input("segmusic2 ="))
mus3min=int(input("minmusica3 ="))
music3seg=int(input("segmusic3 ="))
mus4min=int(input("minmusica4 ="))
music4seg=int(input("segmusic4 ="))
mus5min=int(input("minmusica5 ="))
music5seg=int(input("segmusic5 ="))


#iniciar e variavel segundos
totalsegundos = 0

#soma em min
Somaminutos= mus1min + mus2min + mus3min + mus4min + mus5min

#soma em seg
Somasegundos= music1seg + music2seg + music3seg + music4seg + music5seg


#Converter a duraçao para seg

totalsegundos += (Somaminutos * 60) + Somasegundos

#calcular todos os tempos

horas = Somaminutos // 3600
minutos= (Somasegundos % 3600) // 60
segundos= totalsegundos % 60


print(horas, "H", minutos, "m", segundos,"s")






