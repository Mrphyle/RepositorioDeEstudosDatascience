const prompt = require('prompt-sync')();
/* datainput */
grade1 = prompt("Enter the first grade: ");
grade2 = prompt("Enter the second grade: ");
grade3 = prompt("Enter the third grade: ");
/* process */
average = (parseFloat(grade1) + parseFloat(grade2) + parseFloat(grade3)) / 3;
if (average >= 7) {
    /* output */
    console.log("Approved"+" your grade is: " + average);
}
else if (average <= 6) {
    /* output */
    console.log("Disapproved"+" your grade is: " + average);
}