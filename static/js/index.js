async function loadGuest() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/authGuest');
      // if (!response.ok) {
      //   throw new Error("HTTP error " + response.status);
      // }
      
      const data = await response.json();
      document.getElementById("login").style.display="none"
      document.getElementById("userName").innerText=data.guestName;
      console.log(data); // see data in console
    } catch (error) {
      console.error("Error loading guest:", error);
      document.getElementById("login").style.display="block" 
      document.getElementById("profile").style.display="none"
    }

  // Load when page starts

  }
    loadGuest();