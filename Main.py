#Requêtes utilisateur

cinq=int(input("Nombre de bateaux à 5 cases ="))
quatre=int(input("Nombre de bateaux à 4 cases ="))
trois=int(input("Nombre de bateaux à 3 cases ="))
deux=int(input("Nombre de bateaux à 2 cases ="))

cinqdown=int(input("Nombre de bateaux à 5 cases abbatus="))
quatredown=int(input("Nombre de bateaux à 4 cases abbatus ="))
troisdown=int(input("Nombre de bateaux à 3 cases abbatus ="))
deuxdown=int(input("Nombre de bateaux à 2 cases abbatus ="))

casesdisponibles=int(input("Nombre de cases disponibles autour (max 4) ="))

#Calcul du nombre de bâteaux restants (sauf les 1)

cinqrestant=cinq-cinqdown
quatrerestant=quatre-quatredown
troisrestant=trois-troisdown
deuxrestant=deux-deuxdown
sommerestant=cinqrestant+quatrerestant+troisrestant+deuxrestant

#Calcul des probabilités de la longueur du bateau touché (sauf les 1)

cinqproba=cinqrestant/sommerestant
quatreproba=quatrerestant/sommerestant
troisproba=troisrestant/sommerestant
deuxproba=deuxrestant/sommerestant

#Calcul des probabilités d'être au bord du bateau

cinqprobabord=2/5
quatreprobabord=2/4
troisprobabord=2/3
deuxprobabord=2/2

#Calcul de la probabilité de toucher en étant au bord du bateau

probabordtoucher=1/casesdisponibles

#Calcul de la probabilité de toucher en étant pas au bord du bateau

probapasbordtoucher=2/casesdisponibles

#Calcul de la probabilité finale

proba=cinqproba*(cinqprobabord*probabordtoucher+(1-cinqprobabord)*probapasbordtoucher)+quatreproba*(quatreprobabord*probabordtoucher+(1-quatreprobabord)*probapasbordtoucher)+troisproba*(troisprobabord*probabordtoucher+(1-troisprobabord)*probapasbordtoucher)+deuxproba*probabordtoucher

print("La probabilité de toucher à nouveau vaut",proba)