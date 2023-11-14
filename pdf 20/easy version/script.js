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
  if (isFunctionEnabled) {
    //implement getting a random quote from the array.
    const randomQuote = Math.floor(Math.random() * quotes.length);
    isFunctionEnabled = false;
    return quotes[randomQuote];
  } else {
    return;
  }
}

function startGame() {
  /*
    1 - implement game start/restart logic 
    2 - generate a random quote and display it in the relevant html element
    2* - think carefully how to do it such that you can change the background of each char individually
    */

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

// inputArr - array of input field. quoteArr - array of quote.
function checkInput(inputArr, quoteArr) {
  //implement checking input, ending the game by calling the endGame() function when needed.
  //add the relevant css class to each letter

  // starting up the checking function
  const spanElm = document.getElementsByTagName("span"); // span list of all letters in the quote
  let index = inputArr.length - 1;

  function checkEndGame() {
    // console.log("checking end game..............");
    // console.log(
    //   `input length: ${inputArr.length} \nquote length: ${quoteArr.length}`
    // );
    if (inputArr.length === quoteArr.length) {
      endGame(inputArr, quoteArr);
    }
  }

  for (let i = 0; i < inputArr.length; i++) {
    console.log(`inputarr: ${inputArr[i]} quotearr: ${quoteArr[i]}`);
    if (inputArr[i] === quoteArr[i]) {
      if (spanElm[i].dataset.customVar === "incorrect") {
        spanElm[i].className = "light-yellow";
        console.log("yellow");
        console.log(spanElm[i]);
      } else {
        spanElm[index].className = "correct";
        console.log("green");
        console.log(spanElm[i]);
      }
    } else {
      spanElm[i].className = "incorrect";
      spanElm[i].dataset.customVar = "incorrect"; // in a case where you make a backspace. to remember for the yellow
      console.log("red");
      console.log(spanElm[i]);
    }
  }
  for (let y = inputArr.length; y < quoteArr.length; y++) {
    spanElm[y].className = "dark";
  }
  checkEndGame();
}

function countMatchingChars(inputArr, quoteArr) {
  //helper function used to calculate hits, used for percentage.
  let correct = 0;
  for (let i = 0; i < inputArr.length; i++) {
    if (inputArr[i] === quoteArr[i]) {
      correct++;
    }
  }

  return [correct, inputArr.length];
}

function endGame(inputArr, quoteArr) {
  //stop the timer, calculate elapsed time in seconds
  //in the result element display:
  //  a) how many words were typed
  //  b) in how many seconds it was done
  //  c) the speed (wpm)
  //  d) the accuracy as percentage
  // clearInterval(timeInterval);
  clearInterval(timeInterval);
  let timeTaken = Date.now() - startTime;
  console.log(timeTaken);

  document.getElementById("input").disabled = true;
  var br = document.createElement("br");

  const result = document.getElementById("result");
  // checking amount of words.
  const words = document.createTextNode(`you typed ${quoteWordCount} words`);
  result.appendChild(words);
  result.appendChild(br);

  console.log(`you typed ${quoteWordCount} words`);

  // how many seconds
  const second = document.createTextNode(
    `in ${(timeTaken / 1000).toFixed(1)} seconds. \n`
  );
  result.appendChild(second);
  var br2 = document.createElement("br");

  result.appendChild(br2);

  console.log(`in ${timeTaken / 1000} seconds`);

  // wpm
  timeMin = timeTaken / 1000 / 60;
  const wpm = document.createTextNode(
    `Your speed is ${Math.round(quoteWordCount / timeMin)} wpm.`
  );
  result.appendChild(wpm);
  var br3 = document.createElement("br");

  result.appendChild(br3);

  console.log(`wpm of ${(quoteWordCount / timeMin).toFixed(2)}`);

  // accuracy
  [correct, length] = countMatchingChars(inputArr, quoteArr);
  const match = document.createTextNode(
    `with ${Math.round((correct / length) * 100)}% accuracy.`
  );
  result.appendChild(match);
  var br4 = document.createElement("br");

  result.appendChild(br4);

  console.log(
    `you hit ${correct} out of ${length} (%${((correct / length) * 100).toFixed(
      2
    )})`
  );
  
}


const startButton = document.getElementById("start-btn");
startButton.addEventListener("click", startGame);
document.addEventListener("keydown", (even) => {
  if (even.key === "Enter") {
    console.log("enter pressed");
    startGame();
  }
});
