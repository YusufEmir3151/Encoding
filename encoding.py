import json


def main():
    # encoding.json dosyasını yükle
    with open("C:\\Users\\y.cetinkaya\\Desktop\\Deneme_Projeler\\Encoding\\encoding.json", "r",
              encoding="utf-8-sig") as f:
        encoding_data = json.load(f)
    while True:
        # Cümlenizi alın
        sentence = input("Cümlenizi girin: ")

        # Her bir harfi encoding'e çevirip listeye ekle
        encoded_result = []
        for char in sentence:
            for item in encoding_data:
                if char == item["text"]:
                    encoded_result.append(str(item["encoding"][0]))

        # Sonucu ekrana yazdır
        result_string = ",".join(encoded_result)
        print(result_string)
