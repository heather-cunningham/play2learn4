<template>
  <div id="mf-game-container" class="container-fluid" :key="gameInstanceId">
    <!-- BE Msgs -->
    <div id="mf-msgs-div" v-if="screen=='end'">
      <div id="mf-success-msg-div" v-if="successMessage" 
        class="msg-success success alert alert-success alert-dismissible text-center">
        <div id="success-msg" class="p-2">{{ successMessage }}</div>
        <button id="close-success-msg-btn" @click="successMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>

      <div id="mf-login-score-msg-div" v-if="errorMessage && loginUrl"  
        class="msg-info info alert alert-info alert-dismissible text-center">
        <div id="login-score-msg" class="px-0">
          {{ errorMessage }} <br />
          <a id="mf-login-score-link" v-if="loginUrl" :href="loginUrl" 
            class="m-0 p-0">Log in/Register</a>
        </div>
        <button id="close-score-msg-btn" @click="errorMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      
      <div id="mf-err-msg-div" v-if="errorMessage && !loginUrl"  
        class="msg-error error alert alert-danger alert-dismissible text-center">
        <div id="error-msg" class="p-2">{{ errorMessage }}</div>
        <button id="close-err-msg-btn" @click="errorMessage = ''" type="button" 
          class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    </div>
    <!-- END BE Msgs -->

    <!-- Start Screen -->
    <div id="mf-start-screen-div" v-if="screen=='start'" class="container">
      <div class="row">
        <div class="col">
          <div class="row justify-content-center">
            <label id="operation-lbl" for="operation" class="form-label col-3 me-1 text-end">Operation</label>
            <select id="operation" class="form-select w-50" v-model="operation">
              <option v-for="symbol, operation in operations" :key="operation" :value="symbol">
                {{ operation }}
              </option>
            </select>
          </div>
          <div class="row justify-content-center">
            <label id="max-number-lbl" for="max-number" class="form-label col-3 me-1 text-end">
              Max Operand</label>
            <input id="max-number" class="form-control w-50" type="number" min="1" max="100"
               v-model="maxNumber" />
          </div>
        </div>
      </div>

      <div id="mf-directions-div" class="row mx-3 my-1">
        <ol>
          <li>Choose an arithmetic operation and a max operand.</li>
          <li>Press <strong>Play!</strong></li>
          <li>How many equations can you solve in a minute?</li>
        </ol>
        <button id="mf-play-btn" class="btn btn-primary w-100 mb-3" @click="play">Play!</button>
      </div>
    </div>
    <!-- END Start Screen -->

    <!-- Play Screen -->
    <div id="mf-play-screen-div" v-else-if="screen == 'play'" class="container">
      <div id="mf-score-timer-row" class="row">
        <div class="col d-flex justify-content-between">
          <span id="mf-score">Score: {{ score }}</span>
          <span id="mf-timer">Time Left: {{ timeLeft }}</span>
        </div>
        <hr>
      </div>

      <div id="mf-question-row" class="row">
        <output class="display-5 text-center">{{ number1 }} {{ operation }} {{ number2 }} = </output>
      </div>

      <div id="mf-answer-input-row" class="row">
        <input id="mf-answer-input" class="form-control m-auto" v-model="userInput"/>
      </div>

      <div id="mf-calculator-div" class="row m-auto">
        <div class="row gx-1">
          <div class="col-4">
            <button @click="userInput += '1'" class="btn btn-primary w-100">1</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '2'" class="btn btn-primary w-100">2</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '3'" class="btn btn-primary w-100">3</button>
          </div>
        </div>
        <div class="row gx-1">
          <div class="col-4">
            <button @click="userInput += '4'" class="btn btn-primary w-100">4</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '5'" class="btn btn-primary w-100">5</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '6'" class="btn btn-primary w-100">6</button>
          </div>
        </div>
        <div class="row gx-1">
          <div class="col-4">
            <button @click="userInput += '7'" class="btn btn-primary w-100">7</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '8'" class="btn btn-primary w-100">8</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '9'" class="btn btn-primary w-100">9</button>
          </div>
        </div>
        <div class="row gx-1">
          <div class="col-4">
            <button @click="userInput += '0'" class="btn btn-primary w-100">0</button>
          </div>
          <div class="col-8">
            <button @click="userInput = ''" class="btn btn-primary w-100">Clear</button>
          </div>
        </div>
      </div>
    </div>
    <!-- END Play Screen -->

    <!-- End Screen -->
    <div id="mf-end-screen-div" v-else-if="screen == 'end'" class="container">
      <div class="row">
        <h4 id="mf-times-up-msg" class="display-4 text-center">Time's Up</h4>
      </div>

      <div id="mf-final-score-row" class="row d-flex flex-col text-center">
        <p>You answered</p>
        <div id="mf-final-score" class="display-3">{{ score }}</div>
        <p>questions</p>
      </div>

      <div id="mf-end-btns-row" class="row d-flex flex-col text-center">
        <button id="mf-play-again-btn" @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button id="mf-back-2-start-btn" @click="screen = 'start'" class="btn btn-secondary w-100 m-1">
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
import { getRandomInteger } from '@/helpers/helpers';

