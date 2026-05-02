meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Señor usuario la palabra no está disponible. Pero trabajaremos en ello")
