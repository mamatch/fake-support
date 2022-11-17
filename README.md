# Fake Support

When international students wants to go abroad his country to continue his studies,
they are often asked to prove that they have sufficient resources to live there (
ecept if they have a scholarship). It can be a blocked bank account with the money inside
or they need a person who sign an assumption of responsibility testifying that they have an activity
which helps them to earn enough money to take care of the student. You can guess that a business was born
behind that. Students whose family doesn't have enough means have to buy someone (who is supposed to earn enough)
to sign that document. The problem is that when the person resides on territory of the destination country( eg. Belgium)
,
The control of the documents are not done before they are signed by the administration so many students discover later
that they have been deceived, and a fraud on a such important document results in a visa denial or for those
who were already on the territory and wanted to renew their residence permit, they asked to get back home.

Such behaviour of person which can ruin tha life of students who just want to get the opportunity to get a better life
is unforgivable. With Fake-Support we want to give them a way to know if a person is trustworthy. We want to provide a
sort of black list for people who had already been identified as scammers, and a tools to ensure information about the
one who is not on the list are real.

## Features

A user who gets on our platform can:

- Make a search on the scammers database: The search can be done the name, surname, city, country, the name of
  the agent who approves the document, etc...
- Add a possible scammer to the database: He will provide all tha information he has the documents to prove it.

## For Contributors

### Setup

Clone the repo:

```
git clone https://github.com/mamatch/fake-support.git
cd fake-support
``

Before running the following commands sure postgres-sql server and clients are installed.
Setup the dev environment:

```

export FLASK_APP=fake_support.py
make setup

```

### Run

```

make run

```

