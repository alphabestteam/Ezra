function helloWorld() {
    return "Hello World";
}

function helloName(name) {
    return "Hello " + name;
}

const sqrt = value => value ** 2;

const area = (length, width) => length * width;

const circle = (radius) => [2 * Math.PI * radius, Math.PI * radius ** 2];

const vowelsInWord = (word) => {
    let counter = 0;
    for (letter of word) {
        if (letter.toUpperCase() === 'A' || letter.toUpperCase() === 'E' || letter.toUpperCase() === 'I' || letter.toUpperCase() === 'O' || letter.toUpperCase() === 'U') {
            counter++;
        }
    }
    return counter;
}

const isSameLength = (arr1, arr2) => arr1.length == arr2.length;

const numberToArray = (arr) => arr.toString().split('').map(Number);




console.log(helloWorld());
console.log(helloName('ezra'));
console.log(sqrt(4));
console.log(area(3, 5));
console.log(circle(1));
console.log(vowelsInWord('what do we think'));
console.log(isSameLength([1,2,3],[3,4,5,5]));
console.log(numberToArray(123123));




