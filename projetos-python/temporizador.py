import time

t = input("Digite o tempo(em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida")
    quit()
#\r significa reescrever
#se o usuario digitou 120, eu divido 60
while t != 0:
    minutos, segundos = divmod(t,60)
    timer = "{:02d}:{:02d}".format(minutos,segundos)
    print(timer,end="\r")
    time.sleep(1)
    t = t - 1

print("O tempo acabou")
