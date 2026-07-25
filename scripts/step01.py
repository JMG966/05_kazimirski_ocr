import csv
import os
import sys

import cv2

RACINE_IMAGES = "images"
RACINE_MESURES = "mesures"
SUFFIXE_ORIG = "_orig.png"
SUFFIXE_STEP01 = "_step01.png"


def construire_chemin_source(nom_page):
    tome = nom_page[:5]
    return os.path.join(RACINE_IMAGES, tome, nom_page + SUFFIXE_ORIG)


def binariser_otsu(image):
    seuil, image_binarisee = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return seuil, image_binarisee


def ecrire_image_binarisee(image_binarisee, nom_page):
    tome = nom_page[:5]
    chemin = os.path.join(RACINE_IMAGES, tome, nom_page + SUFFIXE_STEP01)
    cv2.imwrite(chemin, image_binarisee)
    return chemin


def mettre_a_jour_csv_thresholds(nom_page, seuil):
    tome = nom_page[:5]
    chemin_csv = os.path.join(RACINE_MESURES, tome + "_thresholds_otsu.csv")

    lignes = []
    if os.path.isfile(chemin_csv):
        with open(chemin_csv, "r", newline="") as f:
            lecteur = csv.reader(f)
            lignes = list(lecteur)

    if lignes and lignes[0] == ["image", "threshold"]:
        en_tete = lignes[0]
        corps = lignes[1:]
    else:
        en_tete = ["image", "threshold"]
        corps = lignes

    corps = [ligne for ligne in corps if ligne and ligne[0] != nom_page]
    corps.append([nom_page, seuil])

    with open(chemin_csv, "w", newline="") as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow(en_tete)
        ecrivain.writerows(corps)

    return chemin_csv


def main():
    nom_page = sys.argv[1]

    chemin_source = construire_chemin_source(nom_page)
    image = cv2.imread(chemin_source, cv2.IMREAD_GRAYSCALE)

    seuil, image_binarisee = binariser_otsu(image)
    chemin_step01 = ecrire_image_binarisee(image_binarisee, nom_page)
    mettre_a_jour_csv_thresholds(nom_page, seuil)

    print(f"{nom_page},{seuil},{chemin_step01}")


if __name__ == "__main__":
    main()
