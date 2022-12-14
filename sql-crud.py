from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Excecuting the instruction from "chinook"
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "programer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of cpnnecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)


# Open an actual session by calling th Session() subclass above
session = Session()


# Creating the database using declarative_base subclasss
base.metadata.create_all(db)


# creating records on our Programer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margret_hamilton = Programmer(
    first_name="Margret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

justin_brown = Programmer(
    first_name="Justin",
    last_name="Brown",
    gender="M",
    nationality="British",
    famous_for="Student full stack developer"
)

# add each intance of programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(justin_brown)


# updating a SINGLE record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# # commit our session to the database
# session.commit()


# # updating MULTIPLE records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# # deleting a single record via fname & lname
# fname = input("Enter a firt name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No record found")

# delete multiple records
programmers = session.query(Programmer)
for programmer in programmers:
    session.delete(programmer)
    session.commit()

# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer. gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
