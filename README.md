# Minitrice

- [Installation](#installation)
- [Exécution](#exécution)
- [Générator](#générator)
- [Publication](#publication)
- [Liens utiles](#liens-utiles)

# Installation

## Prérequis

Ce projet utilise **Python 3**.

Si Python n'est pas installé :

### Ubuntu / Linux

```bash
sudo apt update
sudo apt install python3
```

### Windows or MacOS

Télécharger Python depuis : [https://www.python.org/downloads/](https://www.python.org/downloads/)


## Rendre les exécutables utilisables

Depuis la racine du projet :

```bash
chmod +x minitrice
chmod +x generator
```

# Exécution

## Mode interactif

```bash
./minitrice
```

Exemple :

```bash
$ ./minitrice
> 3+9
12
>
Fin des calculs :)
$ echo $?
0
```

## Mode STDIN

```bash
echo "3+12" | ./minitrice
```

Sortie :

```bash
15
$ echo $?
0
```

# Generator

Le programme `generator` génère des expressions aléatoires.

## Utilisation

```bash
./generator 5
```

Exemple :

```bash
7-9
84/12
3*4
12+8
100/5
```

## Gestion des erreurs

### 1. Argument manquant

On vérifie s'il y a bien tous les arguments en ligne de commande pour lancer le generator.

```bash
./generator
```

Sortie :

```bash
"Argument manquant."
```

### 2. Nombre entier

On vérifie si l'argument passé est bien un nombre entier.
```bash
./generator 4,2
```

Sortie :

```bash
"L'argument doit être un entier."
```

### 3. Nombre négatif

On vérifie que ce n'est pas un nombre négatif.


```bash
./generator -5
```

Sortie :

```bash
Le nombre d'expressions doit être >= 0.
```

# Publication
[Vidéo Gource](https://youtu.be/3IIUncoCSD8)



# Liens utiles
- [ChatGPT (OpenAI)](https://chat.openai.com/) : utilisé pour la création du fichier de test et la correction de certaines erreurs
- [Guide Gource](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : utilisé pour comprendre comment générer une vidéo Gource


