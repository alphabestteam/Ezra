/* 
1.  the difference between Arr[index] and arr.at(index),
    is that if you want to access the objects from the end
    in Arr[index] you would need to subtract from the length of the array,
    Arr[Arr.length - 1], while in arr.at(index) you can just write arr.at(-1).
*/

const getChar = (number, letter) => {
    if (typeof number === "number") {
        const arr = [];
        for (let i = 0; i < number; i++) {
            arr.push(letter);
        }
        return arr;
    }
    else {
        return "enter valid number";
    }
}

const removeFirstNobjects = (arr, n) => {
    if (Array.isArray(arr)) {
        for (let i = 0; i < n; i++) {
            if (arr.length == 0) {
                return "removed as many objects as can";
            }
            arr.shift();
        }
        return arr;
    } else {
        return "enter valid array";
    }

    // another way to do it is with the splice() and then check if n is bigger than arr.length.
}

const addValueAtStart = (arr, n) => arr.unshift(n);

const joinArrays = (arr1, arr2) => arr1.concat(arr2);

const isIn = (arr, value) => arr.includes(value);

const biggerTrue = biggerThan10 => biggerThan10 !== undefined;


const arr = ['moshe', 'david', 'ari', '23', 5, 4, 3, 6, 4, 34, 12, 4, 6, 'nos', 23432, 'moshe', 'avi', 'david', 'benny'];
console.log('the original arr: ' + arr);

/*2.*/ console.log(getChar(6, 'A'));

/*3.*/ console.log(removeFirstNobjects(arr, 2));

/*4.*/ console.log(addValueAtStart(arr, "noy"));

/*5.*/ console.log(joinArrays([1, 2, 3, 4], arr));

/*6.*/ console.log(arr.map(n => n.toString().toUpperCase()));

/*7.*/ console.log(ddArray = arr.filter(num => num > 10));

/*8.*/ console.log("nos is in: " + isIn(arr, "noss"));

/*9.*/ biggerThan10 = arr.find(num => num > 10);
console.log(biggerThan10);

/*10.*/ console.log(`you're answer is ` + biggerTrue(biggerThan10));

/*11.*/ 



