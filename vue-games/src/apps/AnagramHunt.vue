<template>
  <div id="ah-game-container" class="container-fluid">
    <!-- BE Msgs -->
    <div id="ah-msgs-div">
      <div id="ah-success-msg-div" v-if="successMessage" 
        class="msg-success success alert alert-success alert-dismissible text-center">
        <div id="success-msg" class="p-2">{{ successMessage }}</div>
        <button id="close-success-msg-btn" @click="successMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>

      <div id="ah-login-score-msg-div" v-if="errorMessage && loginUrl"  
        class="msg-info info alert alert-info alert-dismissible text-center">
        <div id="login-score-msg" class="px-0">
          {{ errorMessage }} <br />
          <a id="ah-login-score-link" v-if="loginUrl" :href="loginUrl" 
            class="m-0 p-0">Log in/Register</a>
        </div>
        <button id="close-score-msg-btn" @click="errorMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      
      <div id="ah-err-msg-div" v-if="errorMessage && !loginUrl"  
        class="msg-error error alert alert-danger alert-dismissible text-center">
        <div id="error-msg" class="p-2">{{ errorMessage }}</div>
        <button id="close-err-msg-btn" @click="errorMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    </div>
    <!-- END BE Msgs -->

    <!-- Start Screen -->
    <div id="ah-start-screen-div" v-if="screen=='start'" class="container">
      <div class="row m-auto">
        <div class="col">
          <div class="row justify-content-center">
            <label id="word-length-lbl" for="word-length" class="form-label col-3 me-1 text-end">
              Word Length</label>
            <select id="word-length" class="form-select w-50" v-model="wordLength">
              <option v-for="key in Object.keys(anagrams)" :key="key" :value="key">
                {{ key }}
              </option>
            </select>
          </div>
        </div>
      </div>

      <div id="ah-directions-div" class="row mx-3 my-1">
        <ol class="my-1">
          <li>Choose a word length.</li>
          <li>Press <strong>Play!</strong></li>
          <li>How many anagrams can you find in a minute?</li>
        </ol>
        <cite id="ah-directions-note" 
          class="my-2">* Note, anagrams must include all the letters of the displayed word.</cite>
        <button id="ah-play-btn" class="btn btn-primary w-100 my-3" @click="play">Play!</button>
      </div>
    </div>
    <!-- END Start Screen -->

    <!-- Play Screen -->
    <div id="ah-play-screen-div" v-else-if="screen == 'play'" class="container">
      <div id="ah-score-timer-row" class="row">
        <div class="col d-flex justify-content-between">
          <span id="ah-score">Score: {{ score }}</span>
          <span id="ah-timer">Time Left: {{ timeLeft }}</span>
        </div>
        <hr>
      </div>

      <div id="ah-question-row" class="row">
        <output class="display-5 text-center">{{ currentWord }} ({{ guessesLeft }} left)</output>
      </div>
      
      <div id="ah-answer-input-row" class="row">
        <input id="ah-answer-input" class="form-control" v-model="userInput" />
      </div>

      <div id="ah-correct-answers-div" class="row text-center">
        <ol id="ah-correct-answers-list">
          <li v-for="guess in correctGuesses" :key="guess">{{ guess }}</li>
        </ol>
      </div>
    </div>
    <!-- END Play Screen -->

    <!-- End Screen -->
    <div id="ah-end-screen-div" v-else-if="screen == 'end'" class="container">
      <div class="row">
        <h4 id="ah-times-up-msg" class="display-4 text-center">Time's Up</h4>
      </div>

      <div id="ah-final-score-row" class="row d-flex flex-col text-center">
        <p>You got</p>
        <div id="ah-final-score" class="display-3">{{ score }}</div>
        <p>Anagrams</p>
      </div>

      <div id="ah-end-btns-row" class="row d-flex flex-col text-center">
        <button id="ah-play-again-btn" @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button id="ah-back-2-start-btn" @click="screen = 'start'" class="btn btn-secondary w-100 m-1">
          Back to Start</button>
      </div>
    </div>
    <!-- END End Screen -->
  </div>
</template>

<style scoped>
  div, label {
    padding: 0.2rem;
  }
</style>

<script>
import axios from "axios";
import anagrams from "@/helpers/anagrams";
import {getRandomInteger} from "@/helpers/helpers";

