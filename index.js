
const form = document.querySelector("form");
const expenseName = document.getElementById("expense-name");
const expenseAmount = document.getElementById("expense-amount");
const expenseList = document.getElementById("expense-list");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const li = document.createElement("li");
    li.textContent = expenseName.value + " - $" + expenseAmount.value;
    expenseList.appendChild(li);
    const total = document.getElementById("total");
let currentTotal = 0;

currentTotal += Number(expenseAmount.value);
total.textContent = currentTotal.toFixed(2);
expenseName.value = "";
expenseAmount.value = "";
    console.log("Expense:", expenseName.value);
    console.log("Amount:", expenseAmount.value);
    console.log("Hello, Budget Tracker!");
});
