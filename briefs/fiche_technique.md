# Fiche technique — Kazimirski OCR — Carte d'identité de l'image

Date : 2026-07-25
Étape 3 du plan établi le 2026-07-24 : rédaction commune (Jean-Marc + Claude, hors Claude Code) de la carte d'identité de l'image, avant reconstruction du script de détection du filet.

Statut : description et archivage des exemples en cours. Pas d'analyse ni de synthèse méthodologique à ce stade.

---

## 1. Contexte et cadrage

Hier : « Ça peut être fait maintenant, avec un prompt fermé... **Étape 3 — Rédiger nous-mêmes la "carte d'identité" avant de la donner à Claude Code**, comme tu l'as dit au point 2 : c'est un travail de définition qu'on doit faire à deux, pas une chose à lui demander d'inventer. »

---

## 2. kaz01_0180 — page standard (tome 1)

Texte original intégral :

> Prenons 01_180. Les éléments de la page sont:
>
> * nous avons ici une page du tome 1
> * c'est une page gauche (on voit l'amorce/ombre de la pliure à droite
> * En haut à gauche: numéro de page
> * Deux colonnes séparées par un filet vertical
> * Chaque colonne a un en-tête. C'est la dernière racine de la colonne
> * comme déjà mentionné, il y a à droite de la colonne de droite ce qu'on pourrait appeler l'amorce de la pliure du livre (zone grisée)
> * Chaque colonne a trois niveaux d'indentation:
>
> 1. niveau normal: corps de texte
> 2. indentation négative: les racines (entrée lexicale) avec une police plus grande. Mais il peut y avoir des entrées écrites en police standard. Ce sont des mots d'origine non-arabe ou des mots techniques dont l'origine n'est pas identifiée. Seule la première ligne des entrées lexicales est indentée ainsi
> 3. Indentation "nulle" (la référence d'alignement du texte): corps de texte des entrées lexicales
> 4. Indentation positive: les sous-rubriques (noms, adjectifs, adverbes...) de l'entrée lexicale
> 5. Les sous rubriques verbales (formes dérivées, passif...) sont dans le bloc de l'entrée lexicale avec les sous-rubriques en lignes marquées pour les formes dérivées par un chiffre latin (I, II, III, IV... jusqu'à XV)
> 6. le tiret cadratin ou semi-cadratin est utilisé pour la séparationdes modes (actif/passif) verbaux et pour séparer les exemples.
> 7. Plus en détail, mais on ne l'utilisera pas tout de suite: voyelle de l'inaccompli, pluriel, diptotes, synonymes, nom d'action, renvois...
>
> * Il peut y avoir, en bas des colonnes, des chifres latins ou des numéros qui sont des références d'imprimeris et qui ne nous intéressent pas

Correction (Jean-Marc) :

> Le filet certical s'arête en bas de la zone de texte mais peut reprendre dans les cas où la page est coupée (nouveau paragraphe alphabétique)

Remarques approuvées (Claude, non contestées) :
- Marge haute : numéro de page et en-têtes de colonne alignés sur une même ligne horizontale, au-dessus du filet
- Signes diacritiques débordant au-dessus de la ligne de portée normale (ex. بَـوَّالَـةٌ)
- Espacement variable entre entrées, pas systématique
- Zone grisée de pliure fine, épaisseur variable d'une page à l'autre
- Pas de chiffre d'imprimerie visible sur cette page précise

---

## 3. kaz01_0001 et kaz02_0001 — pages de titre

Texte original intégral :

