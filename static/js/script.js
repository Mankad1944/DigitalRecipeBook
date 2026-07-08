// function showSuccessMessage() {
//     const msg = document.getElementById("message");
//     msg.innerText = "🎉 Registration Successful!";
    
//     // Hide after 3 seconds
//     setTimeout(() => {
//       msg.innerText = "";
//     }, 3000);
//   }

function showSuccess() {
    const msg = document.getElementById("successMessage");
    msg.style.display = "block";
  
    // Auto-hide after 3 seconds
    setTimeout(() => {
      msg.style.display = "none";
    }, 5000);
  }
  
