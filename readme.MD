
# Web Scraping pour le site de Merch de Riot Games

Ce projet utilise **Selenium** pour récupérer des informations sur les produits disponibles sur le site **merch.riotgames.com**. Les données collectées incluent des informations sur les produits comme leur nom, prix, catégorie, images, et éditions limitées.

## Avertissement

Ce projet est uniquement destiné à un usage personnel et éducatif. **Je ne revendique aucune propriété sur les données collectées ou sur le site web de Riot Games**. Ce projet respecte les termes d'utilisation du site, mais il est recommandé de ne pas utiliser ce script pour des fins commerciales ou de scraper de manière abusive.

Le code est fourni tel quel, sans garantie d'aucune sorte. En utilisant ce projet, vous acceptez de respecter les conditions d'utilisation du site et de ne pas enfreindre les droits d'auteur de Riot Games ou d'autres parties.

## Prérequis

- Python 3.x
- Selenium
- ChromeDriver

## Installation

1. Cloner ce repository :
    ```bash
    git clone https://github.com/votre-utilisateur/riot-games-webscrap.git
    cd riot-games-webscrap
    ```

2. Télécharger **ChromeDriver** compatible avec votre version de Chrome et l'ajouter à votre PATH.

## Utilisation

1. Modifier les catégories de produits si nécessaire dans le fichier Python (voir `categories = [...]`).
2. Exécuter le script :
    ```bash
    python main.py
    ```

3. Les informations sur les produits seront sauvegardées dans un fichier `products.json`.

## License

Ce projet est sous licence **MIT**. Vous pouvez l'utiliser, le modifier et le distribuer tant que vous respectez les conditions de la licence.

---

**Attention** : Ce projet utilise des données publiques disponibles sur le site merch.riotgames.com, mais il est toujours important de vérifier les règles et politiques des sites web avant de procéder à un scraping massif.
