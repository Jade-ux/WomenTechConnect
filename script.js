// Hides all of the mentor cards
function hideAll() {
    $('.card').each(function () {
      this.style.display = "none";
    })
  }
  
  // Checks to see if the selected checkbox matches the tags on the mentor cards.
  function checkRole(requiredRole, mentor) {
    let role = mentor.value;
    let selected = false;
  
    if (role == requiredRole) {
      selected = true;
    };
  
    return selected;
  }
  
  // Check when the search button is clicked
  $(".search-mentors").click(function () {
  
    // First hide all mentor cards
    hideAll();
  
    // Return the values of only the checked element
    $('.form-check-input:checked').each(function () {
  
      // Finds all of the mentor cards
      const mentors = $(".cards").children();
  
      // Iterates through all of the mentor cards
      for (let i = 0; i < mentors.length; i++) {
        let mentor = mentors[i];
  
        // Check if the card tags match the selected checkboxes
        if (checkRole(mentor.getAttribute("data-role"), this)) {
  
          // Displays the card if the tags match
          mentor.style.display = "flex";
        }
      }
    });
  })