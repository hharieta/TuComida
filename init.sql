-- Display session user and current database for confirmation
SELECT session_user, current_database();

-- Drop existing tables if they exist to start fresh
DROP TABLE IF EXISTS users, eatery, weekdays, schedule, eateryhours, saucers;

-- Create users table
CREATE TABLE users (
    id_user SERIAL NOT NULL,
    names VARCHAR(64) NOT NULL,
    surname VARCHAR(64) NOT NULL,
    email VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(162) NOT NULL,
    datebirth VARCHAR(32),
    PRIMARY KEY (id_user)
);

-- Create eatery table
CREATE TABLE eatery (
    id_eatery SERIAL NOT NULL,
    eatery_name VARCHAR(20) NOT NULL,
    cuisine VARCHAR(20) NOT NULL,
    url_image VARCHAR(255),  -- Assuming these columns will be added now instead of altering later
    url_maps VARCHAR(255),
    direction VARCHAR,       -- Assuming data type, adjust as needed
    phone VARCHAR(20),
    description VARCHAR,     -- Assuming data type, adjust as needed
    PRIMARY KEY (id_eatery)
);

-- Create index for eatery table
CREATE INDEX idx_eatery_name ON eatery(eatery_name);

-- Create weekdays table
CREATE TABLE weekdays(
    id_day SERIAL NOT NULL,
    day VARCHAR(10) unique not null,
    PRIMARY KEY (id_day)
);

-- Create schedule table
CREATE TABLE schedule (
    id_schedule SERIAL NOT NULL,
    id_day INT NOT NULL,
    opening TIME NOT NULL,
    closing TIME NOT NULL,
    PRIMARY KEY (id_schedule),
    CONSTRAINT fk_weekdays FOREIGN KEY (id_day) REFERENCES weekdays(id_day) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Creating an index on 'id_day' might be beneficial if there are many lookups
CREATE INDEX idx_schedule_id_day ON schedule(id_day);

-- Create eateryhours table
CREATE TABLE eateryhours (
    id_eateryhours SERIAL NOT NULL,
    id_eatery INT NOT NULL,
    id_schedule INT NOT NULL,
    PRIMARY KEY (id_eateryhours),
    CONSTRAINT fk_eatery FOREIGN KEY (id_eatery) REFERENCES eatery(id_eatery) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_schedule FOREIGN KEY (id_schedule) REFERENCES schedule(id_schedule) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Composite index for quick lookups and to ensure each eatery/schedule pair is unique
CREATE UNIQUE INDEX idx_eatery_schedule ON eateryhours(id_eatery, id_schedule);

-- Create saucers table
CREATE TABLE saucers (
    id_saucer SERIAL,
    id_eatery INT NOT NULL,
    saucer_name VARCHAR(50) NOT NULL,  -- Adjusted type based on later alteration
    price FLOAT NOT NULL,
    description TEXT,
    url_image VARCHAR(255),
    PRIMARY KEY (id_saucer),
    CONSTRAINT fk_eatery_saucers FOREIGN KEY (id_eatery) REFERENCES eatery(id_eatery) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT uq_saucer_name_per_eatery UNIQUE (saucer_name, id_eatery)
);

-- Create index for saucers table
CREATE INDEX idx_saucer_name ON saucers(saucer_name);

-- Insert data into weekdays table
INSERT INTO weekdays(day)
VALUES ('Lunes'), ('Martes'), ('Miercoles'), ('Jueves'), ('Viernes'), ('Sábado'), ('Domingo');

-- Populate schedule table with dynamic data for each day
DO $$
BEGIN
    FOR day_id IN 1..7 LOOP
        FOR hour IN 13..16 LOOP
            INSERT INTO schedule (id_day, opening, closing)
            VALUES (day_id, make_time(hour, 0, 0), make_time(hour + 7, 0, 0));
        END LOOP;
    END LOOP;
END $$;




select * from users;
select * from eatery;
select * from eateryhours;
select  * from schedule;
select * from weekdays;

-- Insert data into eatery, eateryhours, users, and saucers as per your requirement
-- Note: Ensure all insert statements are correctly formatted and reference existing IDs where foreign keys are involved

-- Insert data into eatery table (including new columns added directly in the table creation step)
-- ...

-- Insert data into eateryhours table
-- ...

-- Insert data into users table
-- ...

-- Insert data into saucers table
-- ...

-- Perform any select queries or updates as needed
-- ...

