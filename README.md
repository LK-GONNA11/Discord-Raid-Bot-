# Discord Raid Bot

Ce script Python est un bot Discord simple qui effectue une série d'actions sur un serveur Discord spécifié. Il est conçu pour automatiser des tâches telles que la suppression de canaux existants, la création de nouveaux canaux, l'envoi de messages dans ces canaux et le renommage du serveur. **Utilisez ce script de manière responsable et éthique. L'utilisation non autorisée contre des serveurs que vous ne possédez pas ou pour lesquels vous n'avez pas l'autorisation de modifier est strictement interdite et peut avoir de graves conséquences.**

## Fonctionnalités

* **Modification du serveur :**
    * Renomme le serveur cible.
    * Supprime tous les canaux texte existants.
    * Crée un nombre spécifié de nouveaux canaux texte.
    * Envoie un nombre spécifié de messages dans chaque canal créé.
    * Renomme les canaux crées avec une mise en forme barrée.
    * Réinitialise les noms des canaux en supprimant la mise en forme barrée.
* **Entrée utilisateur :** Prend en compte les entrées de l'utilisateur pour le jeton du bot, l'ID du serveur, le nouveau nom du serveur, le nouveau nom du canal, le nombre de canaux et les messages par canal.

## Prérequis

* Python 3.6+
* `discord.py` (installez avec `pip install discord.py`)
* Un jeton de bot Discord (obtenu sur le Portail des développeurs Discord).
* L'ID du serveur Discord à modifier.

## Utilisation

1.  **Clonez le dépôt (si applicable) :**
    ```bash
    git clone https://github.com/LK-GONNA11/Discord-Raid-Server
    ```
2.  **Naviguez vers le répertoire du projet :**
    ```bash
    cd Discord-Raid-Server
    ```
    (Par exemple, `cd discord-raid-bot`)
3.  **Exécutez le script Python :**
    ```bash
    python main.py
    ```
    (Ou `python3 main.py` si nécessaire)
4.  **Entrez les informations :** Suivez les invites du script.
5.  **Le bot effectue les actions :** Les opérations sont automatisées.
6.  **Option de réinitialisation des canaux :** Choisissez de réinitialiser les noms des canaux à la fin.

## Notes importantes

* **Sécurité du jeton :** Gardez votre jeton en sécurité.
* **Permissions :** Assurez-vous que le bot a les permissions nécessaires.
* **Limites de débit :** Discord a des limites de débit.
* **Utilisation éthique :** Utilisez ce script de manière responsable.
* **Dépendances :** Si vous rencontrez des erreurs de dépendances, assurez vous d'avoir installé le module discord.py.

## Clause de non-responsabilité

Ce script est fourni à des fins éducatives. L'auteur n'est pas responsable de toute mauvaise utilisation.
