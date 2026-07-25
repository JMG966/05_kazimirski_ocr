import os
import sys

import cv2

RACINE_IMAGES = "images"
SUFFIXE_STEP01 = "_step01.png"
SUFFIXE_STEP02 = "_step02.png"


def construire_chemin_step01(nom_page):
    tome = nom_page[:5]
    return os.path.join(RACINE_IMAGES, tome, nom_page + SUFFIXE_STEP01)


def inverser_image(image):
    return cv2.bitwise_not(image)


def ecrire_image_inversee(image_inversee, nom_page):
    tome = nom_page[:5]
    chemin = os.path.join(RACINE_IMAGES, tome, nom_page + SUFFIXE_STEP02)
    cv2.imwrite(chemin, image_inversee)
    return chemin


def main():
    nom_page = sys.argv[1]

    chemin_step01 = construire_chemin_step01(nom_page)
    image = cv2.imread(chemin_step01, cv2.IMREAD_GRAYSCALE)

    image_inversee = inverser_image(image)
    chemin_step02 = ecrire_image_inversee(image_inversee, nom_page)

    print(f"{nom_page},{chemin_step02}")


if __name__ == "__main__":
    main()
