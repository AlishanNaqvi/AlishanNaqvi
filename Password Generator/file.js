// Function to Copy Password
function copyPassword(id) {
    const password = document.getElementById(id);
    password.select();
    password.setSelectionRange(0, 99999); // For mobile devices
    document.execCommand('copy');
    alert('Password copied: ' + password.value);
  }
  
  // Function to Generate Random Passwords
  function generatePasswords() {
    const includeNumbers = document.getElementById('numbers').checked;
    const includeUppercases = document.getElementById('uppercases').checked;
    const includeLowercases = document.getElementById('lowercases').checked;
    const includeSymbols = document.getElementById('symbols').checked;
  
    const numbers = '0123456789';
    const upperCases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowerCases = 'abcdefghijklmnopqrstuvwxyz';
    const symbols = '!@#$%^&*()_+[]{}|;:,.<>?';
  
    let charPool = '';
  
    // Add character sets to the pool based on user's selection
    if (includeNumbers) charPool += numbers;
    if (includeUppercases) charPool += upperCases;
    if (includeLowercases) charPool += lowerCases;
    if (includeSymbols) charPool += symbols;
  
    // Function to generate a random password
    function generateRandomPassword(length) {
      let password = '';
      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charPool.length);
        password += charPool[randomIndex];
      }
      return password;
    }
  
    // Update the password input fields with new random passwords
    document.getElementById('password-1').value = generateRandomPassword(12);
    document.getElementById('password-2').value = generateRandomPassword(12);
    document.getElementById('password-3').value = generateRandomPassword(12);
  }
  