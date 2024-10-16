--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Agence;

CREATE DATABASE Agence;

USE Agence;

--
-- Création des tables :
--

CREATE TABLE Destination (
    des_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    des_ville VARCHAR(30) NOT NULL,
    des_hotel VARCHAR(50) NOT NULL,
    des_prix INT UNSIGNED NOT NULL,
    PRIMARY KEY (des_id)
)
ENGINE=INNODB;

CREATE TABLE Activite (
    act_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    act_sortie VARCHAR(30) NOT NULL,
    act_prix INT UNSIGNED NOT NULL,
    PRIMARY KEY (act_id)
)
ENGINE=INNODB;


CREATE TABLE Transport (
    tra_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    tra_type VARCHAR(50) NOT NULL,
    tra_prix INT UNSIGNED NOT NULL,
    PRIMARY KEY (tra_id)
)
ENGINE=INNODB;

CREATE TABLE Facturation (
    fac_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    fac_transport VARCHAR(50) NOT NULL,
    fac_destination VARCHAR(50) NOT NULL,
    fac_activite VARCHAR(50) NOT NULL,
    PRIMARY KEY (fac_id)
)
ENGINE=INNODB;


CREATE TABLE Clients (
    cli_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cli_nom VARCHAR(30) NOT NULL,
    cli_prenom VARCHAR(30) NOT NULL,
    cli_naissance DATE,
    cli_sexe CHAR(1),
    cli_depart DATE,
    cli_arrivee DATE,
    cli_facture INT UNSIGNED,
    cli_transport INT UNSIGNED,
    cli_password VARCHAR(30) NOT NULL,
    PRIMARY KEY (cli_id),
    CONSTRAINT fk_cli_facture FOREIGN KEY (cli_facture) REFERENCES Facturation(fac_id) ON DELETE SET NULL,
    CONSTRAINT fk_cli_transport FOREIGN KEY (cli_transport) REFERENCES Transport(tra_id)
    )
ENGINE=INNODB;

CREATE TABLE Va_faire (
    va_client INT UNSIGNED NOT NULL,
    va_activite INT UNSIGNED NOT NULL,
    CONSTRAINT pk_va_faire PRIMARY KEY(va_client,va_activite),
    CONSTRAINT fk_va_client FOREIGN KEY (va_client) REFERENCES Clients(cli_id),
    CONSTRAINT fk_va_activite FOREIGN KEY (va_activite) REFERENCES Activite(act_id)
)
ENGINE=INNODB;

CREATE TABLE Va_a (
    va_a_client INT UNSIGNED NOT NULL,
    va_destination INT UNSIGNED NOT NULL,
    CONSTRAINT pk_va_a PRIMARY KEY(va_a_client, va_destination),
    CONSTRAINT fk_va_a_client FOREIGN KEY (va_a_client) REFERENCES Clients(cli_id),
    CONSTRAINT fk_va_destination FOREIGN KEY (va_destination) REFERENCES Destination(des_id)
)
ENGINE=INNODB;

--
-- Insertion de valeurs dans les tables :
--

INSERT INTO Clients
VALUES  (1, 'Billaud', 'Anick', '1905-05-16','F','2022-02-16','2022-02-27',NULL,NULL,'Fleur'),
    (2, 'Moreau', 'Louis', '1913-11-05','F', '2003-05-17', '2003-06-16',NULL,NULL,'Hzedwf3f5'),
    (3, 'Bouvier', 'Charles', '1921-11-03','H', '2005-02-23','2005-03-12',NULL,NULL,'Jee1215'),
    (4, 'DEPARDIEU', 'Guillaume', '1971-04-07','H', '2016-11-02','2016-12-24',NULL,NULL,'Guillaume*');

INSERT INTO Activite
VALUES  (1, 'Musée',30),
    (2, 'Festival',170),
    (3, 'Excursion',30),
    (4,'City tour',15),
    (5,'sortie culinaire',500);

INSERT INTO Facturation
VALUES (1,'255','255','255');



INSERT INTO Destination
VALUES  (1, "New York City", "The Plaza", 2000),
    (2, "Paris", "Le Meurice", 1500),
    (3, "Tokyo", "Park Hyatt", 1800),
    (4, "Dubai", "Burj Al Arab", 3000),
    (5, "London", "The Ritz London", 1700),
    (6, "Los Angeles", "The Beverly Hills Hotel", 1900),
    (7, "Hong Kong", "The Peninsula", 2100),
    (8, "Singapore", "Marina Bay Sands", 2500),
    (9, "Sydney", "The Langham", 1600),
    (10, "Rome", "The St. Regis Rome", 1400),
    (11, "Barcelona", "Mandarin Oriental", 1200),
    (12, "Miami", "The Faena Hotel Miami Beach", 2200),
    (13, "Shanghai", "Fairmont Peace Hotel", 2000),
    (14, "Moscow", "The Ritz-Carlton Moscow", 1700),
    (15, "Toronto", "The Ritz-Carlton Toronto", 1800),
    (16, "Berlin", "The Ritz-Carlton Berlin", 1600),
    (17, "Vienna", "The Ritz-Carlton Vienna", 1500),
    (18, "Melbourne", "The Langham Melbourne", 1400),
    (19, "Mumbai", "The Oberoi Mumbai", 1900),
    (20, "Zurich", "Baur au Lac", 2200),
    (21, "San Francisco", "The St. Regis San Francisco", 2300),
    (22, "Buenos Aires", "Alvear Palace Hotel", 2000),
    (23, "Amsterdam", "Hotel De L'Europe Amsterdam", 1700),
    (24, "Seoul", "The Shilla Seoul", 2100),
    (25, "Munich", "The Charles Hotel", 1800),
    (26, "Monte Carlo", "Hotel de Paris Monte-Carlo", 2800),
    (27, "Cape Town", "Belmond Mount Nelson Hotel", 1600),
    (28, "Madrid", "The Westin Palace Madrid", 1500),
    (29, "Athens", "Hotel Grande Bretagne, a Luxury Collection Hotel", 1900),
    (30, "Abidjan", "Le Noom", 2500);

INSERT INTO Transport
VALUES  (1, 'Avion', 1000),
    (2, 'Bateau',700),
    (3, 'Voiture',150),
    (4, 'Moto',75);


INSERT INTO Va_faire
VALUES  (1, 1),
    (1, 3),
    (2, 2),
    (2, 4),
    (2, 5),
    (3, 4),
    (4, 1),
    (4, 3),
    (4, 5);

INSERT INTO Va_a
VALUES  (1, 2),
    (2, 21),
    (3, 14),
    (4, 18);

--
-- Requêtes :
--

SELECT *
From Clients

