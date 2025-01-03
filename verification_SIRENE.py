# Bibliothèques à importer
import requests
from datetime import date
import pandas as pd
import time

st = time.time() # Début du chronomètre
print("Programme démarré")

# Fonction qui convertit un SIRET en SIREN
def convertSiretToSiren(siret):
    siret.replace(" ","") # On supprime les espaces
    if(len(siret)<9): # Si le SIRET est inférieur à 9 caractères (taille du SIREN), on ne le prend pas en compte
        siren = ""
    else:
        siren = siret[0:9] # On ne garde que les 9 premiers chiffres du SIRET
    return siren

# On récupère la date du jour pour avoir les derniers éléments à jour de l'API
today = date.today()

# Entêtes nécessaires pour récupérer les éléments de l'API
headers = {
    'X-INSEE-Api-Key-Integration': 'XXXXXX',
    'Accept': 'application/json',
}

# Paramètres (optionnels) pour récupérer les éléments de l'API
params = {
    "date": today,
}

# On récupère la liste des opérateurs
data = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/b0f62183-cd0c-498d-8153-aa1594e5e8d9", sep=";",encoding="latin-1")
numberLines = data.shape[0] # Nombre de lignes à analyser
increment = 0 # Variable incrémentale pour savoir où l'on en est de l'analyse du fichier
dataInsee = [] # Table pour récupérer les éléments de l'API

# On parcourt la liste des opérateurs
for num in range(0, len(data)):
    sirenFromSiret = convertSiretToSiren(str(data["SIRET_ACTEUR"][num]))
    increment = increment + 1
    if(sirenFromSiret != ""):
        url = "https://api.insee.fr/api-sirene/3.11/siren/"+sirenFromSiret # URL de l'API propre à chaque opérateur
        response = requests.get(url, params=params, headers=headers) # Requête pour récupérer de manière unitaire les éléments
        # On convertit la réponse obtenue au format json
        jsonResponse = response.json()
        # On récupère les éléments nécessaires
        try: # En cas d'erreur, pour éviter que le programme ne s'arrête
            siren = jsonResponse["uniteLegale"]["siren"] # Siren
            statutRequete = jsonResponse["header"]["statut"] # Statut de la requête
            dateCreation = jsonResponse["uniteLegale"]["dateCreationUniteLegale"] # Date de création INSEE
            nomEntite = jsonResponse["uniteLegale"]["periodesUniteLegale"][0]["denominationUniteLegale"] # Nom
            etatAdministratif = jsonResponse["uniteLegale"]["periodesUniteLegale"][0]["etatAdministratifUniteLegale"] # Etat administratif (A : administrativement active ; C : administrativement cessée)
            dateDerniereModification = jsonResponse["uniteLegale"]["periodesUniteLegale"][0]["dateDebut"] # Date de dernière modification
            dataInsee.append([data["IDENTITE_OPERATEUR"][num],data["CODE_OPERATEUR"][num],data["SIRET_ACTEUR"][num],data["RCS_ACTEUR"][num],data["ADRESSE_COMPLETE_ACTEUR"][num],data["ATTRIB_RESS_NUM"][num],data["DATE_DECLARATION_OPERATEUR"][num], sirenFromSiret, statutRequete, dateCreation, nomEntite, etatAdministratif, dateDerniereModification])
            print(str(increment) + " / " + str(numberLines)) # On affiche la progression
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message) # On affiche les raisons de l'erreur
        time.sleep(2) # Pour effectuer une requête toutes les 2 secondes (et respecter la durée minimale imposée par l'INSEE de 30 requêtes par minute)

dataframe = pd.DataFrame(dataInsee)
dataframe.to_csv(r"./MAJOPE_Sirene.csv", header=["IDENTITE_OPERATEUR","CODE_OPERATEUR","SIRET_ACTEUR","RCS_ACTEUR","ADRESSE_COMPLETE_ACTEUR","ATTRIB_RESS_NUM","DATE_DECLARATION_OPERATEUR", "SIREN_INSEE","STATUT_REQUETE_API", "DATE_CREATION_INSEE", "NOM_ENTITE_INSEE", "ETAT_ADMINISTRATIF_INSEE", "DATE_DERNIERE_MODIFICATION_INSEE"], index=False, sep=";",encoding="latin-1")

et = time.time() # Fin du chronomètre
elapsed_time = time.strftime("%H:%M:%S", time.gmtime(et - st)) # Durée d'exécution du programme
print("Programme exécuté en : ", elapsed_time, ".")
