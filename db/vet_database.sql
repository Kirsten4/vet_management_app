DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    qualified_date DATE,
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

CREATE TABLE treatments(
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    price DECIMAL(8,2),
    duration INT,
    overnights INT
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
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
    follow_up BOOLEAN,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE
);

CREATE TABLE appointments(
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    treatment_id INT REFERENCES treatments(id),
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE,
    total_bill Money 
);


INSERT INTO treatments (description, price, duration, overnights) VALUES ('General health check-up', 62.50, 20, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Vaccinations', 26.80, 10, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Keyhole surgery', 1645.00, 90, 2);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Fix broken leg', 678.50, 45, 1);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Trim claws', 19.00, 15, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Flea treatment', 32.50, 5, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Blood test', 36.00, 10, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Hip replacement', 3500.00, 180, 2);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('MRI scan', 2000.00, 30, 0);
INSERT INTO treatments (description, price, duration, overnights) VALUES ('Xray', 350.00, 10, 0);