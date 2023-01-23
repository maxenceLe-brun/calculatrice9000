# calculatrice9000

Donc, j'ai pas l'habitude d'écrire ici mais on fera avec

## Explication et Utilisation

### Touches implémentés:

".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "√", "x!", "x^y", "x^-1", "Ran#", "MOD", "e", "+", "-", "*", "/", "CE", "=", "pi", "ln", "AC", "sin", "cos"

    x! est pour "factoriel de x"   |   Ran# place trois chiffres aléatoires   |   MOD prends le reste d'une division entière  
    CE est pour un retour arrière  |      ln est pour la fonction log(x)      |          AC est pour tout supprimer

### Touches inutiles :

"2nd" ne fais rien actuellement

### Touches non importés:

"deg", "nCr", "log", "tan"

         "nCr" est incompréhensible       |  "deg" sera un jour peut etre  
    "log" est juste après dans ma liste   |   "tan" me donne la migraine  

### Patch 1.0.1 : 23/01/23 2h20      

    AJOUTS :
    cos -> cosinus est désormais disponible! Précision plus ou moins fiable, a revoir
    sin -> sinus implémenté! Niveau précision, comme cosinus.
    
    BUGS :
    ln  -> calcul incorrect, en cours de formatage  
    Log -> implémentation log(x) = ln(x)/ln(10). Inutile due au mauvais calcul de ln  
    CE  -> Modifications sont prévus pour correctement supprimer la dernière "action" faite.
    /!\ -> Le calcul de charactères seul autre que : 1,2,3,4,5,6,7,8,9,0,.,π risque de faire planter le programme.
    
    
    

ATTENTION : si vous utilisez des touches non importés, cela fera crash votre lorsque vous appuirez sur "=".  
Si un appuis arrive, utilisez la touche AC pour éviter un redémarage de la fonction

J'espère que ce programme vous plaira!  
P.S. : je vais bientot commenter mon code, soyez patient !
