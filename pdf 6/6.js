function evalNumbers(x, y, operation) {
    switch (operation) {
        case "add":
            return eval(`x + y`);

        case "subtract":
            return eval(`x - y`);

        case "multiply":
            return eval(`x * y`);

        case "divide":
            return eval(`x / y`);

        case "modulus":
            return eval(`x % y`);

        default:
            return "enter valid operation";
    }
}

document.write(`add --> ${evalNumbers(5,23,"add")}<br>`);
document.write(`subtract --> ${evalNumbers(5,23,"subtract")}<br>`);
document.write(`multiply --> ${evalNumbers(5,23,"multiply")}<br>`);
document.write(`divide --> ${evalNumbers(5,23,"divide")}<br>`);
document.write(`modulus --> ${evalNumbers(5,23,"modulus")}<br>`);
document.write(`wrong --> ${evalNumbers(5,23,"wrong")}<br>`);


