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
  
Il faut réitérer l'action jusqu'a se retrouver avec un fichier ne contenant qu'une seule ligne.  

![Capture d'écran 2024-10-03 214521](https://github.com/user-attachments/assets/21bf2e36-53a2-4cd8-97df-066fbb35f328)
![Capture d'écran 2024-10-03 214545](https://github.com/user-attachments/assets/142321f4-7807-4dbc-bd44-a59a7f0b9ce4)
![Capture d'écran 2024-10-03 214606](https://github.com/user-attachments/assets/a640e6d6-3688-4dd0-9597-a16fafebf7b3)  

J'ai également créé un script pour automatiser tout ce processus.
Le fonctionnement reste similaire à la méthode manuelle, mais avec l'avantage de gagner du temps et d'automatiser les étapes répétitives. Lors de l'exécution du script, vous serez invité à indiquer le fichier de logs sur lequel vous souhaitez travailler, ainsi que l'emplacement où vous souhaitez enregistrer les sous-fichiers générés.

Le script se charge ensuite de diviser les logs en sous-fichiers et de rejouer chaque segment. Il vous demandera simplement de confirmer si le fichier en question provoque l'ouverture des portes. Cela permet au script de filtrer progressivement les logs pour ne conserver que les trames pertinentes.

Avant chaque nouveau test, le script vous invite à refermer manuellement les portes afin que vous puissiez vérifier si les fichiers suivants continuent d'ouvrir les portes ou non.

## Script python pour exploiter la vulnérabilité
Une fois le log trouvé il faut exploiter la vulnérabilité. Pour cela il faut faire un script python qui va venir envoyer un message can. Ce message comportera l'ID et les données associé pour ouvrir les portes. 

![Capture d'écran 2024-10-04 135350](https://github.com/user-attachments/assets/8f1d82d1-dfbc-45ec-b017-99f0c32b6f52)


