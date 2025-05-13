<template>
  <div class="container" style="width: 500px">
    <!-- BEGIN MF Start Screen -->
    <!-- <div v-if="screen=='start'" class="container"> -->
    <div v-show="screen=='start'" class="container">
      <div class="row">
        <div class="col">
          <div class="row">
            <label for="operation" class="form-label col-3">Operation</label>
            <select id="operation" class="form-select col" v-model="operation">
              <option v-for="symbol, operation in operations" :key="operation" :value="symbol">
                {{ operation }}
              </option>
            </select>
          </div>
          <div class="row">
            <label for="max-number" class="form-label col-3">Max Number</label>
            <input id="max-number" class="form-control col" type="number" min="1" max="100" v-model="maxNumber">
          </div>
        </div>
      </div>
      <div class="row m-auto">
        <ol>
          <li>Choose Operation and Max Number</li>
          <li>Press <strong>Play!</strong></li>
          <li>How many questions can you get in a minute?</li>
        </ol>
      </div>
      <button class="btn btn-primary w-100" @click="play">Play!</button>
    </div><!-- END MF Start Screen -->
    
    <!-- BEGIN MF Play Screen -->
    <!-- <div v-else-if="screen == 'play'" class="container"> -->
    <div v-show="screen == 'play'" class="container">
      <div class="row">
        <div class="col d-flex justify-content-between">
          <span>Score: {{ score }}</span>
          <span>Time Left: {{ timeLeft }}</span>
        </div>
        <hr>
      </div>
      <div class="row">
        <output class="display-5 text-center">{{ number1 }} {{ operation }} {{ number2 }} = </output>
      </div>
      <div class="row">
        <input class="form-control m-auto" v-model="userInput" style="width: 200px">
      </div>
      <div class="row m-auto" style="width: 300px">
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
    </div> <!-- END MF Play Screen -->
    
    <!-- BEGIN MF Final Screen -->
    <!-- <div v-else-if="screen == 'end'" class="container"> -->
    <div v-show="screen == 'end'" class="container">
      <div class="row">
        <h4 class="display-4 text-center">Time's Up</h4>
      </div>
      <div class="row d-flex flex-col text-center"><!-- Final Score Div-->
        <p>You answered</p>
        <div class="display-3">{{ score }}</div>
        <p>questions</p>
      </div><!-- END Final Score Div-->
      
      <!-- Record Final Score Div-->
      <div>
        <div>
          <label id="username_lbl" for="username_input">Username</label>
          <input id="username_input" name="Username" v-model="username" />
        </div>
        <div>
          <label id="score_lbl" for="score_input">Final Score</label>
          <input id="score_input" name="FinalScore" v-model="score" />
        </div>
        <button @click="recordScore()">Record Score</button>
      </div>
      <!-- END  Record Final Score Div-->
      
      <div class="row d-flex flex-col text-center">
        <button @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button @click="screen = 'start'" class="btn btn-secondary w-100 m-1">Back to Start Screen</button>
      </div>
    </div>
  </div><!-- END MF Final Screen -->
</template>

<style scoped>
  div, label {
    padding: 0.2rem;
  }
</style>

<script>
import { getRandomInteger } from '@/helpers/helpers';

export default {
  name: 'MathFacts',

  data() {
    return {
      gameName: "Math Facts",
      score: 0,
      screen: "start",
      maxNumber: 30,
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
      username: "",
    }
  }, // END data

  methods: {
    play() {
      this.screen = "play";
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

    async recordScore() {
      // TODO: when Math Facts finishes, make an Ajax call with axios (this.axios)
      // to record the score on the backend
      const scoreData = {
        "username": this.username,
        "final_score": this.score,
        "game_name": this.gameName,
      };
      const response = (await this.axios.post("/record-score/", scoreData)).data;

      console.log(response);
    }
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
        clearInterval(this.interval);
        this.timeLeft = 60;
        this.screen = "end";
        this.recordScore(); // call to record score
      }
    }
  }// END watch
}
</script>