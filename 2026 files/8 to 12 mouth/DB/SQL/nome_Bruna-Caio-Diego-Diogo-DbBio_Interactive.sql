Create DATABASE BioInteractive_db;

USE  BioInteractive_db;

CREATE TABLE User (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(50),
    Password VARCHAR(50)
);
 
CREATE TABLE image_info (
    ImageData BLOB,
    UploadDate DATE,
    UserID INT
);
 
CREATE TABLE location_info_image (
    Latitude FLOAT,
    Longitude FLOAT,
    UserID INT
);
 
CREATE TABLE species_info (
    SpeciesName VARCHAR(50),
    CommonName VARCHAR(50),
    Family VARCHAR(50),
    SpeciesOrder VARCHAR(50),
    Class VARCHAR(50),
    UserID INT
);