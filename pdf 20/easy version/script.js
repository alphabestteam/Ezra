const quotes = [
  "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
  "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
  "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
  "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
  "The inner machinations of my mind are an enigma. - Patrick Star",
  "I can't hear you, it's too dark in here! - Patrick Star",
  "I'm ugly and I'm proud! - SpongeBob SquarePants",
  "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
  "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
  "Is mayonnaise an instrument? - Patrick Star",
  "Can you give SpongeBob his brain back? - Patrick Star",
  "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
  "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
  "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
  "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
  "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
  "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
  "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
  "SpongeBob: Can I be excused for the rest of my life?",
  "SpongeBob: I'm not just ready, I'm ready Freddy!",
  "SpongeBob: You don't need a license to drive a sandwich.",
  "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
  "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
  "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
  "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end.",
];

let isFunctionEnabled = true;
let startTime = 0;
let quoteWordCount = 0;
let timeInterval;

function getRandomQuote() {
  // making sure that you can only play once.
  if (isFunctionEnabled) {
    const randomQuote = Math.floor(Math.random() * quotes.length);
    isFunctionEnabled = false;
    return quotes[randomQuote];
  } else {
    return;
  }
}

function startGame() {
  // starting timer
  startTime = Date.now();
  timeInterval = setInterval(() => {
    document.getElementById("timer").textContent = `Time: ${Math.round(
      (Date.now() - startTime) / 1000
    )}s`;
  }, 1000);

  // getting and formatting the quote
  let quote = getRandomQuote();
  quoteWordCount = quote.split(" ").length;
  let quoteArr = quote.split("");
  quoteArr.forEach((element) => {
    const span = document.createElement("span");
    span.classList.add("span-letter");
    const node = document.createTextNode(element);
    span.append(node);
    document.getElementById("quote").appendChild(span);
  });

  // getting input and adding an event listener
  const input = document.getElementById("input");
  input.addEventListener("input", () =>
    checkInput(input.value.split(""), quoteArr)
  );
}

function checkInput(inputArr, quoteArr) {
  // starting up the checking function
  const spanElm = document.getElementsByTagName("span"); // span list of all letters in the quote

  function checkEndGame() {
    if (inputArr.length === quoteArr.length) {
      endGame(inputArr, quoteArr);
    }
  }

  // iterating over all the letters to see if they match.
  for (let i = 0; i < inputArr.length; i++) {
    if (inputArr[i] === quoteArr[i]) {
      // meaning we deleted an error and have fixed it.
      if (spanElm[i].dataset.customVar === "incorrect") {
        spanElm[i].className = "light-yellow";
      } else {
        spanElm[i].className = "correct";
      }
    } else {
      spanElm[i].className = "incorrect";
      spanElm[i].dataset.customVar = "incorrect"; // in a case where you make a backspace. to remember for the yellow
    }
  }
  // coloring all rest of letters dark.
  for (let y = inputArr.length; y < quoteArr.length; y++) {
    spanElm[y].className = "dark";
  }
  checkEndGame();
}

// counts how many characters are the same.
function countMatchingChars(inputArr, quoteArr) {
  let correct = 0;
  for (let i = 0; i < inputArr.length; i++) {
    if (inputArr[i] === quoteArr[i]) {
      correct++;
    }
  }
  return [correct, inputArr.length];
}

function endGame(inputArr, quoteArr) {
  // stops timer
  clearInterval(timeInterval);
  let timeTaken = Date.now() - startTime;

  //disabled input field
  document.getElementById("input").disabled = true;

  // break
  var br = document.createElement("br");

  // getting result area
  const result = document.getElementById("result");

  // amount of words
  const words = quoteWordCount;
  const wordsText = `you typed ${words} words`;

  // how many seconds
  const time = (timeTaken / 1000).toFixed(1);
  const timeText = `in ${time} seconds.`;

  // wpm
  timeMin = timeTaken / 1000 / 60;
  const wmp = Math.round(quoteWordCount / timeMin);
  const wpmText = `Your speed is ${wmp} wpm.`;

  // accuracy
  [correct, length] = countMatchingChars(inputArr, quoteArr);
  const accuracy = Math.round((correct / length) * 100);
  const accuracyText = `with ${accuracy}% accuracy.`;

  // setting result text
  result.setAttribute("style", "white-space: pre;");
  result.textContent =
    wordsText + "\n" + timeText + "\n" + wpmText + "\n" + accuracyText;

  addToJson(words, time, wmp, accuracy);
}

function addToJson(words, time, wmp, accuracy) {
  const inputData = {
    words: words,
    time: time,
    wmp: wmp,
    accuracy: accuracy,
  };

  // getting the data
  const existingData = JSON.parse(localStorage.getItem("userData")) || []; // || [] - if the array is empty

  // adding data
  existingData.push(inputData);

  // setting data back
  localStorage.setItem("userData", JSON.stringify(existingData));

  console.log(existingData);

  createTable();
}

function createTable() {
  const container = document.getElementsByClassName("container");
  const table = document.createElement("table");
  
  const headRow = table.insertRow(0);

  const cellRank = headRow.insertCell(0);
  cellRank.textContent = "Rank";
  const cellWords = headRow.insertCell(1);
  cellWords.textContent = "Words";
  const cellTime = headRow.insertCell(2);
  cellTime.textContent = "Time";
  const cellWPM = headRow.insertCell(3);
  cellWPM.textContent = "WPM";
  const cellAccuracy = headRow.insertCell(4);
  cellAccuracy.textContent = "Accuracy";
  const cellScore = headRow.insertCell(5);
  cellScore.textContent = "Score";
  
  container.append(table);
}

// starting game
const startButton = document.getElementById("start-btn");
startButton.addEventListener("click", startGame);
document.addEventListener("keydown", (even) => {
  if (even.key === "Enter") {
    document.getElementById("input").focus();
    startGame();
  }
});
