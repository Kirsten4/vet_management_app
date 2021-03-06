
# Vet Management App

## Project Brief: 
### Vet Management App
A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

### MVP
- The practice wants to be able to register / track animals. Important information for the vets to know is -
  - Name
  - Date Of Birth (use a VARCHAR initially)
  - Type of animal
  - Contact details for the owner
  - Treatment notes
- Be able to assign animals to vets
- CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?
### Possible Extensions
- Mark owners as being registered/unregistered with the Vet. unregistered owners won't be able to add any more animals.
- If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have many pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)
- Handle check-in / check-out dates
- Let the practice see all animals currently in the practice (today's date is between the check-in and check-out?)
- Sometimes an owner does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 yr old dog is now 4.
- Add extra functionality of your choosing - assigning treatments, a more comprehensive way of maintaining treatment notes over time. Appointments. Pricing / billing.

## Instructions for use:
### Set-up:
  - create the database (command: createdb vet_database)
  - set up database tables (command: psql -d vet_database -f db/vet_database.sql)
  - run the console file to populate the tables with data (command: python3 console.py)
  - run Flask from the folder the project is stored in
### Using the app:
  - Accesss main functionality from quick access buttons on home page
  - The following CRUD functionality is avialble on each page for Vets, Owners, Animals and Appointments:
    - Add/Register (Create)
    - View (Read)
    - Edit (Update)
    - Delete (Delete)
  - Unregistered owners cannot add new animals
  - Vets are auto-assigned when registering the animal. The vet which has the least animals already assigned to them will be selected.
  - Animals can be checked in from the appointments page
    - If they do not have an appointment today you get a warning message and cannot check them in
    - Once checked in they appear in the animals page in the table "Animals currently in practice"
    - They can then be checked out using the check out button in this table and a price for the treatment will be shown for payment
  - The animals button on the owners page shows a list of all animals belonging to that owner
  - Each animal has treatment notes listed in date order
    - New notes can be added and they will have today's date

## Technologies Used
- Python
- HTML
- CSS
- Flask
- SQL

## Possible Future Extensions
- Add medication schedule
- Show repeat prescriptions to be ordered when due
- Book appointments based on vet schedule/availability
- Show list of animals marked as requiring a follow-up
- Calculate bill based on if the owner is insured and only pays an excess

## Screenshots:
![home-page](https://github.com/Kirsten4/vet_management_app/blob/main/static/img/home-page.png)
![appointments-page](https://github.com/Kirsten4/vet_management_app/blob/main/static/img/appointments-page.png)
![animals-page](https://github.com/Kirsten4/vet_management_app/blob/main/static/img/animals-page.png)
