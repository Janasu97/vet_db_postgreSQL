import psycopg2

def dbDataAdd():
    #Connect to the database
    try:
        conn = psycopg2.connect(host="localhost", dbname="vet_clinic", user="postgres", password="admin", port=5432)
    except:
        return "No data connection to the vet_clinic database. Program terminated"

    conn.autocommit = True
    cur = conn.cursor()

    # Insert data into the animals' table
    sql_db_add = """
    INSERT INTO animals (name, date_of_birth, escape_attempts, neutered, weight_kg)
    VALUES ('Agumon', '2020-02-03', 0, true, 10.23),
           ('Gabumon', '2018-11-15', 2, true, 8),
           ('Pikachu', '2021-01-07', 1, false, 15.04),
           ('Devimon', '2017-05-12', 5, true, 11);
    """
    cur.execute(sql_db_add)

    sql_db_add = """
    INSERT INTO animals (name, date_of_birth, escape_attempts, neutered, weight_kg)
    VALUES
      ('Charmander', '2020-02-08', 0, FALSE, -11),
      ('Plantmon', '2021-11-15', 2, TRUE, -5.7),
      ('Squirtle', '1993-04-02', 3, FALSE, -12.13),
      ('Angemon', '2005-06-12', 1, TRUE, -45),
      ('Boarmon', '2005-06-07', 7, TRUE, 20.4),
      ('Blossom', '1998-10-13', 3, TRUE, 17),
      ('Ditto', '2022-05-14', 4, TRUE, 22);
    """
    cur.execute(sql_db_add)

    # Insert data into the owners' table
    sql_db_add = """
    INSERT INTO owners (full_name, age) VALUES
      ('Sam Smith', 34),
      ('Jennifer Orwell', 19),
      ('Bob', 45),
      ('Melody Pond', 77),
      ('Dean Winchester', 14),
      ('Jodie Whittaker', 38);
    """
    cur.execute(sql_db_add)


    # Insert data into the species' table
    sql_db_add = """
    INSERT INTO species (name) VALUES
      ('Pokemon'),
      ('Digimon');
    """
    cur.execute(sql_db_add)


    # Update the animals table foreign keys
    sql_db_update = """
    UPDATE animals SET species_id = (
      CASE
        WHEN name LIKE '%mon' THEN (SELECT id FROM species WHERE name = 'Digimon')
        ELSE (SELECT id FROM species WHERE name = 'Pokemon')
      END
    );
    """
    cur.execute(sql_db_update)


    sql_db_update = """
    UPDATE animals SET owner_id = (
      CASE
        WHEN name = 'Agumon' THEN (SELECT id FROM owners WHERE full_name = 'Sam Smith')
        WHEN name IN ('Gabumon', 'Pikachu') THEN (SELECT id FROM owners WHERE full_name = 'Jennifer Orwell')
        WHEN name IN ('Devimon', 'Plantmon') THEN (SELECT id FROM owners WHERE full_name = 'Bob')
        WHEN name IN ('Charmander', 'Squirtle', 'Blossom') THEN (SELECT id FROM owners WHERE full_name = 'Melody Pond')
        WHEN name IN ('Angemon', 'Boarmon') THEN (SELECT id FROM owners WHERE full_name = 'Dean Winchester')
      END
    );
    """
    cur.execute(sql_db_update)


    # Insert data into the vets' table
    sql_db_add = """
    INSERT INTO vets (name, age, date_of_graduation) VALUES
      ('Vet William Tatcher', 45, '2000-04-23'),
      ('Vet Maisy Smith', 26, '2019-01-17'),
      ('Vet Stephanie Mendez', 64, '1981-05-04'),
      ('Vet Jack Harkness', 38, '2008-06-08');
    """
    cur.execute(sql_db_add)


    # Insert the data for specialties:
    sql_db_add = """
    INSERT INTO specializations (vet_id, species_id)
    VALUES ((SELECT id FROM vets WHERE name = 'Vet William Tatcher'), (SELECT id FROM species WHERE name = 'Pokemon'));
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO specializations (vet_id, species_id)
    VALUES ((SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), (SELECT id FROM species WHERE name = 'Digimon')),
           ((SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), (SELECT id FROM species WHERE name = 'Pokemon'));
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO specializations (vet_id, species_id)
    VALUES ((SELECT id FROM vets WHERE name = 'Vet Jack Harkness'), (SELECT id FROM species WHERE name = 'Digimon'));
    """
    cur.execute(sql_db_add)


    # Insert the data for visits:
    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Agumon'),
    (SELECT id FROM vets WHERE name = 'Vet William Tatcher'), '2020-05-24');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Agumon'),
    (SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), '2020-07-22');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Gabumon'),
    (SELECT id FROM vets WHERE name = 'Vet Jack Harkness'), '2021-02-02');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Pikachu'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2020-01-05'),
           ((SELECT id FROM animals WHERE name = 'Pikachu'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2020-03-08'),
           ((SELECT id FROM animals WHERE name = 'Pikachu'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2020-05-14');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Devimon'), (SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), '2021-05-04');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Charmander'), (SELECT id FROM vets WHERE name = 'Vet Jack Harkness'), '2021-02-24');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Plantmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2019-12-21'),
           ((SELECT id FROM animals WHERE name = 'Plantmon'), (SELECT id FROM vets WHERE name = 'Vet William Tatcher'), '2020-08-10'),
           ((SELECT id FROM animals WHERE name = 'Plantmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2021-04-07');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Squirtle'), (SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), '2019-09-29');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Angemon'), (SELECT id FROM vets WHERE name = 'Vet Jack Harkness'), '2020-10-03'),
           ((SELECT id FROM animals WHERE name = 'Angemon'), (SELECT id FROM vets WHERE name = 'Vet Jack Harkness'), '2020-11-04');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Boarmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2019-01-24'),
           ((SELECT id FROM animals WHERE name = 'Boarmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2019-05-15'),
           ((SELECT id FROM animals WHERE name = 'Boarmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2020-02-27'),
           ((SELECT id FROM animals WHERE name = 'Boarmon'), (SELECT id FROM vets WHERE name = 'Vet Maisy Smith'), '2020-08-03');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Blossom'), (SELECT id FROM vets WHERE name = 'Vet Stephanie Mendez'), '2020-05-24');
    """
    cur.execute(sql_db_add)


    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date)
    VALUES ((SELECT id FROM animals WHERE name = 'Blossom'), (SELECT id FROM vets WHERE name = 'Vet William Tatcher'), '2021-01-11');
    """
    cur.execute(sql_db_add)


    # # This will add visits
    sql_db_add = """
    INSERT INTO visits (animal_id, vet_id, visit_date) SELECT * FROM (SELECT id FROM animals) animal_ids,
    (SELECT id FROM vets) vets_ids, generate_series('2000-01-01 00:00'::timestamp, '2024-01-01', '120 hours') visit_timestamp;
    """
    cur.execute(sql_db_add)


    # This will add 25.000 owners with full_name = 'Owner <X>' and email = 'owner_<X>@email.com' (~1min approx.)
    sql_db_add = """
    insert into owners (full_name, email) select 'Owner ' || generate_series(1,25000), 'owner_' || generate_series(1,25000) || '@mail.com';
    """
    cur.execute(sql_db_add)


    cur.close()
    conn.close()
    return "Data saved successfully"




