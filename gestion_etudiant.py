
#j'ai juste ajouter ce commentaire histoire de faire un nouveau commit
# Définir la structure de données pour un étudiant
class Etudiant:
 def __init__(self, matricule, nom, prenom, age, filiere, niveau, cotisations):
     self.matricule = matricule
     self.nom = nom
     self.prenom = prenom
     self.age = age
     self.filiere = filiere
     self.niveau = niveau
     self.cotisations = cotisations


# Fonction pour saisir les données des étudiants dans un fichier
def saisir():
     with open("etudiants.txt", "a") as file:
         matricule = input("Matricule : ")
         nom = input("Nom : ")
         prenom = input("Prenom : ")
         age = input("Age : ")
         filiere = input("Filiere : ")
         niveau = input("Niveau : ")
         cotisations = [float(input(f"Cotisation {i + 1} : ")) for i in range(5)]

         etudiant = Etudiant(matricule, nom, prenom, age, filiere, niveau, cotisations)

         file.write(f"{etudiant.matricule};{etudiant.nom};{etudiant.prenom};{etudiant.age};{etudiant.filiere};{etudiant.niveau};{';'.join(map(str, etudiant.cotisations))}\n")


# Ajouter un étudiant au fichier etudiants.txt
def ajouter():
    saisir()


# Modifier les données d'un étudiant existant dans le fichier connaissant son matricules
def modifier(matricule):
     with open("etudiants.txt", "r") as file:
        lignes = file.readlines()
     with open("etudiants.txt", "w") as file:
        for ligne in lignes:
            etudiant_data = ligne.strip().split(";")
            if etudiant_data[0] == matricule:
                saisir()
            else:
                file.write(ligne)


# Supprimer un étudiant par matricule
def supprimer(matricule):
     with open("etudiants.txt", "r") as file:
        lignes = file.readlines()
     with open("etudiants.txt", "w") as file:
         for ligne in lignes:
            etudiant_data = ligne.strip().split(";")
            if etudiant_data[0] != matricule:
                file.write(ligne)


# Afficher la liste des étudiants et le montant total de leurs cotisations
def afficher_etudiants():
     with open("etudiants.txt", "r") as file:
        lignes = file.readlines()
        total_cotisations = 0
     for ligne in lignes:
         etudiant_data = ligne.strip().split(";")
         etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
        etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
         total_cotisations += sum(etudiant.cotisations)
         print(f"{etudiant.nom} {etudiant.prenom} - Total cotisations : {sum(etudiant.cotisations)}")
         print(f"Montant total des cotisations : {total_cotisations}")


# Définir la fonction solvable
def solvable():
     with open("etudiants.txt", "r") as file:
         lignes = file.readlines()
         with open("etat.txt", "w") as etat_file:
             for ligne in lignes:
                 etudiant_data = ligne.strip().split(";")
                 etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
                etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
                 total_cotisations = sum(etudiant.cotisations)
                 etat_file.write(f"{etudiant.nom} {etudiant.prenom} - Total cotisations : {total_cotisations}\n")


# Définir la fonction insolvable
def insolvable():
     with open("etudiants.txt", "r") as file:
         lignes = file.readlines()
         with open("mauvais.txt", "w") as mauvais_file:
             for ligne in lignes:
                 etudiant_data = ligne.strip().split(";")
                 etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
                etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
                 if sum(etudiant.cotisations) < 100: # Exemple d'un seuil de cotisation
                    mauvais_file.write(f"{etudiant.nom} {etudiant.prenom}\n")


# Définir la fonction statistiques
def statistiques():
     with open("etudiants.txt", "r") as file:
         lignes = file.readlines()
         total_etudiants = len(lignes)
         etudiants_insolvables = 0
     for ligne in lignes:
         etudiant_data = ligne.strip().split(";")
         etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
        etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
         if sum(etudiant.cotisations) < 100: # Exemple d'un seuil de cotisation
             etudiants_insolvables += 1
             pourcentage_insolvables = (etudiants_insolvables / total_etudiants) * 100
             return pourcentage_insolvables


# Définir la fonction supprimer étudiants non cotisants
def supprimer_non_cotisants():
     with open("etudiants.txt", "r") as file:
        lignes = file.readlines()
     with open("etudiants.txt", "w") as file:
        for ligne in lignes:
             etudiant_data = ligne.strip().split(";")
             etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
            etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
             if sum(etudiant.cotisations) > 0:
                file.write(ligne)


# Définir la fonction recherche
def recherche(matricule):
     with open("etudiants.txt", "r") as file:
        lignes = file.readlines()
     for ligne in lignes:
        etudiant_data = ligne.strip().split(";")
        if etudiant_data[0] == matricule:
             etudiant = Etudiant(etudiant_data[0], etudiant_data[1], etudiant_data[2], etudiant_data[3],
            etudiant_data[4], etudiant_data[5], map(float, etudiant_data[6:]))
             print(f"Matricule : {etudiant.matricule}")
             print(f"Nom : {etudiant.nom}")
             print(f"Prenom : {etudiant.prenom}")
             print(f"Age : {etudiant.age}")
             print(f"Filiere : {etudiant.filiere}")
             print(f"Niveau : {etudiant.niveau}")
             print(f"Cotisations : {', '.join(map(str, etudiant.cotisations))}")


# Programme principal
while True:
 print("\nMenu :")
 print("1. Ajouter un étudiant")
 print("2. Modifier les données d'un étudiant")
 print("3. Supprimer un étudiant")
 print("4. Afficher la liste des étudiants et le montant total de leurs cotisations")
 print("5. Créer le fichier etat.txt et afficher les étudiants solvables")
 print("6. Créer le fichier mauvais.txt et afficher les étudiants insolvables")
 print("7. Calculer le pourcentage d'étudiants n'ayant pas fait toutes les cotisations")
 print("8. Supprimer les étudiants non cotisants")
 print("9. Rechercher un étudiant par matricule")
 print("0. Quitter")
 choix = input("Choisissez une option : ")
 if choix == "1":
    ajouter()
 elif choix == "2":
    matricule = input("Matricule de l'étudiant à modifier : ")
    modifier(matricule)
 elif choix =="3":
    matricule = input("Matricule de l'étudiant à supprimer : ")
    supprimer(matricule)
 elif choix == "4":
    afficher_etudiants()
 elif choix == "5":
    solvable()
 elif choix == "6":
    insolvable()
 elif choix == "7":
    pourcentage = statistiques()
    print(f"Pourcentage d'étudiants insolvables : {pourcentage}%")
 elif choix == "8":
    supprimer_non_cotisants()
 elif choix == "9":
    matricule = input("Matricule de l'étudiant à rechercher : ")
    recherche(matricule)
 elif choix == "0":
    break
 else:
    print("Option invalide. Réessayez.")