> kaz01_0001 et kaz02_0001
> On aborde les différences techniques entre les deux volumes qui n'ont as été scannés de la même manière: le premier tome a un fond très clair alors que le second a un fon sépia avec des taches comme on le verra plus tard.
> Ces deux pages sont les premières pages de chacun des volumes
>
> * Titre sur 2 lignes "DICTIONNAIRE" / "ARABE-FRANÇAIS" en très grosse police et en majuscules
> * une "aeabesque de séparation
> * la première lettre du volume (ا pour le premier volume et ض pour le second) en très grosse police
> * Titre, arabesques et lettres arabes sont centrés sur la page
> * ensuite on a les deux colonnes sans entête avec le filet entre les colonnes
> * en bas de page on voit ici les caractères qui indiquent le volume à gauche et le chapitre à droite
> * la pliure est très légèrement visible à gauche (zone verticale un peu plus sombre, surtout en haut

Correction n°1 (Jean-Marc) :

> L'en-tête de colonne ne rappelle pas, comme la logique le voudrait, la racine précédente mais, comme je l'ai écrit pour l'image précédente, la dernière racine de la colonne
> Le filet vertical n'existe que quand il y a du texte (un peu plus bas que le haut de l'écriture quand il y a un mot arabe vocalisé sur la première ligne
> Petite numérotation d'entrée en haut de la colonne 1: explique, je ne vois pas

Correction n°2 (Jean-Marc) :

> Ah, mais c'est la lettre arabe ا (alif) elle-même, indentée négatif comme toutes les entrées lexicales.

Remarque approuvée (Claude) :
- Pas de numéro de page en haut sur ces deux pages

---

## 4. kaz01_1392 et kaz02_1638 — fins de tome

Texte original intégral :

> Les deux pages sont les fins de tome.
>
> * numéro de page
> * en-tête de colonnes
> * deux colonnes séparées par un filet vertical
>
> 1. Tome 1
>
> * Titre de bas de page en majuscules "FIN DU TOME PREMIER"
> * En dessous, la même chose en arabe
> * Une grosse arabesque
> * Les trois centrés sur la page
> * Tout en bas à droite: références de l'imprimerie
> * Page avec pas mal de taches sur la droite surtout (zone de pliure avec léger grisé)
> * Grosse tache/cercle manuscrit en dessous de Paris
>
> 2. Tome 2
>
> * Mêmes caractéristiques générales
> * Titre de bas de page en majuscules "FIN"
> * Signe manuscrit en gris clair en bas à gauche de la page
> * Pliure très légèrement marquée à droite
> * La caractéristique principale de cette page (et de plusieurs autres dans ce tome) est l'encre de la page précédente qui, presque partout, a traversé le papier (caractères en gris léger et dédoublement partiel du filet vertical)

Remarques approuvées (Claude) :
- Deux gabarits de colophon différents entre les tomes
- Bruit structurel généralisé sur toute la page kaz02_1638, pas localisé au seul filet

---

## 5. kaz02_0131 et kaz02_1325

Texte original intégral :

> 02_0131: page coupée par un changement de chapitre alphabétique
>
> * Dimensions (sur mon écran avec ma résolution: H_totale=12.7+3.5+20.3=36.5 W_totale= 21.1)
> * On en déduit facilement les % que j'estime applicables à toutes les pages su même style (à la position verticale du gap près, bien sûr.
> * La lettre de paragraphe alphabétique est centrée vertical dans le gap entre les deux blocs de texte. Police: la même taille que les entrées lexicales
> * L'image est inclinée (défaut de scanner), on en parle dans l'autre exemple. Mais ici on voit, grâce à la transparence du papier, que les deux filets verticaux sont bien alignés. Ce n'est pas toujours le cas...
>
> 02_1325: page inclinée
>
> * rien à part qu'il va falloir la redresser

Remarque approuvée (Claude) :
- Ratios calculés à partir des dimensions fournies : bloc_sup 34,8% / gap 9,6% / bloc_inf 55,6% de la hauteur totale

---

## 6. Nouvelle liste de référence des problèmes (tome 2, en cours)

Texte original intégral :

> kaz02_0375: je ne vois pas de problème à part l'inclinaison déjà décrite
> kaz02_0759: inclinaison entraînant une coupurs du texte
>
> * page inclinée fortement et décalage vers la gauche
> * Le scan a coupé quelques lettres finales. Reconstruction manuelle ou ré-écriture manuelle de la page
> * Il va falloir identifier ces pages: la distance entre le bord du texte arabe et le bord de l'image est nulle (après redressement)
>
> kaz02_0354: même problème que kaz02_0759 mais à droite. Même traitement à apporter
> kaz02_1051: changement de paragraphe alphabétique déjà traité.
>
> * Voici les dimensions de cette image (du même tome que la précédente: bloc_sup: 17.6 gap: 4.5 bloc_inf: 14.4 W: 21.4
> * Image légèrement inclinée
>
> Bon, le reste des images a déjà été décrit.

Consigne de rupture méthodologique (Jean-Marc) :

> Il faut conserver cette liste comme référence des problèmes (supprimer toute liste précédente)... nous repartons du début SANS TENIR COMPTE DES PROBLEMES SUCCESSIFS RENCONTRES. Nous ne conservons, en mémoire (archives/ rangés en vrac), que les techniques que nous devrons bien sûr améliorer avec de meilleurs prompts et une analyse préalable plus fine.

---

## 7. Pipeline technique (5 étapes)

Texte original intégral :

> 1. binarization de l'image:
>
> * mise de l'image en noir/blanc par suppression des pixels en dessous d'un threshold défini
>
> 2. Inversion de l'image
>
> * remplace les pixels blancs par des noirs et vice versa: augmentation de la finesse de lecture (blanc sur noir)
>
> 3. Rotation de l'image
>
> * alignement vertical des colonnes en travaillant sur le filet pour préparer le découpage en deux de la page
>
> 4. Découpage de la page
>
> * découpage sur le filet qui est maintenant vertical et création de deux fichiers: kaz0x_abcd_L.png et kaz0x_abcd_R.png
>
> 5. Nettoyage des images
>
> * élimination des artefacts et du bruit restant par reconnaissance de forme/concavité/taille

---

## Règle de méthode pour la suite de ce document

Toute observation de Jean-Marc est restituée mot à mot, sans reformulation ni interprétation. Les remarques de Claude sont insérées séparément, identifiées comme telles, et n'altèrent jamais le texte original — sauf si une remarque contredit une observation et que Jean-Marc l'a explicitement approuvée.

Statut : liste des problèmes tome 2 encore ouverte. En attente de la suite.
