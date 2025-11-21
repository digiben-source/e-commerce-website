// Simulated user database
let users = [];

// Function to handle form submission for login
document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();
  let username = document.getElementById('loginUsername').value;
  let password = document.getElementById('loginPassword').value;
  
  // Check if user exists in the database
  let userExists = users.find(user => user.username === username && user.password === password);
  
  if (userExists) {
    // Show the "Go To Home" button
    document.getElementById('homeButtonContainer').style.display = 'block';
  } else {
    alert('Invalid username or password. Please try again.');
  }
  
  // Clear the login form
  document.getElementById('loginForm').reset();
});

// Function to handle form submission for signup
document.getElementById('signupForm').addEventListener('submit', function(event) {
  event.preventDefault();
  let username = document.getElementById('signupUsername').value;
  let password = document.getElementById('signupPassword').value;
  
  // Check if username already exists
  let userExists = users.some(user => user.username === username);
  
  if (!userExists) {
    // Add the new user to the database
    users.push({ username, password });
    alert('User successfully registered!');
  } else {
    alert('Username already exists. Please choose a different username.');
  }
  
  // Clear the signup form
  document.getElementById('signupForm').reset();
});

// Function to handle "Go To Home" button click
document.getElementById('homeButton').addEventListener('click', function() {
  alert('Redirecting to home page...');
  // Implement redirection logic here
});