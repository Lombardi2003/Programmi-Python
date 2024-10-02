# Scrivere un programma che prenda in input un testo lungo
# Stampi la frequenza di ogni carattere
#
# Plus: stampare le frequenze in ordine crescente

a = input("Inserisci un testo lungo: ")
caratteri = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']

print("\nStampa delle frequenze non ordinate: ")
for c in caratteri:
    print(c,' = ',a.count(c))