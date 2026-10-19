print("_____ FP 01 | EX 08 _____")

totalSegundosAlbum = 0

# 1. Perguntar os valores ao utilizador
minutosLidos = int(input("Insira os minutos da musica 1: "))
segundosLidos = int(input("Insira os segundos da musica 1: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

minutosLidos = int(input("Insira os minutos da musica 2: "))
segundosLidos = int(input("Insira os segundos da musica 2: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

minutosLidos = int(input("Insira os minutos da musica 3: "))
segundosLidos = int(input("Insira os segundos da musica 3: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

minutosLidos = int(input("Insira os minutos da musica 4: "))
segundosLidos = int(input("Insira os segundos da musica 4: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

minutosLidos = int(input("Insira os minutos da musica 5: "))
segundosLidos = int(input("Insira os segundos da musica 5: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

print(f"Total segundos do album: {totalSegundosAlbum} s.")

# 2. Calculos
horas = totalSegundosAlbum // 3600
totalSegundosAlbum = totalSegundosAlbum % 3600

minutos = totalSegundosAlbum // 60
totalSegundosAlbum = totalSegundosAlbum % 60

segundos = totalSegundosAlbum

# 3. Apresentar resultado
print(f"Total Álbum: {horas}h {minutos}m {segundos}s")
