# API Choice

- Étudiant : Charlotte Gourmelon - - Devenas
- API choisie : Frankfurter API
- URL base : https://api.frankfurter.app
- Documentation officielle / README : Frankfurter API
- Auth : None 
- Endpoints testés :
  - GET /latest?from=EUR ... https://api.frankfurter.app/latest?from=EUR
  - GET /latest?from=EUR&to=USD ... https://api.frankfurter.app/latest?from=EUR&to=USD
 
- Hypothèses de contrat (champs attendus, types, codes) :


Lors de l’appel de l’API, la réponse est retournée au format JSON.
Les champs principaux attendus sont :
amount : nombre (float) correspondant au montant de base
base : chaîne de caractères indiquant la devise de base (ex : EUR)
date : chaîne de caractères représentant la date du taux
rates : objet JSON contenant les taux de conversion vers d’autres devises


Codes HTTP attendus :

200 : requête réussie

400 : paramètre incorrect (devise invalide par exemple)

500 : erreur interne du serveur



- Limites / rate limiting connu :


La Frankfurter API est une API publique gratuite et ne nécessite pas de clé.

La documentation ne mentionne pas de limite stricte de requêtes, mais comme toute API publique, il peut exister un rate limiting implicite si un trop grand nombre de requêtes est envoyé en peu de temps.


- Risques (instabilité, downtime, CORS, etc.) :


Les principaux risques possibles sont :

Indisponibilité temporaire de l’API (downtime serveur).

Latence variable selon la charge du serveur.

Changements futurs dans le format de la réponse JSON.

Limitation de requêtes si l’API détecte un usage trop intensif.

Problèmes réseau pouvant provoquer des timeouts.




EXEMPLE : 

GET /latest?from=EUR

<img width="853" height="809" alt="image" src="https://github.com/user-attachments/assets/b51d7d51-ece6-4a7f-8f80-ee79e8a35ede" />



