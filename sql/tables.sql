-- Author: mendrika261
-- Date: April 14, 2023
-- Description: Table creation for the project "Fihirana-FFPM"

DROP TABLE IF EXISTS tononkira;
DROP TABLE IF EXISTS hira;
DROP TABLE IF EXISTS sokajy;

CREATE TABLE sokajy (
                        id SERIAL PRIMARY KEY,
                        anarana VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE hira (
                      id SERIAL PRIMARY KEY,
                      sokajy_id SERIAL REFERENCES sokajy(id),
                      lohateny VARCHAR(100) NULL,
                      isa_andininy INT NOT NULL,
                      mpanoratra VARCHAR(120) NULL
);

CREATE TABLE tononkira (
                        id SERIAL PRIMARY KEY,
                        hira_id SERIAL REFERENCES hira(id),
                        andininy INTEGER NULL,
                        tononkira TEXT NOT NULL,
                        fiverenany BOOLEAN DEFAULT FALSE
);