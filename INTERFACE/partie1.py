# Import les fonctions
import pygame
from mysql.connector import connect
pygame.init()

cli_id=int
des_id=int
cli_naissance=str
i=int()
#Connect
bdd=connect(host="localhost",user="root",
            password="root",database="agence")

#definir les fonctions de saisir client
def f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password):
    cursor=bdd.cursor()
    sql="INSERT INTO clients(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.execute(sql,(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password))
    bdd.commit()

#definir les fonction de suppimer    
def f_suppclient(cli_id):
    cursor=bdd.cursor()
    sql="DELETE FROM clients WHERE cli_id="+str(cli_id)
    cursor.execute(sql)
    bdd.commit()    
#definir un foction de modification
def f_modclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password):
    f_suppclient(cli_id)
    f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sexe,cli_depart,cli_arrivee,cli_facture,cli_transport, cli_password)


#definir les fonction de ajouter destination 
def f_ajoutedestination(des_id,des_pays,des_ville,des_hotel,des_prix):
    cursor=bdd.cursor()
    sql="INSERT INTO destination(des_id,des_pays,des_ville,des_hotel,des_prix) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(des_id,des_pays,des_ville,des_hotel,des_prix))
    bdd.commit()


#definir le fonction de suppimer
def f_suppdestination(des_id):
    cursor=bdd.cursor()
    sql="DELETE FROM destination WHERE des_id="+str(des_id)
    cursor.execute(sql)
    bdd.commit()    

def afficher_clients(WINDOW):
    cursor = bdd.cursor()
    sql = "SELECT * FROM clients"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:        
        print("ID"), row[0]
        print("Nom:", row[1])
        print("Prenom:", row[2])
        print("Date de naissance:", row[3])
        print("Sexe:", row[4])
        print("Ville de départ:", row[5])
        print("Ville d'arrivée:", row[6])
        print("Facture:", row[7])
        print("Transport:", row[8])
        print("Mot de passe:", row[9])
        print("--------------------")

    
#modifier
def f_moddestination(des_id,des_pays,des_ville,des_hotel,des_prix):
    f_suppdestination(des_id)
    f_ajoutedestination(des_id,des_pays,des_ville,des_hotel,des_prix)

    
#definir le fonction de ajouter un besoin du client:
def f_ajouteva(va_client,va_destination):
   cursor=bdd.cursor()
   sql="INSERT INTO va_a(va_client,va_destination) VALUES(%s,%s)"
   cursor.execute(sql,(va_client,va_destination))
   bdd.commit()

#definir le fonction de supprimer
def f_suppva(va_client):
    cursor=bdd.cursor()
    sql="DELETE FROM va_a WHERE va_client="+str(va_client)
    cursor.execute(sql)
    bdd.commit()
#modifier    
def f_modva(va_client,va_destination):
    f_suppva(va_client)
    f_ajouteva(va_client,va_destination)
    
#fonction ajouter les activites
def f_ajouteactivite(act_id,act_visite,act_festival,act_excursion,act_prix):
    cursor=bdd.cursor()
    sql="INSERT INTO activite(act_id,act_visite,act_festival,act_excursion,act_prix)VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(act_id,act_visite,act_festival,act_excursion,act_prix))
    bdd.commit()
    
#suppimer
def f_suppactivite(act_id):
    cursor=bdd.cursor()
    sql="DELETE FROM activite WHERE act_id="+str(act_id)
    cursor.execute(sql)
    bdd.commit()

#modifier
def f_modactivite(act_id,act_visite,act_festival,act_excursion,act_prix):
    f_suppactivite(act_id)
    f_ajouteactivite(act_id,act_visite,act_festival,act_excursion,act_prix)