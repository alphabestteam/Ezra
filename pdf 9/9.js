const text = `          Kung Fu Panda is a beloved animated movie about a clumsy, \
food-loving panda named Po who dreams of becoming a kung fu master.\nPo's \
dream becomes a reality when he is unexpectedly chosen to become the \
Dragon Warrior and train with the Furious Five to protect the Valley of \
Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, \
and grossed over $631 million worldwide, making it the highest-grossing \
non-sequel animated film at the time of its release.\nAlong the way, Po \
learns valuable lessons about inner strength, perseverance, and the \
importance of family and friendship.\nWith stunning animation, a \
heartwarming story, and a star-studded cast including Jack Black, Angelina \
Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for \
all ages.       `;

// 1
const breakTextToArray = (text) => text.split('\n');
console.log(breakTextToArray(text));

// 2 
const swapWord = (text) => text.replace("movie", "film");
console.log(swapWord(text));

// 3
const swapAllWords = (text) => text.replaceAll("Panda", "Bear");
console.log(swapAllWords(text));

// 4
const upperCase = (text) => text.toUpperCase();
console.log(upperCase(text));

// 5
const lowerCase = (text) => text.toLowerCase();
console.log(lowerCase(text));

// 6
const findInstance = (text, instance) => text.indexOf(instance);
console.log(findInstance(text, "Po"));

// 7
const cutString = (text, index) => text.slice(index);
console.log(cutString(text,92));

// 8
const removeWhiteSpace = (text) => text.trim();
console.log(removeWhiteSpace(text));

// 9 
const firstInstance = breakTextToArray(cutString(text,92))[0];
console.log(firstInstance);

// 10
const breakIntoWords = (text) => text.split(" ");
console.log(breakIntoWords(removeWhiteSpace(text)));

// 11
const checkEnd = (text, value) => text.endsWith(value);
console.log(checkEnd(text, "ages.")); // will return false because the text ends with whitespaces.

// 12
const addText = (text, addedText) => text.concat(addedText);
console.log(addText(text, "is one of my favorite movies!"));

