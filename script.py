#1) retorna 91
print("questão 1")
print("retorna 91")
print(" ")
#######################################

#2)
print("questão 2")
def pertence_a_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False
print(pertence_a_fibonacci(21))
print(pertence_a_fibonacci(20))
print(" ")
#####################################
#3)
print("questão 3")
print("a) 1, 3, 5, 7, 9")
print("b) 2, 4, 8, 16, 32, 64, 128")
print("c) 0, 1, 4, 9, 16, 25, 36, 49")
print("d) 4, 16, 36, 64, 100")
print("e) 1, 1, 2, 3, 5, 8, 13")
print("f) 2,10, 12, 16, 17, 18, 19, 200")
print(" ")
#4)
print("questão 4")
print("Ligue um dos interruptores e espere um pouco. Desligue e ligue um segundo interruptor. Vá até a sala.")
print("A lâmpada desligada e quente corresponde ao primeiro interruptor,") 
print("a lâmpada acesa ao segundo e a lâmpada apagada e fria ao terceiro.")
print(" ")

#5)
print("questão 5")
def inverte1(string):
    return string[::-1]
def inverte2(string):
    res = ""
    for i in string:
        res = i + res
    return res
print("resposta 1 " + inverte1("gabriel"))
print("resposta 2 " + inverte2("gabriel"))
