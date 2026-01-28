
# Lève-toi et Code

## 1 Décisions Mobile First

### Priorité au-dessus de la ligne de flottaison

- Titre principal (H1) avec promesse claire.
- Description courte du produit.
- CTA unique : « Commencer à coder ».
- Liste de bénéfices rapides (preuves).

Ces éléments permettent de comprendre l’offre en moins de 5 secondes et d’identifier immédiatement l’action principale.

### Éléments masqués / différés sur mobile

- Programme détaillé
- Newsletter
- Section inspiration
- Footer

Ces éléments sont secondaires pour un utilisateur mobile et alourdiraient inutilement la première lecture.

### Pourquoi

L’objectif est de réduire la charge cognitive sur mobile et de prioriser le message, le produit et l’action principale (CTA).  
Cela améliore la lisibilité, la performance perçue et la compréhension rapide de l’offre.

---

## 2 Responsive desktop (progressive enhancement)

### Breakpoint choisi

- 900px

Ce breakpoint correspond au passage classique tablette → desktop et permet d’enrichir la mise en page sans modifier la structure mobile.

### Enrichissements desktop

- Affichage de la navigation principale.
- Hero organisé en deux colonnes (contenu + avis).
- Affichage du programme en grille.
- Ajout de la newsletter.
- Ajout de la section inspiration.
- Affichage du footer.

### Pourquoi

Le desktop permet d’afficher plus d’informations sans nuire à la lisibilité.  
Ces éléments sont considérés comme des bonus informatifs pour les utilisateurs disposant d’un écran large.

Le CSS mobile n’est jamais modifié : uniquement enrichi via media query (progressive enhancement).

---

## 3 Performance et Audit

assets/lighthouse-mobile.png

Le Largest Contentful Paint (LCP) correspond au titre principal (H1) situé dans la section Hero, qui représente l’élément le plus important affiché à l’écran lors du chargement initial.  
La valeur mesurée (0,07 s) indique un affichage quasi instantané du contenu principal, ce qui améliore fortement la perception de rapidité pour l’utilisateur.  

Cette performance élevée est principalement due à l’absence d’images lourdes dans la zone critique et à l’utilisation de polices système, évitant tout téléchargement de ressources externes bloquantes.  
Le CLS est nul, ce qui garantit une stabilité visuelle totale pendant le chargement, et l’INP très faible assure une bonne réactivité lors des premières interactions.  

Ces choix techniques permettent d’obtenir une page rapide, lisible immédiatement et adaptée à un usage mobile.

### LCP identifié

Le LCP correspond au titre principal (H1) situé dans la section Hero.

### Deux actions décidées 

1. Utilisation d’une police système (system-ui) afin d’éviter le chargement de polices externes.
2. Suppression de toute image lourde dans le Hero pour garantir un affichage immédiat du message principal.

### Pourquoi

Ces choix réduisent le temps de rendu du contenu principal, améliorent la performance perçue et garantissent un affichage rapide du message clé, notamment sur mobile.
