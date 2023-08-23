import json

def main():
    # encoding.json dosyasını yükle
    with open("C:\\Users\\y.cetinkaya\\Desktop\\Deneme_Projeler\\Encoding\\train.json", "r", encoding="utf-8-sig") as f:
        encoding_data = json.load(f)
    while True:
        # Şifrelenmiş sayı dizisini alın
        encoded_input = input("Şifrelenmiş metin: ")
        encoded_numbers = list(map(int, encoded_input.split(',')))

        # Şifrelenmiş sayı dizisini çözümle
        decoded_text = ""
        for number in encoded_numbers:
            for item in encoding_data:
                if number in item["encoding"]:
                    decoded_text += item["text"]
                    break

        print(decoded_text)
