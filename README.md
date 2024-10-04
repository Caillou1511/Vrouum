# Vrouum
## Objectif
Compromettre le système de la voiture grâce à un script python. 
## Trouver l'ID
Une fois toutes les interfaces lancée.  
_**./controls vcan0**_  
_**./iscim vcan0**_  
Nous pouvons lancer un candump qui va venir récupérer tous les messsages CAN générer par notre interface, notre manette.  
_**candump vcan0**_  
 
J'ai créé mon candump et de la je l'ai split.
Grace à canplayer je lancais mes differents fichier pour savoir lequel contenait l'ID pour l'ouverture de porte.
A chaque fois je gardais le fichier qui contenanit l'ID.
J'ai continué de le faire jusqu'a avoir un fichier qui ne contenanit qu'une ligne.
Je sais que j'aurais pu faire un script qui aurait automatiser la demarche mais j'aimais bien le faire a la main.
![Capture d'écran 2024-10-03 214521](https://github.com/user-attachments/assets/21bf2e36-53a2-4cd8-97df-066fbb35f328)
![Capture d'écran 2024-10-03 214545](https://github.com/user-attachments/assets/142321f4-7807-4dbc-bd44-a59a7f0b9ce4)
![Capture d'écran 2024-10-03 214606](https://github.com/user-attachments/assets/a640e6d6-3688-4dd0-9597-a16fafebf7b3)

## Script python
Une fois l'ID trouvé il sufisait de faire un script qui allait envoyé un message au bus can. Le message etant celui d'ouvrir la porte grace a son ID.

![Capture d'écran 2024-10-04 135350](https://github.com/user-attachments/assets/8f1d82d1-dfbc-45ec-b017-99f0c32b6f52)
