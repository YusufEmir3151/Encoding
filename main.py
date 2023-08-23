import encoding
import decoding

while True:
    print("İşlem seçin:")
    print("1- Şifreleme")
    print("2- Çözümleme")
    x = input("işlem: ")
    if x == 1:
        encoding.main()
    elif x == 2:
        decoding.main()
    else:
        print("yanlış seçim")
        exit()
