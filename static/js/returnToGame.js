/* Function to return to the game's page after playing a game when not logged in. */
window.addEventListener("load", function () {
  const returnToGame = localStorage.getItem("returnToGame");

  if (returnToGame) {
    setTimeout(() => {
      fetch("/check-auth-status/")
        .then((response) => response.json())
        .then((data) => {
          if (data.is_authenticated) {
            localStorage.removeItem("returnToGame"); 
            window.location.href = returnToGame;
          }
        });
    }, 250);
  }
});
