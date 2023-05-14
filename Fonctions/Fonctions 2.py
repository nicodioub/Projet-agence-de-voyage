# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:45:32 2023

@author: 34679246
"""

# Import les fonctions
from mysql.connector import connect

cli_id=int
des_id=int
cli_naissance=str
#Connected sur Mysql
bdd=connect(host="localhost",user="root",
            password="root",database="agence_de_voyage")

#definir les fonctions de saisir client
def f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer):
    cursor=bdd.cursor()
    sql="INSERT INTO client(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.execute(sql,(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer))
    bdd.commit()

#definir les fonction de suppimer    
def f_suppclient(cli_id):
    cursor=bdd.cursor()
    sql="DELETE FROM client WHERE cli_id="+str(cli_id)
    cursor.execute(sql)
    bdd.commit()    
#definir un foction de modification
def f_modclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer):
    f_suppclient(cli_id)
    f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer)


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

#finir? NON!
#fonction de connection:
def f_connect():
    while True:
        print("BIENVEUNE au système de l'argence du voyage!")
        print("Pour nouveau client tapper 1,")
        i=int(input("Pour registration d'ancient client tapper 2:"))
        
     #nouveau client   
        if i==1:
            cli_id=input("saisir ton id en numero:")
            cli_nom=input("saisir ton nom")
            cli_prenom=input("saisir ton prenom")
            
            cli_sex=input("saisir ton sex(H ou F): ")
         #   cli_naissance=("choisir ton date de naissance:")
            cli_depart=None
            cli_rentrer=None
            cli_password=input("saisir ton password")
            f_ajouteclient(cli_id,cli_nom,cli_prenom,cli_naissance,cli_sex,cli_depart,cli_rentrer)
            cursor=bdd.cursor()
            sql="INSERT INTO client(cli_password)VALUES(%s)"
            cursor.execute(sql,(cli_password))
            if cli_sex=="H":
                print("M."+cli_nom+"Bienveune!Vous peuvez maintenant choisir ton destination!")
            elif cli_sex=="F":
                print("Mme."+cli_nom+"Bienveune!Vous peuvez maintenant choisir ton destination!")
                
            break
    #ancient client
        elif i==2:
            cli_nom=input("saisir ton nom")
            cli_prenom=input("saisir ton prenom")
            cli_password=input("SASIR TON PASSWORD:")
            
    #trouver password  dans le bdd      
            cursor=bdd.cursor()
            sql="SELECT cli_password FROM client WHERE cli_nom="+cli_nom+" AND cli_prenom="+cli_prenom
            cursor.execute(sql)
            resultat=cursor.fetchall()
    #resultat :
            if resultat==None:
                print("E1_client_not_found")
            elif resultat==cli_password:
                print("Bienvenue,"+cli_prenom+" "+cli_nom)
                
            #MODE DE ADMIN?
                if cli_nom=="admin" and cli_prenom=="admin":
                    
                    break
            else:
                print("PASSWORD INCORRECT")
                
#programme principale
f_connect()
                