DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS treatment;

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
    email_address VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type_of_animal VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    photo VARCHAR(255),
    checked_in_time VARCHAR(255),
    checked_out_time VARCHAR(255)
);

CREATE TABLE notes(
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    comment TEXT,
    follow_up BOOLEAN
);

CREATE TABLE treatment(
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    price MONEY,
    duration INT
);