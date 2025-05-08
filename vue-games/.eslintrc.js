module.exports = {
  root: true,
  env: {
    node: true
  },
  parser: "vue-eslint-parser",
  parserOptions: {
    parser: "@babel/eslint-parser",
    requireConfigFile: false
  },
  extends: ["plugin:vue/vue3-essential", "eslint:recommended"]
};  