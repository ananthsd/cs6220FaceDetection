from deepface import DeepFace
import pandas as pd


def find_image(img_path):
    try:
        df = DeepFace.find(img_path, db_path = "small_data")

        best = df.iloc[0]['identity']
        dash = best.index("/")+1
        best = best[dash:]
        dash = best.index("/")
        best = best[:dash]
        best = best.replace("_"," ")
        # print(best)
        return best
    except ValueError:
        return None


# find_image("patrick.jpg")