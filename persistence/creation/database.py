import sqlite3


def setup():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS "countries" (
        "id"   INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "organisations" (
        "id"   INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "location_id"  INTEGER NOT NULL,
        FOREIGN KEY("location_id") REFERENCES "locations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "events" (
        "id"   INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "type" TEXT NOT NULL CHECK("type" IN ("presentation", "workshop", "seminar")),
        "host_id"  INTEGER NOT NULL,
        FOREIGN KEY("host_id") REFERENCES "organisations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "presenters" (
        "id"   INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "organisation_id"  INTEGER NOT NULL,
        FOREIGN KEY("organisation_id") REFERENCES "organisations"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "locations" (
        "id"   INTEGER NOT NULL UNIQUE,
        "city" TEXT NOT NULL,
        "country_id"   INTEGER NOT NULL,
        FOREIGN KEY("country_id") REFERENCES "countries"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "event_presenters" (
        "event_id" INTEGER NOT NULL,
        "presenter_id" INTEGER NOT NULL,
        FOREIGN KEY("presenter_id") REFERENCES "presenters"("id"),
        FOREIGN KEY("event_id") REFERENCES "events"("id"),
        PRIMARY KEY("event_id","presenter_id")
    );
    INSERT INTO "countries" ("id","name") VALUES (1,'United Kingdom');
    INSERT INTO "organisations" ("id","name","location_id") VALUES (1,'Solent University',1);
    INSERT INTO "events" ("id","name","type","host_id") VALUES (1,'Data Science Workshop','workshop',1);
    INSERT INTO "presenters" ("id","name","organisation_id") VALUES (1,'Prins Butt',1);
    INSERT INTO "locations" ("id","city","country_id") VALUES (1,'Southampton',1);
    INSERT INTO "event_presenters" ("event_id","presenter_id") VALUES (1,1);
    COMMIT;
    """
    cursor.executescript(sql)
    db.commit()


def display_presenters():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    SELECT p.name, o.name 
    FROM presenters p 
    INNER JOIN organisations o ON p.organisation_id = o.id;
    """
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"{record[0]} ({record[1]})")


def display_events():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    SELECT e.name AS "event", l.city, c.name AS "country" 
    FROM events e 
    INNER JOIN organisations O ON e.host_id = o.id 
    INNER JOIN locations l ON o.location_id = l.id 
    INNER JOIN countries c ON l.country_id = c.id;
    """
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"{record[0]} ({record[1]}, {record[2]})")


def display_presenters_for_event(event_id):
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    SELECT e.name
    FROM events e
    WHERE e.id = ?;
    """
    values = [event_id]
    cursor.execute(sql, values)
    record = cursor.fetchone()

    print(f"The event name is: {record[0]}")

    sql = """
    SELECT p.name, o.name
    FROM presenters p 
    INNER JOIN event_presenters ep ON ep.presenter_id = p.id 
    INNER JOIN events e ON ep.event_id = e.id 
    INNER JOIN organisations o ON p.organisation_id = o.id
    WHERE e.id = ?;
    """
    cursor.execute(sql, values)
    records = cursor.fetchall()

    print("The presenters for this event are as follows:")
    for record in records:
        print(f"{record[0]} ({record[1]})")


def display_events_for_presenter(presenter_id):
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
    SELECT p.name
    FROM presenters p
    WHERE p.id = ?;
    """
    values = [presenter_id]
    cursor.execute(sql, values)
    record = cursor.fetchone()

    print(f"The presenter name is: {record[0]}")

    sql = """
    SELECT e.name AS "event" 
    FROM events e 
    INNER JOIN event_presenters ep ON ep.event_id = e.id 
    INNER JOIN presenters p ON ep.presenter_id = p.id 
    WHERE p.id = ?;
    """
    cursor.execute(sql, values)
    records = cursor.fetchall()

    print("The events for this presenter are as follows:")
    for record in records:
        print(record[0])


# setup()
# display_presenters()
# display_events()
# display_presenters_for_event(1)
# display_events_for_presenter(1)