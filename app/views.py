#depuis le dossier app, importer app contenu dans le fichier __init__.py
from app import app
from flask import render_template,request
from docxtpl import DocxTemplate
import zipfile



dico_motifs={"courses":"Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionnelle, des achats de première nécessité dans des établissements dont les 3 activités demeurent autorisées, le retrait de commande et les livraisons à domicile.",
            "medical":"Consultations, examens et soins ne pouvant être ni assurés à distance ni différés et l’achat de médicaments",
            "sport":"Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.",
            "justice":"Convocation judiciaire ou administrative et pour se rendre dans un service public"
            }

@app.route('/')
def afficher_home():
    return render_template("public/home_public.html")

@app.route('/formulaire')
def afficher_formulaire():
    return render_template("public/formulaire.html")

@app.route("/creation_attestation", methods=['POST'])
def creation_attestation():
    return render_template("public/creation_attestation.html")