// Hides all of the mentor cards
function hideAll() {
  $('.card').each(function () {
    this.style.display = "none";
  })
}

// Checks to see if the selected checkbox value, matches the provided data-attribute on the mentor card.
function checkAttributeMatch(cardAttribute, checkboxValue) {
  let match = false;

  if (checkboxValue == cardAttribute) {
    match = true;
  };

  return match;
}

// If the slected checkbox match the attributes of a mentor, then show that mentor card
function showSelectedMentor() {

  // Iterate for each checkbox that is active
  $('.form-check-input:checked').each(function () {

    // Finds all of the mentor cards
    const mentors = $(".cards").children();

    // Iterates through all of the mentor cards
    for (let i = 0; i < mentors.length; i++) {
      let mentor = mentors[i];

      // Check if the mentor card attribute matches the current checkbox value
      if (checkAttributeMatch(mentor.getAttribute("data-role"), this.value)) {

        // Displays the card if the tags match
        mentor.style.display = "flex";
      }
    }
  });
}

// Check when the search button is clicked
$(".search-mentors").click(function () {

  // First hide all mentor cards
  hideAll();

  // Shows selected mentors
  showSelectedMentor();
})