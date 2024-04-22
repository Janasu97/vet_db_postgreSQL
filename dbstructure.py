import psycopg2

def buildDB():
    #Connect to the database
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="admin", port=5432)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""CREATE database vet_clinic;""")
        conn.close()
    except:
        pass

    try:
        conn = psycopg2.connect(host="localhost", dbname="vet_clinic", user="postgres", password="admin", port=5432)
    except:
        return "No data connection to the vet_clinic database. Program terminated"

    conn.autocommit = True
    cur = conn.cursor()

    #Create animals table
    sql_create_animals = """
      CREATE TABLE IF NOT EXISTS animals (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100),
      date_of_birth DATE,
      escape_attempts INTEGER,
      neutered BOOLEAN,
      weight_kg DECIMAL);
    """
    cur.execute(sql_create_animals)


    # Modify the animals' table to add species column.
    sql_alter_table = """
    ALTER TABLE animals
    ADD COLUMN species VARCHAR(100);
    """
    cur.execute(sql_alter_table)


    # Create the owners table
    sql_create_owners = """
      CREATE TABLE IF NOT EXISTS owners (
      id SERIAL PRIMARY KEY,
      full_name VARCHAR(100),
      age INTEGER);
    """
    cur.execute(sql_create_owners)

    
    # Create the species table
    sql_create_species = """
      CREATE TABLE IF NOT EXISTS species (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100));
    """
    cur.execute(sql_create_species)

    
    # Modify the animals table
    sql_alter_table = """
        ALTER TABLE animals
        DROP COLUMN species;
        """
    cur.execute(sql_alter_table)

    #Modify the animals table
    sql_alter_table = """
        ALTER TABLE animals
        ADD COLUMN species_id INTEGER REFERENCES species(id),
        ADD COLUMN owner_id INTEGER REFERENCES owners(id);
        """
    cur.execute(sql_alter_table)
    
    
    # Create the vets table
    sql_create_vets = """
      CREATE TABLE IF NOT EXISTS vets (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100),
      age INTEGER,
      date_of_graduation DATE);
    """
    cur.execute(sql_create_vets)

    
    # Create the specializations join table
    sql_create_specializations = """
      CREATE TABLE IF NOT EXISTS specializations (
      vet_id INTEGER REFERENCES vets(id),
      species_id INTEGER REFERENCES species(id),
      PRIMARY KEY (vet_id, species_id));
    """
    cur.execute(sql_create_specializations)

    
    # Create the visits join table
    sql_create_visits= """
      CREATE TABLE IF NOT EXISTS visits (
      animal_id INTEGER REFERENCES animals(id),
      vet_id INTEGER REFERENCES vets(id),
      visit_date DATE,
      PRIMARY KEY (animal_id, vet_id, visit_date));
    """
    cur.execute(sql_create_visits)

    
    # Add an email column to your owners table
    sql_alter_table = """
    ALTER TABLE owners ADD COLUMN email VARCHAR(120);
    """
    cur.execute(sql_alter_table)
    
    
    # Set index on animal_id
    sql_add_idx = """
    CREATE INDEX ON visits (animal_id);
    """
    cur.execute(sql_add_idx)

    
    # Create index on vet_id
    sql_add_idx = """
    CREATE INDEX vet_id_index ON visits (vet_id);
    """
    cur.execute(sql_add_idx)

    
    # Set index on email
    sql_add_idx = """
    CREATE INDEX email_index ON owners (email);
    """
    cur.execute(sql_add_idx)


    # Close the database after all of the operations
    cur.close()
    conn.close()
    return "database created successfully"

