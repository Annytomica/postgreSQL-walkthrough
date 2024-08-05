from sqlalchemy import (
    create_engine, Column, Integer, String, MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost "chinook" db
# /// indicates the chinook database is hosted within local environment
db = create_engine("postgresql:///chinook")

#  grab the metadata that is produced by our database table schema, 
# and creates a subclass to map everything back to us here within the 'base' variable.
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to database directly, we are asking for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

anny_devoy = Programmer(
    first_name = "Anny",
    last_name = "Devoy",
    gender = "F",
    nationality = "New Zealander",
    famous_for = "Genome Engineering"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(anny_devoy)


# updating a single record -> use .first() otherwise will be expected to iterate over query list even if 1 entry
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Earth Survival"

# commit our session to the database
# session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming - to avoid deleting the wrong record(s)
if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")

# deleting all records - do not actually run this code!
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(pregrammer)
#     session.commit()

# query the database to find all the Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + ' ' + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )