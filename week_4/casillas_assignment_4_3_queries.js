/*
  Title: casillas_assignment_4_3_queries.js
  Author: Maxine Casillas
  Date: 2026-06-28
  Description: MongoDB Shell queries for Assignment 4.3.
*/

// a. Display all users in the collection.
db.users.find();

// b. Display the user with the email address jbach@me.com.
db.users.find({ email: "jbach@me.com" });

// c. Display the user with the last name Mozart.
db.users.find({ lastName: "Mozart" });

// d. Display the user with the first name Richard.
db.users.find({ firstName: "Richard" });

// e. Display the user with employeeId 1010.
db.users.find({ employeeId: "1010" });
