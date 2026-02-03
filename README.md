# Bot_Trading
Bot_Trading est un robot éducatif Python de trading screen-watcher. Il utilise la vision par ordinateur (OpenCV) pour analyser les graphiques Pocket Option, détecter les bougies et indicateurs RSI/MACD, puis générer des signaux CALL/PUT basés sur une stratégie de retournement, sans exécution automatique. Compatible Windows.


CAHIER DE CHARGES

BOT DE TRADING BASÉ SUR ANALYSE VISUELLE (SCREEN-WATCHER)


---

1. Contexte du projet

Le présent projet consiste à développer un bot de trading assisté, basé exclusivement sur l’analyse visuelle d’un graphique affiché à l’écran.

Le bot est destiné à un utilisateur non informaticien, sans connaissance en programmation ni en plateformes de développement (GitHub, API, MT4/MT5).

Le bot agit comme un assistant de trading et ne passe aucun ordre automatiquement.


---

2. Objectif général

L’objectif du bot est de :

Observer un graphique de trading affiché à l’écran

Analyser les bougies et indicateurs à partir d’images (screenshots)

Détecter des opportunités de trading (SIGNAL) selon des stratégies définies

Alerter l’utilisateur via son, message et capture d’écran



---

3. Définition du SIGNAL

Un SIGNAL correspond à :

> Une alerte indiquant qu’une configuration de marché conforme à une stratégie prédéfinie a été détectée sur une bougie clôturée, à partir d’une analyse visuelle.



Types de signaux :

CALL (ACHAT)

PUT (VENTE)


Un signal :

N’exécute aucun trade

Ne garantit aucun gain

Sert uniquement d’aide à la décision



---

4. Contraintes techniques majeures

Le bot fonctionne sous les contraintes suivantes :

❌ Aucun usage d’API de trading

❌ Aucun usage de MT4 / MT5

❌ Aucun accès direct aux données numériques du marché

✅ Analyse basée uniquement sur des images capturées de l’écran

✅ Utilisation de Computer Vision (OpenCV)



---

5. Principe de fonctionnement global

1. Capture automatique de l’écran (zone du graphique)


2. Prétraitement de l’image (nettoyage, contours, couleurs)


3. Détection visuelle des éléments suivants :

Bougies (couleur, taille, mèches)

Moyennes mobiles

RSI

MACD



4. Application des règles de stratégie


5. Application des filtres de sécurité


6. Génération d’un SIGNAL si toutes les conditions sont validées


7. Enregistrement et alerte




---

6. Stratégies intégrées

6.1 STRATÉGIE 1 – REVERSAL

Timeframe bougie : 30 secondes

Expiration recommandée : 2 minutes


Conditions CALL (ACHAT)

RSI visuel en zone basse (<30)

Histogramme MACD descendant puis montant

Prix visuellement proche de la MA lente

Bougie verte propre

Absence de tendance forte


Conditions PUT (VENTE)

RSI visuel en zone haute (>70)

Histogramme MACD montant puis descendant

Prix proche de la MA lente

Bougie rouge propre



---

6.2 STRATÉGIE 2 – CROSSING

Timeframe bougie : 30 secondes

Expiration recommandée : 1 minute


Conditions CALL

MA rapide croise MA lente vers le haut

Ligne MACD au-dessus de la ligne signal

Histogramme MACD positif

Bougie verte propre


Conditions PUT

MA rapide croise MA lente vers le bas

Ligne MACD sous la ligne signal

Histogramme MACD négatif

Bougie rouge propre



---

7. Filtres de sécurité (ANTI-PERTE)

Le bot doit ignorer toute analyse si :

Deux signaux consécutifs ont déjà été émis

La volatilité visuelle est excessive

Les mèches des bougies sont trop longues

Les moyennes mobiles sont plates

Le délai de cooldown (1 minute) n’est pas écoulé



---

8. Time Control

Analyse strictement interdite sur une bougie en cours

Analyse uniquement sur bougie clôturée

Intervalle d’analyse : 30 secondes



---

9. Sorties et alertes (OUTPUT)

À chaque SIGNAL, le bot doit produire :

🔊 Un signal sonore

🪟 Un message d’alerte à l’écran

📝 Un fichier de log (TXT / CSV)

🕒 Un horodatage précis

📸 Une capture d’écran annotée (flèche, texte)



---

10. Environnement utilisateur requis

Pour garantir le bon fonctionnement :

Système : Windows

Résolution écran fixe

Graphique toujours à la même position

Même thème graphique (couleurs)

Même niveau de zoom

Aucune fenêtre superposée au graphique



---

11. Livraison du projet

Le projet est livré sous forme :

D’un dépôt GitHub : Bot_Trading (compte : Nekena21)

D’un programme prêt à l’emploi

D’une documentation d’utilisation simplifiée


L’utilisateur final n’a aucune obligation de modifier le code.


---

11 bis. Récupération et installation du bot (UTILISATEUR NON TECHNIQUE)

Cette section décrit pas à pas comment l’utilisateur peut récupérer et lancer le bot sur son ordinateur sans connaissance de GitHub ni de programmation.

1. Téléchargement du bot depuis GitHub

1. Ouvrir un navigateur Internet (Chrome recommandé)


2. Aller sur le lien du dépôt GitHub fourni par le développeur


3. Cliquer sur le bouton Code


4. Cliquer sur Download ZIP


5. Une fois le fichier téléchargé, faire clic droit → Extraire tout


6. Choisir un dossier simple (exemple : Documents)



Le dossier Bot_Trading est maintenant présent sur l’ordinateur.


---

2. Pré-requis système

Avant le premier lancement, l’utilisateur doit disposer de :

Un ordinateur sous Windows

Une connexion Internet active

Python installé (version fournie ou installée avec assistance)


Aucune connaissance en programmation n’est requise.


---

3. Premier lancement du bot

1. Ouvrir le dossier Bot_Trading


2. Double-cliquer sur le fichier de lancement fourni (exemple : lancer_bot.bat)


3. Une fenêtre noire (terminal) s’ouvre automatiquement


4. Le message "Starting trading_bot_cv" confirme le démarrage



Le bot fonctionne désormais en arrière-plan.


---

4. Préparation de l’écran de trading

Pour que le bot fonctionne correctement, l’utilisateur doit :

Ouvrir la plateforme de trading (Pocket Option ou équivalent)

Afficher le graphique configuré par le développeur

Ne pas déplacer la fenêtre

Ne pas changer le zoom ou les couleurs

Éviter toute fenêtre superposée au graphique



---

5. Utilisation quotidienne

Le bot analyse automatiquement les bougies clôturées

Lorsqu’un SIGNAL est détecté :

un son est émis

un message apparaît

une capture d’écran est enregistrée



L’utilisateur peut alors décider manuellement d’entrer ou non en position.


---

6. Arrêt du bot

Pour arrêter le bot :

Cliquer sur la fenêtre du terminal

Appuyer sur Ctrl + C

Fermer la fenêtre


Le bot s’arrête immédiatement et sans risque.


---

12. Limites connues

Le bot n’est pas infaillible

La précision dépend fortement de la qualité de l’image

Toute modification graphique peut invalider l’analyse



---

13. Responsabilité

Le bot est un outil d’assistance.

L’utilisateur reste seul responsable de ses décisions de trading et des pertes éventuelles.


---

14. Conclusion

Ce bot constitue un assistant visuel avancé, reposant sur des règles strictes et une analyse par image. Il est destiné à un usage discipliné et contrôlé, et non à un trading automatique sans supervision humaine.