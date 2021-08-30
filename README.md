Car Parking Space Management System

# CONTRIBUTING

We welcome bug fixes, ehancements, new features, and feedback at email: nminhstickpk@gmail.com

Please contact to me before submit pull requests We use Gitflow, so main branch is reserved for releases.

# CONTENTS

Hardware - hardware for this project.

Software - software for this project.

Architecture design - brief idea about how the system works.

README.md - instruction for using this repo.

# PROBLEMS

- Ecomony Issuse:

+ Inefficient use of existing parking capacity:  Due to the fact that not dividing space properly or even not doing it, maximizing space is unattainable.

+ Confusing parking policies: regulations and usual fees may apply at certain times but not always. Plus, because of human involvement, the wrong when do the calculation of parking fee is inevitable.

- Limited security: Without using video surveillance system, our parking lots are vulnerable to threats such as: theft from cars (belongings in the cars or external components), theft of cars or vandalism.

It is because of us not making use of cutting-edge technology that causes these problems. Plus, it is common in Viet Nam to hire low-skilled labor to work at parking lot.

# SOLUTIONS: 

We focus on implement innovations to solve isssue. The technologies we use are:

- RFID technology: RFID is an Automatic Identification and Data Capture (AIDC) technology that uses RF waves to transfer data between a reader and a tagged object. Basically, it is a card with a unique id so if each customer is given a RFID card, vehicle identification can be done automatically. This use of this technology decrease the workload of check-in, out and mantain the records of cars passing by, resulting in automatic fee calculation. Plus, the barrier is also controlled by the system so that it will open only if the vehicle is authentic.

- Camera surveillance system: 

+ Firstly, cameras are setup in sercurity with automatic number plate recognition algorithm. With RFID technology, this identify the vehicle.

+ Secondly, cameras in each local check for number of cars inside a parking lot in order to maximizing the use of space.

+ Thirdly, the main reason is for monitoring and surveillance.

# WHAT WE HAVE DONE:
- Designing architecture for our system. This gives a brief understanding of how the data are collected, stored and viewed.

- Hardware design for sensor checking car vacancy and transfer data to the database.

- Building admin interface to monitor and observe the system.

- Showing some of the data gathered via website.


