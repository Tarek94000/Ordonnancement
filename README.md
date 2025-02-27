# Ordonnancement de Tâches

## Description
Le projet *Ordonnancement-main* vise à modéliser et optimiser l'ordonnancement de tâches en utilisant des algorithmes avancés. Il permet de gérer des tâches avec des dépendances et de déterminer les temps critiques du projet.

## Fonctionnalités
- **condition.py** : Gestion des contraintes et dépendances entre tâches.
- **process.py** : Implémentation des algorithmes d’ordonnancement.
- **read_display.py** : Lecture des données et affichage des résultats.
- **main.py** : Script principal permettant d'exécuter le programme.
- **test.py** : Tests unitaires pour vérifier la fiabilité des algorithmes.
- **Tables/** : Contient des fichiers de données servant de cas de test.
- **Tests/** : Contient des scénarios de validation.

## Installation
1. Cloner le dépôt :
   ```sh
   git clone https://github.com/tarek94000/Ordonnancement-main.git
   cd Ordonnancement-main
   ```
2. Installer les dépendances :
   ```sh
   pip install -r requirements.txt
   ```
   *(Si `requirements.txt` n'est pas disponible, installez manuellement les bibliothèques requises.)*

## Utilisation
Pour exécuter le projet :
```sh
python main.py
```
Ou directement depuis l'interpréteur.
Cela analysera les fichiers de données et affichera l'ordonnancement optimisé des tâches.

## Algorithmes implémentés
1. **Méthode des temps les plus précoces** - Détermine les temps de début et de fin les plus précoces des tâches.
2. **Méthode des temps les plus tardifs** - Calcule les marges et identifie les tâches critiques.
3. **Méthode du chemin critique (CPM - Critical Path Method)** - Identifie les tâches critiques qui influencent la durée totale du projet.
4. **Tri topologique** - Trie les tâches en fonction des dépendances pour assurer un bon ordre d’exécution.

## Contributions
Si vous souhaitez contribuer, veuillez ouvrir une *issue* ou proposer une *pull request* avec des améliorations.

## Auteurs
- Tarek (@tarek94000)

