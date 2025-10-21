async function loadGuest() {
    try {
      const response = await fetch('http://192.168.100.11:8000//api/authGuest');
      // if (!response.ok) {
      //   throw new Error("HTTP error " + response.status);
      // }
      
      const data = await response.json();
      console.log("", data);
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

  async function setBookingID(roomID,guestCount,roomType){ 
    document.getElementById('modalBookingID').value=`#${roomID}`
  
    // room section-box
    const response=await fetch(`http://192.168.100.11:8000/api/rooms/${guestCount}/${roomType}`)
    const rooms=await response.json()
    rooms.forEach(room => {
      document.getElementById('roomSelect').innerHTML+=`<option value=${ room.roomID }>${ room.building } - ${room.roomCode} </option>`
    });
    };

  function openDeleteModal(bookingID) {
  document.getElementById("modalBookingID").value = bookingID;
  const modal = new bootstrap.Modal(document.getElementById("deleteBookingModal"));
  modal.show();
  }

function createStay() {
  const bookingID = document.getElementById("modalBookingID").value;
  fetch(`/createStay/${bookingID}/`, {
    method: "POST",
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  })
  .then(response => {
    if (response.ok) {
      alert("Stay created successfully!");
      location.reload();
    }
  });
}



// Helper to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
