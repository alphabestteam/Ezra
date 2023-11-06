const button = document.getElementById('the-button');
const bobGif = document.getElementById("bob");


const toggleBob = function(){
    //implement this function
    if (button.textContent == "Hide Bob ;)"){
        bobGif.style.display = 'none';
        button.textContent = "Show me Bob ;)";
    }
    else {
        bobGif.style.display = 'block';
        button.textContent = "Hide Bob ;)";
    }
    
};

button.addEventListener('click',toggleBob);
