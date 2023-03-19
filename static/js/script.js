/**
 * Hides all of the mentor cards.
 */
function hideAll() {
  $('.card').each(function () {
    this.parentElement.style.display = "none";
  })
}

/**
 * Checks to see if the selected checkbox value, matches the provided data-attribute on the mentor card.
 * @param {string} cardAttribute the attribute taken from the mentor card
 * @param {string} checkboxValue the value of the current selected checkbox
 * @returns {boolean} if the cardAttribute and checkboxValue are equal
 */
function checkAttributeMatch(cardAttribute, checkboxValue) {
  console.log(cardAttribute)
  let match = false;

  if (checkboxValue == cardAttribute) {
    match = true;
  };

  return match;
}


/**
 * If the selected checkbox value matches the attributes of a mentor, then show that mentor card.
 */
function showSelectedMentor() {

  // Iterate for each checkbox that is active
  $('.form-check-input:checked').each(function () {

    // Finds all of the mentor cards
    const mentors = $(".card");

    // Iterates through all of the mentor cards
    for (let i = 0; i < mentors.length; i++) {
      let mentor = mentors[i];
      
      console.log(`data-{$this.name}`)
      // Check if the mentor card attribute matches the current checkbox value
      if (checkAttributeMatch(mentor.getAttribute(`data-${this.name}`), this.value)) {

        // Displays the card if the tags match
        mentor.parentElement.style.display = "block";
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