DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    qualified_date VARCHAR(255),
    photo VARCHAR(255)
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255),
    address VARCHAR(255),
    email_address VARCHAR(255)
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type_of_animal VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id)
);