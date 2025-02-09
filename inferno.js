

// const username = localStorage.getItem("username");
// console.log(username)

// const submit = ()=>{
//     alert("submit")
//     localStorage.setItem("username", "JohnDoe");
// }

// document.getElementById("inviteForm").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevents page reload

//     // Get form values
//     let name = document.getElementById("name").value;
//     let person = document.getElementById("person").value;
//     let date = document.getElementById("date").value;
//     let location = document.getElementById("location").value;

//     // Format the message
//     let message = `
//         <h3>🎉 Invitation Created! 🎉</h3>
//         <p><strong>${person}</strong>, you have been invited by <strong>${name}</strong> to go out!</p>
//         <p><strong>Date & Time:</strong> ${date}</p>
//         <p><strong>Location:</strong> ${location}</p>
//         <p>Hope to see you there! 😊</p>
//     `;

//     // Display the message
//     let messageDiv = document.getElementById("message");
//     messageDiv.innerHTML = message;
//     messageDiv.classList.remove("hidden");
//     localStorage.setItem("username", "JohnDoe");

//     // Clear the form
//     document.getElementById("inviteForm").reset();
// });