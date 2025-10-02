const loginScreen = document.getElementById("login-screen");
const quizContainer = document.getElementById("quiz-container");
const usernameInput = document.getElementById("username");
const loginBtn = document.getElementById("login-btn");
const userDisplay = document.getElementById("user-display");
const questionContainer = document.getElementById("question-container");
const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");
const restartBtn = document.getElementById("restart-btn");
const loadBtn = document.getElementById("load-btn");
const submitBtn = document.getElementById("submit-btn");
const timerDisplay = document.getElementById("timer");
const scoreDisplay = document.getElementById("score");
const finalScore = document.getElementById("final-score");

const questions = [
  {
    q: "Planet terbesar di tata surya?",
    options: ["Bumi", "Jupiter", "Mars", "Venus"],
    answer: 1,
  },
  {
    q: "Bintang terdekat dari Bumi?",
    options: ["Sirius", "Matahari", "Alpha Centauri", "Betelgeuse"],
    answer: 1,
  },
  {
    q: "Planet merah disebut?",
    options: ["Mars", "Saturnus", "Neptunus", "Merkurius"],
    answer: 0,
  },
];

let currentQuestion = 0;
let score = 0;
let timer;
let timeLeft = 15;
let userAnswers = [];

function startTimer() {
  clearInterval(timer);
  timeLeft = 15;
  timerDisplay.textContent = timeLeft;
  timer = setInterval(() => {
    timeLeft--;
    timerDisplay.textContent = timeLeft;
    if (timeLeft <= 0) {
      clearInterval(timer);
      saveProgress();
      nextQuestion();
    }
  }, 1000);
}

function loadQuestion(index) {
  const q = questions[index];
  questionContainer.innerHTML = `
    <h3>${q.q}</h3>
    ${q.options
      .map(
        (opt, i) => `
      <label>
        <input type="radio" name="answer" value="${i}" ${
          userAnswers[index] == i ? "checked" : ""
        }>
        ${opt}
      </label><br>
    `
      )
      .join("")}
  `;
  startTimer();
}

function saveProgress() {
  localStorage.setItem(
    "quizProgress",
    JSON.stringify({
      currentQuestion,
      score,
      userAnswers,
    })
  );
}

function nextQuestion() {
  checkAnswer();
  if (currentQuestion < questions.length - 1) {
    currentQuestion++;
    loadQuestion(currentQuestion);
  } else {
    showFinalScore();
  }
}

function prevQuestion() {
  if (currentQuestion > 0) {
    currentQuestion--;
    loadQuestion(currentQuestion);
  }
}

function checkAnswer() {
  const selected = document.querySelector('input[name="answer"]:checked');
  if (selected) {
    const answer = parseInt(selected.value);
    userAnswers[currentQuestion] = answer;
  }
}

function calculateScore() {
  score = userAnswers.reduce(
    (acc, ans, idx) => (ans === questions[idx].answer ? acc + 1 : acc),
    0
  );
  scoreDisplay.textContent = score;
}

function showFinalScore() {
  clearInterval(timer);
  calculateScore();
  questionContainer.innerHTML = "";
  finalScore.textContent = `Selesai! Skor akhir kamu: ${score}/${questions.length}`;
  finalScore.classList.remove("hidden");
}

loginBtn.addEventListener("click", () => {
  const username = usernameInput.value.trim();
  if (username) {
    userDisplay.textContent = username;
    loginScreen.classList.add("hidden");
    quizContainer.classList.remove("hidden");
    loadQuestion(currentQuestion);
  }
});

nextBtn.addEventListener("click", () => {
  saveProgress();
  nextQuestion();
});
prevBtn.addEventListener("click", () => {
  saveProgress();
  prevQuestion();
});
restartBtn.addEventListener("click", () => {
  localStorage.removeItem("quizProgress");
  currentQuestion = 0;
  userAnswers = [];
  score = 0;
  scoreDisplay.textContent = score;
  finalScore.classList.add("hidden");
  loadQuestion(currentQuestion);
});
loadBtn.addEventListener("click", () => {
  const progress = JSON.parse(localStorage.getItem("quizProgress"));
  if (progress) {
    currentQuestion = progress.currentQuestion;
    score = progress.score;
    userAnswers = progress.userAnswers;
    scoreDisplay.textContent = score;
    finalScore.classList.add("hidden");
    loadQuestion(currentQuestion);
  }
});
submitBtn.addEventListener("click", () => {
  saveProgress();
  showFinalScore();
});
