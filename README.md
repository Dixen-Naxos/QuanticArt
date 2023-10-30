# QuanticDream

## Pour les étapes de lancement :
 - Installer blender
 - Installer qiskit et qiskit-aer sur l'environnement python de blender
 - Ouvrir le fichier Rendu_spaghetti
 - Supprimer tous les objets

## Pour une génération à partir d'un objet complexe model :
 - Importer l'objet model, s'assurer qu'il est bien de type MESH et que ses vertex ont des coordonnées entière positives (cela fonctionnera aussi avec des nombres négatifs ou à virgule mais le résultat risque de ne pas correspondre exactement au model)
 - Sur les lignes 96 et 97 du script modifier le nom de l'objet model (actuellement : "Suzanne") par le nom de votre objet
 - Pour les très gros objets vous pouvez aussi modifier le nombre de qubits utiliser sur les lignes 79, 80, 81 (actuellement: 7, donc 2 puissance 7 = 128, notre objet fera maximum 128x128x128)
 - Lancer le script

## Pour un objet random:
 - Décommenter les lignes 94 et 95
 - Replacer le nom de l'objet sur les lignes 96 et 97 par "Cube"
 - Vous pouvez modifier les paramètres de la fonction de la ligne 94 afin de faire varier le nombre de vertices et la taille de l'objet
 - Lancer le script