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

function getRandomQuote() {
  //implement getting a random quote from the array.
  const randomQuote = Math.floor(Math.random() * quotes.length);
  return quotes[randomQuote];
}

function startGame() {
  /*
    1 - implement game start/restart logic 
    2 - generate a random quote and display it in the relevant html element
    2* - think carefully how to do it such that you can change the background of each char individually
    */
  let quoteArr = getRandomQuote().split("");
  quoteArr.forEach((element) => {
    const span = document.createElement("span");
    span.classList.add("span-letter");
    const node = document.createTextNode(element);
    span.append(node);
    document.getElementById("quote").appendChild(span);
  });

  const input = document.getElementById("input");

  input.addEventListener("input", (event) =>
    checkInput(input.value.split(""), quoteArr, event)
  );
}

// inputArr - array of input field. quoteArr - array of quote.
function checkInput(inputArr, quoteArr, event) {
  //implement checking input, ending the game by calling the endGame() function when needed.
  //add the relevant css class to each letter
  const spanElm = document.getElementsByTagName("span");
  let index = inputArr.length - 1;
  const inputLetter = inputArr[index],
    quoteLetter = spanElm[index].textContent;

  if (event.inputType === "deleteContentBackward") {
    spanElm[index + 1].className = "backspace";
  } else {
    if (inputLetter === quoteLetter) {
      if (spanElm[index].className === "incorrect") {
        spanElm[index].className = "light-yellow";
        console.log("almost true");
        console.log(spanElm[index]);
      } else {
        spanElm[index].className = "correct";
        console.log("true");
        console.log(spanElm[index]);
      }
    } else {
      spanElm[index].className = "incorrect";
      console.log("false");
      console.log(spanElm[index]);
    }
  }
}

function countMatchingChars(strA, strB) {
  //helper function used to calculate hits, used for percentage.
}

function endGame() {
  //stop the timer, calculate elapsed time in seconds
  //in the result element display:
  //  a) how many words were typed
  //  b) in how many seconds it was done
  //  c) the speed (wpm)
  //  d) the accuracy as percentage
}

const startButton = document.getElementById("start-btn");
startButton.addEventListener("click", startGame);
