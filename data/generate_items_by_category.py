import xml.etree.ElementTree as ET
import json
from collections import defaultdict

# Nom du fichier types.xml
FICHIER_TYPES = "types.xml"
EXPORT_JSON = "items_by_category.json"

def extraire_objets_par_categorie(fichier_xml):
    tree = ET.parse(fichier_xml)
    root = tree.getroot()
    items_by_category = defaultdict(list)

    for type_tag in root.findall('type'):
        name = type_tag.get('name')
        cat_tag = type_tag.find('category')
        cat = cat_tag.get('name') if cat_tag is not None else "uncategorized"
        if name:
            items_by_category[cat].append(name)

    for k in items_by_category:
        items_by_category[k].sort()

    return items_by_category

def sauvegarder_json(data, nom_fichier):
    with open(nom_fichier, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Fichier JSON créé : {nom_fichier}")

if __name__ == "__main__":
    data = extraire_objets_par_categorie(FICHIER_TYPES)
    sauvegarder_json(data, EXPORT_JSON)
