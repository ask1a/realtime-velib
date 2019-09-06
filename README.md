# realtime-velib
kafka storm python realtime bike rent

Projet permettant de remonter l'activité en temps réel de l'utilisation des velos en libre service dans plusieurs villes.

L'idée était de creer une implémentation de Kafka et Storm en utilisant uniquement python (2.7 compatible storm)

Le projet fonctionne sous linux après avoir installé zookeeper, kafka, storm, maven et créé un topic kafka intitulé 'velib-stations'.
Un fois lancé les csv par ville du répertoire /tmp/stockage_ville sont alimentés en temps réel.

Lancement de l'application:
 - Lancer zookeeper
 - Lancer Kafka
 - Lancer Storm:
    - Nimbus
    - Supervisor(workers)
 - Creer le topic 'velib-stations' si ce n'est pas déjà fait
 - Lancer le producer Kafka 'get-stations.py'
 - Packager l'application via la commande 'mvn package' à la racine du projet
 - Lancer le .jar obtenu --> storm jar target/velos-1.0-SNAPSHOT.jar org.apache.storm.flux.Flux -r resource/topology.yaml (ne pas oublier de rajouter le dossier bin de l'application storm dans le PATH en éditant .bashrc)

Askia VANRYCKEGHEM, Axelle RABANY
