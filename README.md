# Vrouum
## Objectif
Compromettre le système de la voiture grâce à un script python. 
## Trouver l'ID
Une fois toutes les interfaces lancée.  
_**./controls vcan0**_  
_**./iscim vcan0**_  
Nous pouvons lancer un candump qui va venir récupérer tous les messsages CAN générer par notre interface, notre manette.  
_**candump vcan0**_  
Une fois le candump générer nous allons diviser le fichier pour pouvoir analyser par plus petit bloque nos log. On commencer par savoir combien de ligne comporte notre fichier.  
_**xc -l "nomdufichier.log"**_  
Puis on le divise.  
_**split -l "nombre de ligne voulu par fichier" "nomdufichier.log" "nomdessousfichier.log"**_  
Et on finit par rejouer les fichiers pour analyser l'action qu'il a sur notre interface icsim.  
_**canplayer -I "nomdufichier.log"**_    
Il nous suffit à chaque fois de garder le fichier qui contient la trame d'ouverture des portes.  
  
Il faut réitérer l'action jusqu'a se retrouver avec un fichier ne contenant qu'une seule ligne. Il est possible de faire un scripte pour automatiser le process mais j'ai voulu le faire à la main.

![Capture d'écran 2024-10-03 214521](https://github.com/user-attachments/assets/21bf2e36-53a2-4cd8-97df-066fbb35f328)
![Capture d'écran 2024-10-03 214545](https://github.com/user-attachments/assets/142321f4-7807-4dbc-bd44-a59a7f0b9ce4)
![Capture d'écran 2024-10-03 214606](https://github.com/user-attachments/assets/a640e6d6-3688-4dd0-9597-a16fafebf7b3)

## Script python
Une fois l'ID trouvé il sufisait de faire un script qui allait envoyé un message au bus can. Le message etant celui d'ouvrir la porte grace a son ID.

![Capture d'écran 2024-10-04 135350](https://github.com/user-attachments/assets/8f1d82d1-dfbc-45ec-b017-99f0c32b6f52)
