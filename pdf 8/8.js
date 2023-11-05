/* 
1.  the difference between Arr[index] and arr.at(index),
    is that if you want to access the objects from the end
    in Arr[index] you would need to subtract from the length of the array,
    Arr[Arr.length - 1], while in arr.at(index) you can just write arr.at(-1).
*/

function getChar(number, letter) {
    if (typeof number != 'number') {
        return "enter valid number";
    }
    const arr = [];
    for (let i = 0; i < number; i++) {
        arr.push(letter);
    }
    return arr;
}

document.write(getChar(h, 'A'));