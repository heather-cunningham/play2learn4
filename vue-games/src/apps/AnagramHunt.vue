<template>
  <div id="ah-game-container" class="container">
    <!-- Start Screen -->
    <div id="ah-start-screen-div" v-if="screen=='start'" class="container">
      <div class="row m-auto">
        <div class="col">
          <div class="row justify-content-center">
            <label for="word-length" class="form-label col-3 me-1 text-end">Word Length</label>
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
        <cite class="mb-2">*Note, anagrams must include all the letters of the given word.</cite>
        <button class="btn btn-primary w-100 mb-3" @click="play">Play!</button>
      </div>
    </div>

    <!-- Play Screen -->
    <div v-else-if="screen == 'play'" class="container">
      <div class="row">
        <div class="col d-flex justify-content-between">
          <span>Score: {{ score }}</span>
          <span>Time Left: {{ timeLeft }}</span>
        </div>
        <hr>
      </div>
      <div class="row">
        <output class="display-5 text-center">{{ currentWord }} ({{ guessesLeft }} left)</output>
      </div>
      <div class="row">
        <input class="form-control" v-model="userInput">
      </div>
      <div class="row text-center">
        <ol>
          <li v-for="guess in correctGuesses" :key="guess">{{ guess }}</li>
        </ol>
      </div>
    </div>

    <!-- End Screen -->
    <div v-else-if="screen == 'end'" class="container">
      <div class="row">
        <h4 class="display-4 text-center">Time's Up</h4>
      </div>
      <div class="row d-flex flex-col text-center">
        <p>You got</p>
        <div class="display-3">{{ score }}</div>
        <p>Anagrams</p>
      </div>
      <div class="row d-flex flex-col text-center">
        <button @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button @click="screen = 'start'" class="btn btn-secondary w-100 m-1">Back to Start Screen</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  div, label {
    padding: 0.2rem;
  }
</style>

<script>
import anagrams from "@/helpers/anagrams";
import {getRandomInteger} from "@/helpers/helpers";

export default {
  name: 'AnagramGame',
  data() {
    return {
      userName: '',
      score: 0,
      timeLeft: 60,
      anagrams: anagrams,
      currentWord: "",
      anagramList: [],
      wordLength: 5,
      screen: "start",
      correctGuesses: [],
      userInput: "",
      interval: null,
    }
  },
  computed: {
    guessesLeft() {
      return this.anagramList.length - this.correctGuesses.length - 1;
    }
  },
  methods: {
    play() {
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
    async recordScore() {
      // TODO: when Anagram Hunt finishes, make an Ajax call with axios (this.axios)
      // to record the score on the backend
    }
  },
  watch: {
    userInput() {
      // check answer when user input changes
      this.checkAnswer()
    },
    timeLeft(newValue) {
      if (newValue == 0) {
        this.screen = "end";
        this.timeLeft = 60;
        clearInterval(this.interval);
        this.recordScore(); // calls recordScore
      }
    }
  }
}
</script>