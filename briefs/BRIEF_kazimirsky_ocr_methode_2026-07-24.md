# Kazimirski OCR — Brief méthode de travail avec Claude Code

Date : 2026-07-24

Fait suite à la session de détection du filet vertical par suivi pas-à-pas
(méthode à 3 points HAUT/CENTRE/BAS + régression), au cours de laquelle
plusieurs correctifs successifs ont révélé des affirmations de validation
non vérifiées de la part de Claude Code (cas kaz01_1392, entre autres).
Ce document fixe le cadre de méthode à appliquer pour la suite du projet,
avant toute reprise du travail algorithmique lui-même.

## Comportement attendu de Claude Code (à placer en tête de chaque session/prompt)

Claude Code exécute strictement ce qui est écrit, sans reformuler, sans
compléter, sans corriger de sa propre initiative une ambiguïté perçue —
toute ambiguïté doit être signalée en retour, jamais résolue par une
hypothèse silencieuse. Aucune affirmation de succès, de validation ou de
correction n'est acceptée sans l'artefact qui la prouve (image régénérée,
valeurs chiffrées, diff de code) joint dans la même réponse. Un seul mode
par réponse : investigation seule (aucune modification de fichier) ou
modification (avec diff explicite) — jamais les deux mélangés, et le mode
doit être annoncé en première ligne. Toute modification de code doit être
précédée d'un commit git de l'état courant, et suivie d'un commit + push
une fois validée. Aucune amélioration, optimisation ou correction non
demandée ne doit être introduite à l'occasion d'une tâche précise.

## 1. Versioning
Compte GitHub existant. Claude Code effectue lui-même les commits et push,
à chaque étape validée — jamais de code modifié qui ne soit pas commité
avant la modification suivante.

## 2. Carte d'identité de l'image — bloc de constantes figé
Avant tout traitement, un bloc de constantes en tête de chaque script
définit précisément et sans ambiguïté possible : dimensions attendues,
zones de marge, définition exacte de « zone de texte utile », tout élément
géométrique identifiable directement sur l'image source. Rédigé par
Jean-Marc et Claude (chat), jamais interprété ou complété par Claude Code.

## 3 & 7. Prompts fermés, pas nécessairement courts
Un prompt peut être long (énumération de cas précis, carte d'identité
complète) mais ne doit contenir aucune justification, intention, ou
raisonnement (« pour éviter que... », « parce que... »). Uniquement des
faits vérifiables et des instructions fermées. Toute marge d'interprétation
laissée dans un prompt est une porte ouverte à une déviation.

## 4. Structuration systématique du code
Organisation imposée et identique à chaque script (constantes, fonctions
nommées par leur rôle exact, pas de fonction fourre-tout), pour pouvoir
demander une fonction précise par son nom plutôt que reformuler une requête
sujette à interprétation.

## 5 & 6. Arborescence des fichiers

```
/Volumes/SSD_JMG/00.General/05_kazimirsky_ocr/
├── images/
│   ├── kaz01/
│   │   ├── kaz01_xyzt_orig.png
│   │   ├── kaz01_xyzt_step01.png
│   │   ├── kaz01_xyzt_step02.png
│   │   └── ...
│   └── kaz02/
│       └── (même structure)
├── scripts/
│   ├── step01.py
│   ├── step02.py
│   └── ...
├── tests/        (contenu libre)
├── archives/     (tout ce qui ne sert plus)
├── mesures/      (fichiers de mémoire technique : seuils, mesures issues du pipeline)
├── briefs/       (briefings horodatés)
└── CHANGELOG.md
```

État au 2026-07-24 : arborescence des dossiers en place, seuls les fichiers
`_orig.png` sont présents ; `scripts/`, `tests/`, `archives/`, `mesures/`,
`briefs/` encore vides.

## 8. (réservé)

## 9. Aucune affirmation sans artefact
« Confirmé », « validé », « vérifié » sont interdits sans l'image, le
chiffre ou le diff correspondant produit dans la même réponse.

## 10. Suite de régression fixe et obligatoire — enrichie
Liste de pages-tests, non modifiable par Claude Code, à régénérer et
présenter systématiquement à chaque modification de code touchant la
détection du filet. Catégories à couvrir (représentatives du dictionnaire,
pas seulement les cas déjà rencontrés) :
- Page de titre de tome (kaz01_0001, kaz02_0001)
- Dernière page de tome / colophon (kaz01_1392, kaz02_1638)
- Changement de rubrique alphabétique proche du centre (kaz01_0076,
  kaz02_0131)
- Texte collé au filet / halo large (kaz02_0375, kaz02_0759)
- Page de référence historique du projet (kaz01_0180)
- Cas de point CENTRE mal placé, non résolus (kaz02_0354, kaz02_1051,
  kaz02_1399)
- Page à forte inclinaison réelle, cas de succès à ne pas régresser
  (kaz02_1325)
- Au moins une page ordinaire de chaque tome, prise au hasard à chaque run,
  en plus de la liste fixe

## 11. Un seul mode par réponse
Investigation seule ou modification, jamais les deux, annoncé en première
ligne de la réponse.

## 12. Changelog séparé
`CHANGELOG.md` daté, une ligne par changement réel, en plus des
commentaires versionnés dans le code lui-même.

## 13. Commit avant modification
Chaque modification de code précédée d'un commit de l'état courant
fonctionnel, pour garantir un retour en arrière réel (`git revert`), jamais
une reconstruction de mémoire.

## 14. Environnement figé
`requirements.txt` versionné et figé, pour éliminer toute variation de
comportement due à une bibliothèque.

## 15. Vérification humaine obligatoire avant tout passage à l'échelle
Aucun traitement complet du corpus (3030 pages) ne doit être relancé tant
que la suite de régression (point 10) n'a pas été inspectée visuellement
par Jean-Marc lui-même sur les images produites — jamais sur la seule base
d'un rapport de métriques.

## 16. Pas de seuils ou paramètres non spécifiés
Toute constante numérique introduite par Claude Code sans valeur donnée
explicitement doit être signalée comme telle (« seuil introduit, non
spécifié, à valider ») et jamais présentée comme faisant partie de la
consigne d'origine — pratique déjà bien suivie jusqu'ici, à maintenir
formellement.

## Prochaines étapes (à ce jour)
1. Migration mécanique : créer `CHANGELOG.md`, `requirements.txt`,
   initialiser le dépôt git avec premier commit (sans toucher à la
   logique algorithmique).
2. Rédaction commune (Jean-Marc + Claude, hors Claude Code) de la carte
   d'identité de l'image (point 2) avant toute reconstruction du script de
   détection du filet.
3. Reconstruction du script sous le nouveau régime, avec structuration
   imposée (point 4) et suite de régression (point 10) comme garde-fou
   systématique à chaque modification.
