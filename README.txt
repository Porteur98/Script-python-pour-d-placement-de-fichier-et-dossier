# Script-python-pour-d-placement-de-fichier-et-dossier

ATTENTION: Il s'agit d'un script non terminé. Il peut permettre d'effectué les différentes demandes possibles mais à condition de ne faire aucune faute de frappe, d'espace, etc.
Le code est surtout beaucoup plus optimisé au niveau du déplacement de fichier et de dossier, mais n'est pas parfait.

CE QUI RESTE A AMELIORER : 
- Possibilité de supprimer des dossiers.
- Copier/déplacer des dossiers. 
- Synchroniser mais avec plus d'options, notamment le système de "include" ou "exclude". 

          
EXPLICATION:         
Il s'agit d'un script python proposant à travers un menu de faire différentes gestions de fichiers et dossiers sur votre ordinateur local ou vers un poste distant. 
Le script a été fait pour la gestion de fichier ou dossier sur LINUX. Il est possible après de le modifier pour du Windows. 
L'intérêt du script a surtout été plus travaillé sur le déplacement de fichier et dossier dans son répertoire local. Cependant il y'a d'autre options en plus dans le menu (omme supprimer des fichiers ou faire une syncro de répertoire/dossier vers un autre poste) qui sont moins travaillés niveau développement. 

Principe du Script : 

A travers un menu vous verrez différentes options possible : 

1 - Déplacer des fichier ou dossiers.
2 - Supprimer des fichiers.
3 - Copier/Déplacer/ vers un autre poste.
4 - Synchroniser votre répertoire/dossier vers un autre poste/server.
5 - Quitter le programme.


I - Déplacer des fichier ou dossiers :

Vous pourrez à travers cette option, déplacer un ou plusieurs fichiers ou documents d'un dossier A à un dossier B. 
Cela est surtout utile quand vous avez plusieurs fichiers ou dossiers séparés dans d'autres dossier de votre ordinateur. 
La recherche des fichiers et des dossiers se font sur votre répertoire personnel, soit votre HOME.

EXEMPLE : 

Contexte : 
Vous avez plusieurs fichiers "jean" : jean1.txt, jean2.txt, jean3.txt, jeandelafontaine, etc.
Ils sont situés dans des dossiers différents : jean1.txt, jean2.txt dans dossier PrénomJean.
                                                   jean3.txt dans dossier Images. 
                                                   jeandelafontaine dans dossier Bureau. 
De plus, vous ne savez pas à la base où se trouve tous ces fichiers et vous souhaitez déplacer vos fichiers dans le dossier de destination "DossierPrénom".
    
    
Que permet le script ? 
      
Le script peut vous permettre de chercher tous les fichiers contenant la chaine de caractère "jean".
      
Ainsi il vous affiche tous les fichiers présent sur votre HOME avec cette chaine : jean1.txt, jean2.txt, jean3.txt, jeandelafontaine
      
Cependant, il se pourrait que vous ne soyez intéresser que par certain de ces fichiers. 
      
Admettant vous ne voulez déplacer que les .txt, le script va vous demander de saisir les fichiers qui vous intéresse.
     
Il suffit d'écrire juste ".txt" afin de sélectionner les fichiers avec l'extension .txt. Après en fonction des fichiers que vous avez, il est libre à vous de sélectionner       la chaine de caractère que vous souhaitez. La seule condition est qu'il faut que un fichier possède cette chaine de caractère saisie.
      
Une fois que vous avez saisie les fichiers que vous souhaitez, il faut saisir le nom d'un dossierde destination pour déplacer vos fichiers. 
      
Dans ce cas là, écrivez le nom d'un dossier que vous avez en tête sinon, juste avant la demande de saisie du nom de dossier de destination, on vous propose d'afficher une       arborescence de votre répertoire personnelle si vous désirez voir les différents dossiers existants.
      
Vous saississez comme nom de dossier de destination "DossierPrénom", le script vous affiche ensuite le(s) chemin(s) du(es) dossier(s) trouvé contenant la chaine de              caractère "DossierPrénom" ou non (dan ce cs il va vous demander de ressaisir à nouveau un nom). Il se peut que vous avez plusieurs dossiers avec la même chaine de               caractère. tout comme à l'image des fichiers jean, le script vous affichera le chemin de tous les dossiers trouvé mais il se suffira juste ici de copier/coller le chemin         du dossier qui vous intéresse.
      
Le script vous listera la liste des fichiers que vous souhaitez déplacer puis vous demandera de valider "oui" ou "non" pour le déplacement jusqu'à "DossierPrénomé". 
      
Une fois ceci effectué, vous retournez au menu du script. 
      
   
II- Supprimer des fichiers.

Vous pourrez ici saisir tout simplement les noms de fichiers à rechercher sur votre HOME pour ensuite le supprimer. Comme expliqué plus haut concernant les fichiers de même noms (ou non) situé dans dans endroits différents, cela peut-être utile. 
Ne pas écrire lors de la sélections des fichiers (après la recherche), le nom des extensions. Marquer au contraire le nom des fichiers avec les caractères que vous souhaitez. Pour la sélection par extension, je n'ai pas encore mis cela.


III- Copier/Déplacer/ vers un autre poste.

Vous pouvez copier ou déplacer un fichier vers un ordinateur distant. 
Il suffira d'écrire le nom des fichiers que vous souhaitez copier/déplacer, sélectionner les fichiers que vous souhaitez. Puis il faudra écrire les différents informations que l'on a besoin pour copier/déplacer vers le poste distant : on effectue cela par ssh. Les différentes informations sont : nom de l'user, ip, chemin du dossier de destination.


IV- Synchroniser votre répertoire/dossier vers un autre poste/server.

Vous pouvez synchroniser un dossier ou votre répertoire complet vers un autre ordinateur ou serveur. 
Ceci peut-être une alternative au copier/déplacer, toujours en ssh, l'avantage est que uen première il copie tous les éléments d'un dossier, puis quand vous refaites la prochaine fois l'opération, il se contente de "mettre à jour" sur l'autre poste/serveur (il compare les fichiers existant et manquants). 
Cela s'effectue avec la commande Linux "rsync", sur le script la commande a été configuré pour le strict minimum, mais il est possible de l'améliorer pour d'autre besoin. http://www.linuxguide.it/command_line/linux-manpage/do.php?file=rsync

Il suffira ici de saisir votre dossier source (de votre pc local) à synchroniser vers le poste distant, pis le dossier de destination qui correspond au dossier de sauvegarde/synchro sur le poste distant. Etant donne que ça se passe en ssh, il faudra rentré certaines informations : nom de l'user, ip.


      
      
      
      
      
      
    

                                             
