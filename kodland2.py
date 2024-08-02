meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY": "korkunç"
            }
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print("İstediğiniz kelimenin anlamı: ", meme_dict[word])
    else:
        print("Aradığınız kelime sözlükte bulunmamaktadır.")
