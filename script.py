#!/usr/bin/env python3

# Le dictionnaire Plantes et la liste Saisons de ce script sont valables pour les cultures sur le 45ème parallèle de l'hémisphère nord.

import time, os, pickle

OuiNon = ['Oui', 'Yes', 'O', 'Y', 'oui', 'OUI', 'yes', 'YES' 'o', 'y', 'Non', 'No', 'N', 'non', 'no', 'n', 'NON']
Oui = ['Oui', 'Yes', 'O', 'Y', 'oui', 'yes', 'o', 'y', 'OUI', 'YES']
Non = ['Non', 'No', 'N', 'non', 'no', 'n', 'NON', 'NO']



#Liste pour gérer les parcelles

with open('Hist', 'rb') as fichier:
	Recup = pickle.Unpickler(fichier)
	Historiques = Recup.load()

#Cultures =['Plante', 'Parcelle', 'Tâche', 'Année']

#Forme de la construction du dictionnaire "Historiques" dans Hist sauvegardé avec pickle
#Historiques = {('Parcelle','Année'):('Culture1','Culture2'),
#	((-1000,-1000),2015):('Pruneau', 'Courges'),
#	((0,0),2018):('Pomme de terre', 'NA'),
#	((0,0),2019):('Ail', 'Radis'),
#	((0,1),2019):('Pomme de terre', 'Laitue romaine')}



#Liste pour gérer les travaux saisonniers.

Saisons = ('Hiver2', 'Hiver3', 'Printemps1', 'Printemps2', 'Printemps3', 'Été1', 'Été2','Été3', 'Automne1', 'Automne2', 'Autonme3', 'Hiver1', 'NA')
SemisDebut = Saisons
SemisFin = Saisons
PlantationsDebut = Saisons
PlantationsFin = Saisons



#Dictionnaires et listes pour "typer" les plantes. 
#L'entrée 'Année' est reprise pour construire l'historique des parcelles.

Racines = ['Rhizome', 'Tubercule', 'Bulbe', 'Pivot', 'Fasciculé', 'Adventive']

Récoltes = [['Feuille', 'Fruit', 'Fleur', 'Racine', 'Graîne'], 'Année']

Familles=['Aïzoacées','Amaranthacées','Apiacées','Aracées','Asparagacées','Astéracées',
	'Basellacées','Boraginacées','Brassicacées','Campanulacées','Cannacées',
	'Chénopodiacées','Cucurbitacées','Cypéracées','Dioscoréacées','Fabacées',
	'Laitue','Lamiacées','Lauracées','Liliacées','Malvacées',
	'Onagracées','Oxalidacées','Plantaginacées','Poacées','Polygonacées',
	'Portulacacées','Renonculacées','Rosacées','Rutacées','Solanacées',
	'Tropaéolacées','Valérianacées','Verbenaceae']

