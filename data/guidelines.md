# Tagging Guidelines

There are sentences taken from product descriptions in `sentences.txt`. For each of them we want to determine if it "sounds green".

The file has a following structure
```
[sentence]\t[tag]
```
where the tag is either `+` (plus) for "green" sentences and `-` (minus) for "non-green" sentences.

We spot a "green sentence" if it has one of the following characteristics:

1. Claims about having natural, organic or bio ingredients such as: 

   > Sa formule contenant 99,7% d'ingrédients d'origine naturelle

2. Calls the product natural, organic or bio:

   > Sérum hydratant naturel intense, à la pivoine nordique

   > Offrez-vous les soins que vous méritez en réalisant jusqu'à 15 masques bio

   > Des soins naturels pour la peau

3. Mentions that the product is certified by Ecocert or other certifying organisation:

   > Une gamme engagée aux formules certifiées COSMOS ORANIC par Ecocert (ou certifiée BIO)

4. Highlights one specific plant-based ingredient:

   > Dans sa composition, nous retrouvons l’huile de jojoba, elle constitue en elle-même une véritable protection contre les agressions extérieures

   > L’huile végétale d’argan et de rose musquée sont réputées pour leurs propriétés nourrissantes, régénérantes et restructurantes	

5. Uses words such as *biodégradable*, *éco-responsable*:

   > Comme tous les produits Cosmydor, elle est 100% biodégradable, fabriquée et conditionnée artisanalement en France de manière éco-responsable, et proposée dans un contenant sans plastique de provenance européenne

6. Claims to be *sans qqch*:

   > Nos formules sont actives bio, cruelty-free et véganes sans parabens ni silicones

7.  A word withing the sentence has a prefix of bio- or éco-:

   > bio-active
   >
   > éco-extracted

There are cases where the sentence may appear "green" but it doesn't refer to the environment:

1. Natural as in "normal-looking":

   > Sans trace, bronzage naturel, Visage et corps	

2. Bio- and éco- not referring to plants or substances:

   > Pro**bio**tic
   > Éco+ (économique, pas cher)