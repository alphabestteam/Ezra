const button = document.getElementById('the-button');
// const main = document.querySelector("main");
const bobGif = document.getElementById("bob");



const toggleBob = function(){
    //implement this function
    if (bobGif.getAttribute('show-bob') == "true"){
        bobGif.style.display = 'none';
        button.textContent = "Show me Bob ;)";
        bobGif.setAttribute('show-bob', 'false');
    }
    else {
        bobGif.style.display = 'block';
        button.textContent = "Hide Bob ;)";
        bobGif.setAttribute('show-bob', 'true');

    }
    
};

button.addEventListener('click',toggleBob);