Plantes = {'Amaranthe' : (Familles[1], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Arroche' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Arroche-fraise' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Asperge' : (Familles[4], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Artichaut' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Aubergine' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Bardane comestible' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Baselle rouge' : (Familles[6], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Betterave potagère' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Blette ou Poirée' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Bourrache orientale' : (Familles[7], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Bunias d\'Orient' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Calebasse ou Gourde' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Canna comestible' : (Familles[10], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Capucine tubéreuse' : (Familles[31], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cardon' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Carotte' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Céleri-rave' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cerfeuil tubéreux' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chayote' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chénopode Bon-Henri' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chervis' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chicorée frisée' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chicorée scarole' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chicorée sauvage' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou à grosses côtes' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou brocoli' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou de Bruxelles' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou de Chine' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou-fleur' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou frisé' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou pommé cabus' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chou-rave' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Claytone de Cuba' : (Familles[26], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Claytone de Sibérie' : (Familles[26], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cochléaire officinale' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Concombre' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cornichon' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Coqueret du Pérou' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Courge' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Courgette' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pâtisson' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Potiron' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Giraumon' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Citrouille' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Courge musquée' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Courge à la cire ou Bénincasa' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Crambé maritime' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cresson alénois' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cresson des jardins' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Crosne du Japon' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Daïkon Raphanus' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Dolique-asperge' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Épinard' : (Familles[11], Racines[3], Récoltes[0][0], SemisDebut[0], SemisFin[11], PlantationsDebut[12], PlantationsDebut[12]),    # Renseignements_complets (semis à étaler sur l'année)
	'Fenouil bulbeux' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Fève' : (Familles[15], Racines[4], Récoltes[0][1], SemisDebut[9], SemisFin[3], PlantationsDebut[12], PlantationsDebut[12]),    # Renseignements_complets (aussi possible de les semer en automne)
	'Ficoïde glaciale' : (Familles[0], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Fraisier ananas' : (Familles[28], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Fraisier à gros fruits' : (Familles[28], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Gesse commune' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Guimauve' : (Familles[20], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Haricot commun' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Hélianthi' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Igname de Chine' : (Familles[14], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Kiwano ou concombre métulifère' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Laitue pommée' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Laitue romaine' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Lentille cultivée' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Maceron' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Mâche' : (Familles[32], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Maïs sucré' : (Familles[24], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Margose ou concombre amer' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Melon' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Morelle de Balbis' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Navet' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Oignon' : (Familles[19], Racines[2], Récoltes[0][3], SemisDebut[3], SemisFin[9], PlantationsDebut[9], PlantationsFin[3]),    #
	'Onagre' : (Familles[21], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Oca du Pérou' : (Familles[22], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Oseille' : (Familles[25], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Patience' : (Familles[25], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Panais' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pastèque' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Persil tubéreux' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Petit pois' : (Familles[15], Racines[4], Récoltes[0][1], SemisDebut[9], SemisFin[3], PlantationsDebut[12], PlantationsDebut[12]),    #
	'Piment' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pissenlit' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Plantain corne de cerf' : (Familles[23], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Poireau' : (Familles[19], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Poire de terre' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Poire-melon' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pois-asperge' : (Familles[15], Racines[4], Récoltes[0][1], SemisDebut[9], SemisFin[3], PlantationsDebut[12], PlantationsDebut[12]),    #
	'Pois chiche' : (Familles[15], Racines[4], Récoltes[0][1], SemisDebut[9], SemisFin[3], PlantationsDebut[12], PlantationsDebut[12]),    #
	'Poivron' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pomme de terre' : (Familles[30], Racines[1], Récoltes[0][3], SemisDebut[12], SemisFin[12], PlantationsDebut[2], PlantationsFin[3]),	#
	'Pourpier' : (Familles[26], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Quinoa' : (Familles[11], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Radis' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Raiponce cultivée' : (Familles[9], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Roquette' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Rhubarbe' : (Familles[25], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Rutabaga ou chou-navet' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Salsifis' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Serpent végétal' : (Familles[12], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Scolyme d\'Espagne' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Scorsonère' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Soja Glycine' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Souchet ou amande de terre' : (Familles[13], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Taro Colocasia' : (Familles[3], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Tétragone cornue' : (Familles[0], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Tomate' : (Familles[30], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Topinambour' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Tournesol géant' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Ulluque' : (Familles[6], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Absinthe' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Agastache anisée' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Ail' : (Familles[19], Racines[2], Récoltes[0][3], SemisDebut[12], SemisDebut[12], PlantationsDebut[9], PlantationsFin[3]),    #
	'Aneth' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Angélique officinale' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Anis vert' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Aurone' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Basilic' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Bourrache' : (Familles[7], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Calament officinal' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Carvi' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Céleri à côtes' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cerfeuil' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Châtaigne de terre' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Chrysanthème comestible' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Ciboule commune' : (Familles[19], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Ciboulette' : (Familles[19], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Citronnelle de l\'Inde' : (Familles[24], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Coriandre' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cresson de Para' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Cumin de Malte' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Dracocéphale' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Échalote' : (Familles[19], Racines[2], Récoltes[0][3], SemisDebut[12], SemisDebut[12], PlantationsDebut[9], PlantationsFin[3]),    #
	'Estragon' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Fenouil officinal' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Hysope' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Lavande officinale' : (Familles[15], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Laurier sauce' : (Familles[18], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Livèche ou Ache des montagnes' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Mélisse officinale' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Menthe' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Menthe-coq' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Menthe pileuse' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Monarde' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Moutarde' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Origan ou marjoliane vivace' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Nigelle de Damas' : (Familles[27], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Pérille de Nankin' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Persicaire odorante' : (Familles[25], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Persil' : (Familles[2], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Petite pimprenelle' : (Familles[28], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Romarin' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Rue officinale' : (Familles[29], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Sarriette vivace' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Sauge officinale' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Sauge sclarée' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Stévie ou Stévia ou sucre en feuilles' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Tanaisie crispée' : (Familles[5], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Thym commun' : (Familles[17], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Raifort' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Verveine citronnelle' : (Familles[33], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0]),
	'Wasabi' : (Familles[8], Racines[0], Récoltes[0][0], SemisDebut[0], SemisFin[0], PlantationsDebut[0], PlantationsFin[0])}







def recherche_saison():
	""" Fonction explicite """
	print('Nous sommes le', time.strftime('%d/%m/%Y', time.localtime()))
	global Saison
	if 0 < int(time.strftime('%m', time.localtime())) <= 3 :
		if (int(time.strftime('%m', time.localtime())) == 3) and (int(time.strftime('%d', time.localtime())) < 20):
			print('C\'est la fin de l\'hiver. Les arbres sont taillés et les troups dans les haies comblés par de nouveaux plants. \n Il faut surveiller la floraison des saules ou des forsythias, c\'est qu\'il fait 6°C et que le potager peut commencer à se remplir')
			Saison = 'Hiver3'
		elif (int(time.strftime('%m', time.localtime())) == 3) and (int(time.strftime('%d', time.localtime())) >= 20):
			print('Voila le printemps, les narcices fleurissent-ils ? ;)')
			Saison = 'Printemps1'
		else:
			print('C\'est l\'hiver. Les arbres sont taillés et les troups dans les haies comblés par de nouveaux plants. \n Il faut surveiller la floraison des saules ou des forsythias, c\'est qu\'il fait 6°C et que le potager peut commencer à se remplir')
			Saison = 'Hiver2'
	elif 3 < int(time.strftime('%m', time.localtime())) <= 6 :
		if (int(time.strftime('%m', time.localtime())) == 6) and (int(time.strftime('%d', time.localtime())) < 20):
			print('C\'est la fin du printemps, prêt pour les plantations ?')
			Saison = 'Printemps3'
		elif (int(time.strftime('%m', time.localtime())) == 6) and (int(time.strftime('%d', time.localtime())) >= 20):
			print('Voila l\'été, il va falloir arroser.')
			Saison = 'Été1'
		else:
			print('C\'est le printemps. Les narcices, les lilas, les cerisiers et les rosiers vont fleurir, garder les à l\'œil.')
			Saison = 'Printemps2'
	elif 6 < int(time.strftime('%m', time.localtime())) <= 9 :
		if (int(time.strftime('%m', time.localtime())) == 9) and (int(time.strftime('%d', time.localtime())) < 23):
			print('C\'est la fin de l\'été. L\'engrais vert est-il en place ?')
			Saison = 'Été3'
		elif (int(time.strftime('%m', time.localtime())) == 9) and (int(time.strftime('%d', time.localtime())) >= 23):
			print('Voila l\'automne, les feuilles vont tomber')
			Saison = 'Automne1'
		else:
			print('C\'est l\'été, en espérant que chacun fasse le plein pour les petits plats d\'hiver.')
			Saison = 'Été2'
	elif 9 < int(time.strftime('%m', time.localtime())) <= 12 :
		if (int(time.strftime('%m', time.localtime())) == 9) and (int(time.strftime('%d', time.localtime())) < 21):
			print('C\'est la fin de l\'automne. Tout ce qui doit l\'être est à l\'abris du gel ?')
			Saison = 'Automne3'
		elif (int(time.strftime('%m', time.localtime())) == 9) and (int(time.strftime('%d', time.localtime())) >= 21):
			print('Voila l\'hiver, va-t-il neiger cette année ?')
			Saison = 'Hiver1'
		else:
			print('Prêt à recommencer au printemps ?')
			Saison = 'Automne2'


def proposer_activite():
	global Asemer, Aplanter
	Asemer, Aplanter = [], []
	for n in list(Plantes.keys()):
		SmDeb, SmFin = Plantes[n][3], Plantes[n][4]		#Récupérer dates Semis dans dictionnaire Plantes
		if Saisons.index(SmDeb) == Saisons.index(SmFin):
			pass
		elif Saisons.index(SmDeb) < Saisons.index(SmFin):
			track = Saisons.index(SmDeb)
			while track <= Saisons.index(SmFin):
				if Saisons[track] == Saison :
					print('Vous pouvez semer des ', n, 's')
					Asemer.append(n)
				track += 1
		elif Saisons.index(SmDeb) > Saisons.index(SmFin):
			track = Saisons.index(SmDeb)
			while track <= 12:
				if Saisons[track] == Saison :
					print('Vous pouvez semer des ', n, 's')	
					Asemer.append(n)		
				track += 1
			track = 0
			while track <= Saisons.index(SmFin):
				if Saisons[track] == Saison :
					print('Vous pouvez semer des ', n, 's')	
					Asemer.append(n)		
				track += 1
	for n in list(Plantes.keys()):
		PltDeb, PltFin = Plantes[n][5], Plantes[n][6]		#Récupérer dates Plantations dans dictionnaire Plantes
		if Saisons.index(PltDeb) == Saisons.index(PltFin):
			pass
		elif Saisons.index(PltDeb) < Saisons.index(PltFin):
			track = Saisons.index(PltDeb)
			while track <= Saisons.index(PltFin):
				if Saisons[track] == Saison :
					print('Vous pouvez planter des ', n, 's')
					Aplanter.append(n)
				track += 1
		elif Saisons.index(PltDeb) > Saisons.index(PltFin):
			track = Saisons.index(PltDeb)
			while track <= 12:
				if Saisons[track] == Saison :
					print('Vous pouvez planter des ', n, 's')
					Aplanter.append(n)			
				track += 1
			track = 0
			while track <= Saisons.index(PltFin):
				if Saisons[track] == Saison :
					print('Vous pouvez planter des ', n, 's')	
					Aplanter.append(n)		
				track += 1

		


def choisir_plante():
	global Objet
	Objet = 0
	while (Objet in Plantes.keys()) == False :
		print("Saisir le nom d'une plante à semer ou à planter parmi celles-ci : ", Asemer, Aplanter)
		Objet = input()
		if (Objet in Plantes.keys()) == False:
			print('Saisie hors liste, recommencer : ')
	print('L(\')e ', Objet, ", est un(e) ", Plantes[Objet][0], "à,", Plantes[Objet][1], "dont vous récolterez (peut-être) la(les) ", Plantes[Objet][2], '(s)') 



def chercher_parcelle():
	n=0
	ListTemp = []	#(Parcelles où il ne faut pas cultiver)
	while n < len(list(Historiques.values())):
		if list(Historiques.values())[n][0] in list(Plantes.keys()):	#
			if (Plantes[list(Historiques.values())[n][0]][0]) == Plantes[Objet][0]:	#Comparer la famille plantée sur une parcelle avec la famille de la plante à travailler
				ListTemp.append((list(Historiques.items())[n][0][0]))	#Ajout dans la liste, des parcelles ayant eu des cultures de la même famille 
		if list(Historiques.values())[n][1] in list(Plantes.keys()):	#
			if (Plantes[list(Historiques.values())[n][0]][0]) == Plantes[Objet][0]:	#Comparer la famille plantée sur une parcelle avec la famille de la plante à travailler
				ListTemp.append((list(Historiques.items())[n][0][0]))
		n += 1
	n=0
	ListTempFinal = []
	while n < len(Historiques.keys()) :	#Sélectionner les parcelles n'ayant pas été recouverte par la famille à travailler. 
		if (list(Historiques.keys())[n][0] not in list(ListTemp)) and (list(Historiques.keys())[n][0] not in list(ListTempFinal)): #Évite les doublons
			ListTempFinal.append(list(Historiques.keys())[n][0])
		n += 1
	if ListTemp == ['Parcelle', (-1000, -1000)] :
		creer_parcelle()
	else :
		print('Vous pouvez planter ou semer', Objet, 'sur les (la) parcelles :', list(ListTempFinal))




def creer_parcelle():
	global Reponse
	Reponse = '?'
	while (Reponse in OuiNon) == False :
		print('Aucune parcelle n\'est disponible pour accueillir les ', Objet, 's. Voulez-vous en travailler une nouvelle ? Oui, Non')
		Reponse = input()
		if (Reponse in OuiNon) == False :
			print('Saisir oui ou non')
		elif (Reponse in Non) == True :
			print('Voulez-vous quand même planter quelques chose ?')
			Reponse = input()
			if (Reponse in OuiNon) == False :
				print('Saisir oui ou non')
			elif (Reponse in Non) == True :
				print('B\'bye')
			elif (Reponse in Oui) == True :
				lancer()
		elif (Reponse in Oui) == True :
			print('Quels sont les coordonnées de la parcelle sur votre terrain ? Saisir x et y')
			x = int(input('Coordonnée x ? '))
			y = int(input('Coordonnée y ? '))
			while (type(x) == int and type(y) == int) == False :
				print('les coordonnées doivent être des numéros')
				x = int(input('Coordonnée x ? '))
				y = int(input('Coordonnée y ? '))
				print(type(x),type(y))
			else :
				Parcelles = ((x,y),int(time.strftime('%Y', time.localtime())))
				Historiques[Parcelles] = (Objet,'NA')
				with open('Hist', 'wb') as fichier:
					pick1 = pickle.Pickler(fichier)
					pick1.dump(Historiques)






def lancer():
	os.chdir('/home/pam/Bureau/Jardin/ProgrammePy')
	recherche_saison()
	proposer_activite()
	choisir_plante()
	chercher_parcelle()

lancer()

