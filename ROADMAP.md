# Feuille de route — ANIP Django OCR

## Objectif

Faire évoluer ce dépôt en une application Django d’OCR de documents, fiable et facile à présenter. Le périmètre initial recommandé est l’extraction de texte et de champs depuis des formulaires. La comparaison de visages et l’estimation d’âge sont à reporter : elles ne sont pas implémentées actuellement et soulèvent des enjeux supplémentaires de vie privée, de biais et de conformité.

## État actuel observé

Le dépôt contient une structure Django, un formulaire d’envoi d’image et une vue OCR utilisant OpenCV et `pytesseract`. Les vues de comparaison de visages et d’estimation d’âge sont des fonctions vides. Les tests sont encore au stade de squelette, et le README ne décrit pas l’installation ni l’utilisation du projet.

Cette feuille de route est une proposition de travail, pas la confirmation que les fonctionnalités ont été testées en exécution.

## Étapes proposées

### 1. Définir le MVP — 1 à 2 jours

- Se concentrer d’abord sur l’OCR de formulaires, sans reconnaissance faciale ni estimation d’âge.
- Définir un scénario simple : téléverser une image, extraire le texte, afficher le résultat et laisser l’utilisateur le corriger.
- Choisir quelques champs à repérer, par exemple un nom, une date ou un numéro fictif.
- Décrire explicitement ce que l’application ne fait pas encore.

### 2. Rendre l’application utilisable de bout en bout — 3 à 5 jours

- Corriger ou retirer temporairement les routes `compare/` et `age/`. Les vues actuelles ne prennent pas le paramètre `request` requis par Django et ne réalisent aucun traitement.
- Vérifier le formulaire de téléversement, l’affichage du résultat et la gestion des erreurs : format invalide, image illisible ou texte vide.
- Ajouter un `requirements.txt` reproductible et documenter les commandes d’installation et de lancement dans le README.
- Documenter l’installation du binaire système Tesseract et de ses données linguistiques. Le paquet Python `pytesseract` seul ne fournit pas Tesseract ; prévoir notamment la langue française (`fra`).
- Stocker les fichiers téléversés de manière temporaire et les supprimer après traitement.

### 3. Ajouter tests et protections — 3 à 5 jours

- Limiter la taille des images et vérifier leur format réel avant traitement.
- Ajouter des tests pour les pages, les formulaires, les téléversements et les cas d’erreur.
- Configurer GitHub Actions pour lancer les tests à chaque modification.
- Ne pas conserver les documents ou résultats sans nécessité et expliquer clairement leur traitement.
- Avant toute mise en ligne, déplacer la clé secrète hors du code, désactiver `DEBUG` et configurer `ALLOWED_HOSTS` correctement.

### 4. Mesurer et améliorer l’OCR — environ 1 semaine

- Tester des prétraitements : niveaux de gris, contraste, redressement et résolution.
- Comparer les résultats avec et sans prétraitement sur un jeu de test distinct des données de développement.
- Conserver une transcription attendue (vérité terrain) et mesurer une métrique telle que le taux d’erreur de caractères.
- Présenter les limites de l’OCR et permettre à l’utilisateur de corriger le texte obtenu.
- Décrire la méthode et les résultats dans le README plutôt que de revendiquer une précision non mesurée.

### 5. Préparer une présentation convaincante — 2 à 3 jours

- Ajouter des captures d’écran ou une courte vidéo de démonstration.
- Fournir quelques documents de démonstration fictifs.
- Ajouter une section expliquant les limites, la confidentialité et les choix techniques.
- Si une démo est publiée, éviter le stockage permanent des fichiers téléversés.

Les durées sont des estimations indicatives pour organiser le travail ; elles dépendent de l’expérience et du temps disponible.

## Données et ressources possibles

Privilégier des jeux de données publics prévus pour la recherche ou des documents synthétiques. Vérifier la licence, les conditions d’accès et les restrictions de redistribution avant toute utilisation.

- [FUNSD](https://guillaumejaume.github.io/FUNSD/) — formulaires annotés, utiles pour tester l’extraction de texte et de champs.
- [XFUND](https://github.com/doc-analysis/XFUND) — formulaires multilingues annotés ; vérifier les langues et les conditions applicables au sous-ensemble choisi.
- [SROIE](https://rrc.cvc.uab.es/?ch=13) — reçus annotés, utiles pour l’OCR et l’extraction de champs, mais ce ne sont pas des pièces d’identité.
- [Tesseract — données de langue](https://github.com/tesseract-ocr/tessdata_best) — modèles linguistiques, dont `fra.traineddata` pour le français.
- [LFW](https://vis-www.cs.umass.edu/lfw/) — jeu connu pour l’évaluation de la vérification faciale. Son existence ne règle pas les questions de droits, de consentement ou d’adéquation à un usage réel ; la reconnaissance faciale est hors du périmètre du MVP proposé.

Pour une démonstration de formulaires d’identité, une option prudente consiste à créer des documents synthétiques : modèles conçus pour le projet, noms et dates fictifs, et marquage évident « DOCUMENT FICTIF ». Ne pas utiliser de vraies pièces d’identité trouvées en ligne ni les documents de proches. Éviter les données personnelles réelles.

## Ce qui peut intéresser les recruteurs

Le projet peut devenir un bon exemple de travail si la présentation met en évidence l’ingénierie autour de l’OCR, et pas seulement l’appel à une bibliothèque :

- une démo fonctionnelle et documentée ;
- une installation reproductible ;
- des tests automatisés et une CI ;
- une évaluation chiffrée, accompagnée de sa méthode ;
- une gestion sûre des fichiers et une explication claire de la confidentialité ;
- une présentation honnête des limites et des fonctionnalités non implémentées.

## Ordre de priorité recommandé

1. Construire un MVP d’OCR français sur des formulaires fictifs.
2. Le rendre installable, testable et documenté.
3. Ajouter une évaluation mesurée et une démonstration.
4. Ne considérer les fonctionnalités biométriques que séparément, après analyse des risques, des données et des obligations applicables.
