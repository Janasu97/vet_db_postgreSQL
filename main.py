from dbstructure import buildDB
from dataAdd import dbDataAdd
import psycopg2


def getData(sql_query):
    #Select and print the records matching selection properties

    #Connect to the database
    try:
        conn = psycopg2.connect(host="localhost", dbname="vet_clinic", user="postgres", password="admin", port=5432)
    except:
        return "No data connection to the vet_clinic database. Program terminated"

    conn.autocommit = True
    cur = conn.cursor()


    # What specialty should Maisy Smith consider getting? Look for the species she visits the most.
    cur.execute(sql_query)

    for row in cur.fetchall():
        print(row)


    cur.close()
    conn.close


if __name__ == '__main__':
    if input("Do you want to create the database? Y/N").lower() == "y":
        structure_message = buildDB()
        print(structure_message)
    else:
        print("Passed on creating the database")

    if input("Do you want to add records to the database? Y/N").lower() == "y":
        db_add_message = dbDataAdd()
        print(db_add_message)
    else:
        print("Passed on adding records into the database")

    sql_query = """
        SELECT v.animal_id, a.name as animal_name, o.full_name as owner_name, v.visit_date
        from visits as v
        join animals as a on v.animal_id = a.id
        join owners as o on a.owner_id = o.id
        where o.full_name = 'Jennifer Orwell'
        AND v.vet_id = 1
        AND v.visit_date > '2023-12-01'
        ORDER BY v.visit_date
        """

    getData(sql_query)