export default {
  name: "MathFacts",

  data() {
    return {
      gameId: -1, // Default
      gameInstanceId: 0, // To force component refresh
      gameName: "math_facts", 
      player: "",
      score: 0,
      screen: "start",
      maxNumber: 10, // default
      operation: "+",
      operations: {
        "Addition": "+",
        "Subtraction": "-",
        "Multiplication": "x",
        "Division": "/"
      },
      number1: 0,
      number2: 0,
      userInput: "",
      interval: null,
      timeLeft: 60,
      errorMessage: "",
      loginUrl: "",
      successMessage: "",
    }
  }, // END data

  methods: {
    play() {
      this.createGame();
      this.$nextTick(() => {
        this.screen = "play";
      });
      if (this.interval) {
        clearInterval(this.interval);
      }
      this.gameInstanceId++; // To force Vue to re-render
      this.timeLeft = 60; 
      this.score = 0;
      this.getNewQuestion();
      this.interval = setInterval(() => {
        this.timeLeft--;
      }, 1000)
    },

    getNewQuestion() {
      let num1 = getRandomInteger(0, this.maxNumber + 1);
      let num2 = getRandomInteger(0, this.maxNumber + 1);
      if (this.operation == "-") {
        this.number1 = Math.max(num1, num2);
        this.number2 = Math.min(num1, num2);
      }
      else if (this.operation == "/") {
        this.number1 = num1 * num2;
        this.number2 = num2;
      }
      else {
        this.number1 = num1;
        this.number2 = num2;
      }
    },

    async createGame() {
      const data = {
        game_name: this.gameName,
        settings: {
            operation: this.operation,
            max_number: this.maxNumber,
        }
      };

      try {
          const response = await axios.post("/create-game/", data);
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
            operation: this.operation,
            max_number: this.maxNumber
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

  computed: {
    correctAnswer() {
      if (this.userInput.trim() == "") {
        return false;
      }

      const input = parseInt(this.userInput);
      if (this.operation == "+") {
        return input === this.number1 + this.number2;
      }

      if (this.operation == "-") {
        return input === this.number1 - this.number2;
      }

      if (this.operation == "x") {
        return input === this.number1 * this.number2;
      }

      if (this.operation == "/") {
        return input === this.number1 / this.number2;
      }

      return false;
    },
  }, // END computed

  watch: {
    userInput() {
      if (this.correctAnswer) {
        this.score++; 
        this.getNewQuestion();
        this.userInput = "";
      }
    },

    timeLeft(newTime) {
      if (newTime === 0) {
        this.userInput = ""
        if (this.interval) {
          clearInterval(this.interval);
        }
        this.timeLeft = 60;
        this.screen = "end";
        this.recordFinalScore(); 
      }
    }
  }, // END watch

  // Lifecycle Hook Overrides & Methods
  mounted() {
    const pendingScore = sessionStorage.getItem("pendingScore")

    if (pendingScore) {
      sessionStorage.removeItem("pendingScore");

      axios.post("/submit-final-score/", JSON.parse(pendingScore), {
          headers: { "Content-Type": "application/json" }
      }).then(() => {
        // CANNOT get this Django message to work, no matter what I do.
        // this.successMessage = "Thanks for logging in! Score saved successfully.";
        alert("Thanks for logging in! Score saved successfully."); // Turned this one back into a JS alert instead. 
      }).catch(error => {
        this.errorMessage = "Error saving score, not saved.";
        console.error("Error saving score after login:", error.response ? error.response.data : error.message);
      });
    }
  }, // END mounted()
}
</script>