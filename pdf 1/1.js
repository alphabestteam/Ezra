let find, going_to_find, missing = true, not_left = true;
while (not_left) {
    alert("patrick is missing! go find him");

    going_to_find = confirm("are you going to find him?");
    if (going_to_find === true) {
        alert("bob is going to look for patrick!!");
        not_left = false
    }
}

while (missing) {
    find = prompt("did you find patrick?");
    if (find === "yes") {
        alert("bob found patrick!");
        missing = false
    }
}
