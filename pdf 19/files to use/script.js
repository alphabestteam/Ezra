function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

questionA(); 
questionB(); 
questionC();
questionD();
// questionE();

/*
we're dealing with task managing. in general the rule is Main>microThread>callback.

questionA(); - wil return bob,sponge. because plain log is a sync function so it goes in the main task.
questionB(); - will return bob, promise b, sponge, timeout b. because bob is main, promise b is from type 
               microthread so it will go next, then will come the timeout's because they're from type callback.
questionC(); - bob, promise b, promise c, sponge, timeout b, timeout c. same idea as before but the twist is that we'd
               think that promise c will come at the end because it's a timeout (callback), but because it's inside a promise
               it run in the microthread part.

*/