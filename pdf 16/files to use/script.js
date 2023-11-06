const addEvent = () => {
    let counter = 0;
    const raiseCounter = () => {
        // i'm assuming that you don't want me to use getElementById('counter-display')...
        counter += 1;
        document.getElementById('counter-display').textContent = counter;
    }

    const btn = document.getElementById('my-button');
    btn.addEventListener('click', raiseCounter);

}
addEvent();