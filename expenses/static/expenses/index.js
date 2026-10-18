
/* 1. Find the form in the HTML page */
const form = document.querySelector("form");

/* 2. Find the expense name and amount input boxes */
const expenseName = document.getElementById("expense-name");
const expenseAmount = document.getElementById("expense-amount");

/* 3. Find the list where expenses will appear */
const expenseList = document.getElementById("expense-list");

/* 4. Listen when the user submits the form */
form.addEventListener("submit", function(event) {

    /* Stop the page from refreshing */
    event.preventDefault();
    // Check if the user entered a name and amount
if (expenseName.value === "" || expenseAmount.value === "") {
    alert("Please enter an expense name and amount.");
    return;
}

    /* 5. Create a new list item for the expense */
    const li = document.createElement("li");

    /* Put the expense name and amount inside the list item */
    li.textContent = expenseName.value + " - $" + expenseAmount.value;

    /* Add the expense to the webpage */
    expenseList.appendChild(li);

    /* 6. Find the place where the total is displayed */
    const total = document.getElementById("total");

    /* 7. Add the new expense to the total */
    let currentTotal = Number(total.textContent);
    currentTotal += Number(expenseAmount.value);

    /* Display the total with two decimal places */
    total.textContent = currentTotal.toFixed(2);

    /* 8. Clear the input boxes for the next expense */
    expenseName.value = "";
    expenseAmount.value = "";

    /* 9. Print messages in the browser console */
    console.log("Expense added successfully!");
});
