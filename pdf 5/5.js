
document.getElementById("button").addEventListener("click", getScore);

function getScore() {
    let score, letter_score = ``, sentence = ``;
    score = document.getElementById("number").value;
    if (score >= 0 && score <= 100) {
        if (score == 100) { letter_score = "A+"; }
        else if (90 <= score && score <= 99) { letter_score = "A"; }
        else if (80 <= score && score <= 89) { letter_score = "B"; }
        else if (70 <= score && score <= 79) { letter_score = "C"; }
        else if (60 <= score && score <= 69) { letter_score = "D"; }
        else if (50 <= score && score <= 59) { letter_score = "E"; }
        else { letter_score = "F"; }

        switch (letter_score) {
            case "A+":
                sentence = "Perfect!";
                break;
            case "A":
                sentence = "Amazing!";
                break;
            case "B":
                sentence = "Nicely done!";
                break;
            case "C":
                sentence = "This is fine!";
                break;
            case "D":
                sentence = "You can do better!";
                break;
            case "E":
                sentence = "Moed B is an option!";
                break;
            case "F":
                sentence = "Moed B is a must!";
                break;
            default:
                sentence = "please enter in a valid score";
        }

        const para = document.createElement("h4");
        const node = document.createTextNode(`You scored a ${letter_score} ${sentence}`);
        para.appendChild(node);

        const element = document.getElementById("divs").appendChild(para);
    }
    else {
        alert("invalid number!!!");
        
    }
}