export default {
  name: 'AnagramGame',

  data() {
    return {
      gameId: -1, // Default
      gameName: "anagram_hunt", 
      player: "",
      score: 0,
      anagrams: anagrams,
      currentWord: "",
      anagramList: [],
      wordLength: 5, // Default
      screen: "start",
      correctGuesses: [],
      userInput: "",
      interval: null,
      timeLeft: 60,
      errorMessage: "",
      loginUrl: "",
      successMessage: "",
    }
  }, // END data

  computed: {
    guessesLeft() {
      return this.anagramList.length - this.correctGuesses.length - 1;
    }
  }, // END computed

  methods: {
    play() {
      this.createGame();
      this.score = 0;
      this.screen = "play";
      this.newAnagramList();
      this.interval = setInterval(() => {
        this.timeLeft -= 1;
      }, 1000)
    },

    checkAnswer() {
      const input = this.userInput.toLowerCase()
      if (this.anagramList.includes(input) && !this.correctGuesses.includes(input) && this.currentWord !== input) {
        this.correctGuesses.push(input);
        this.userInput = "";
        this.score += 1;

        if (this.correctGuesses.length == this.anagramList.length - 1) {
          this.newAnagramList();
        }
      }
    },

    newAnagramList() {
      const currentAnagramList = [...this.anagramList];
      const potentialAnagramLists = this.anagrams[this.wordLength];
      this.anagramList = [...potentialAnagramLists[getRandomInteger(0, potentialAnagramLists.length)]];
      while (this.anagramList[0] === currentAnagramList[0]) {
        this.anagramList = [...potentialAnagramLists[getRandomInteger(0, potentialAnagramLists.length)]];
      }
      this.currentWord = this.anagramList[getRandomInteger(0, this.anagramList.length)];
      this.correctGuesses = [];
    },

    async createGame() {
      const data = {
        game_name: this.gameName,
        settings: {
            word_length: this.wordLength
        }
      };

      try {
          const response = await axios.post("/create-game/", data);

          console.log("Game created successfully:", response.data);
          this.gameId = response.data.game_id;
      } catch (error) {
          console.error("Error creating game:", error.response ? error.response.data : error.message);
      }
    },

    async recordFinalScore() {
      const data = {
        game_id: this.gameId,
        game_name: this.gameName,
         settings: {
            word_length: this.wordLength
        }, 
        final_score: this.score
      };

      try {
        const response = await axios.post("/submit-final-score/", data, {
          headers: { 
            "Content-Type": "application/json",
            "X-CSRFToken": document.cookie.match(/csrftoken=([^;]+)/)[1],  
          }
        });

        if (response.data.status === "success") {
          this.successMessage = response.data.message; 
        }

      } catch (error) {
        if (error.response && error.response.status === 401) {
          this.loginUrl = error.response.data.login_url;
          this.errorMessage = "Please, sign in/up to save your score!";

          sessionStorage.setItem("pendingScore", JSON.stringify(data));
          localStorage.setItem("returnToGame", window.location.href);
        } else {
          this.errorMessage = "Error saving score, not saved.";
          console.error("Error saving score:", error.response ? error.response.data : error.message);
        }
      }
    },
  }, // END methods

  watch: {
    userInput() {
      // check answer when user input changes
      this.checkAnswer()
    },

    timeLeft(newTime) {
      if (newTime == 0) {
        this.userInput = ""
        clearInterval(this.interval);
        this.timeLeft = 60;
        this.screen = "end";
        this.recordFinalScore(); 
      }
    }
  }, // END watch

  // Lifecycle Hook Overrides & Methods
  mounted() {
    const pendingScore = sessionStorage.getItem("pendingScore");

    if (pendingScore) {
      sessionStorage.removeItem("pendingScore");

      axios.post("/submit-final-score/", JSON.parse(pendingScore), {
          headers: { "Content-Type": "application/json" }
      }).then(() => {
        // CANNOT get this alert to work as a Django message, no matter what I do.
          alert("Thanks for logging in!  Score saved successfully.");
      }).catch(error => {
          console.error("Error saving score after login:", error.response ? error.response.data : error.message);
      });
    }
  }, // END mounted()
}
</script>