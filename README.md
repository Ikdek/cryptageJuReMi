**Méthode de cryptage/décryptage utilisée 🤔**

La méthode de cryptage/décryptage utilisée dans ce code est une variante du chiffrement de Vigenère 🔒. Le chiffrement de Vigenère est un algorithme de chiffrement polyalphabétique qui utilise une clé pour chiffrer et déchiffrer les données 🔑.

### **Principe de fonctionnement 🔄**

Le chiffrement fonctionne de la manière suivante :

1. **Chiffrement 🔒** :
 * Pour chaque caractère du texte en clair, on additionne la valeur ASCII de ce caractère avec la valeur ASCII du caractère correspondant de la clé (en utilisant la valeur modulo `len(key)` pour déterminer l'indice du caractère de la clé à utiliser) 📝.
 * On prend le résultat modulo 256 pour obtenir une valeur comprise entre 0 et 255, qui correspond à un caractère ASCII 🔢.
 * On convertit cette valeur en un caractère ASCII et on l'ajoute au résultat 📄.

2. **Déschiffrement 🔓** :
 * Pour chaque caractère du texte chiffré, on soustrait la valeur ASCII du caractère correspondant de la clé (en utilisant la même méthode que pour le chiffrement) de la valeur ASCII du caractère chiffré 📝.
 * On prend le résultat modulo 256 pour obtenir une valeur comprise entre 0 et 255, qui correspond à un caractère ASCII 🔢.
 * On convertit cette valeur en un caractère ASCII et on l'ajoute au résultat 📄.

### **Implémentation dans le code 💻**

Les fonctions `encrypt` et `decrypt` implémentent respectivement le chiffrement et le déchiffrement 🔒🔓.

* La fonction `encrypt(key, string)` prend en entrée une clé et un texte en clair, et renvoie le texte chiffré 🔒.
* La fonction `decrypt(key, encrypted_string)` prend en entrée une clé et un texte chiffré, et renvoie le texte en clair 🔓.

Le code utilise les opérations suivantes :

* `ord(char)` : renvoie la valeur ASCII d'un caractère 🔢.
* `chr(shift)` : renvoie le caractère correspondant à une valeur ASCII 📝.
* `% 256` : opération modulo pour garantir que la valeur résultante est comprise entre 0 et 255 🔢.

### **Exemple 📚**

Supposons que nous voulions chiffrer le texte "Hello" avec la clé "secret" 🔑.

1. On itère sur chaque caractère du texte :
 * 'H' (72) + 's' (115) = 187 % 256 = 187 => caractère ASCII 187 🔢
 * 'e' (101) + 'e' (101) = 202 % 256 = 202 => caractère ASCII 202 🔢
 * 'l' (108) + 'c' (99) = 207 % 256 = 207 => caractère ASCII 207 🔢
 * 'l' (108) + 'r' (114) = 222 % 256 = 222 => caractère ASCII 222 🔢
 * 'o' (111) + 'e' (101) = 212 % 256 = 212 => caractère ASCII 212 🔢

Le texte chiffré est donc la suite des caractères ASCII 187, 202, 207, 222, 212 🔒.

Pour déchiffrer, on effectue les opérations inverses en utilisant la même clé 🔓.

### **Remarques 📝**

* L'utilisation du modulo 256 permet de gérer les caractères ASCII étendus (valeurs supérieures à 127) 🔢.
* Il est important de noter que la sécurité d'un système de chiffrement repose non seulement sur l'algorithme utilisé, mais également sur la gestion des clés et d'autres facteurs 🔑.
