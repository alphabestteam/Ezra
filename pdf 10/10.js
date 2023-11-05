const bobMap = new Map([
    ['Main character', 'spongebob'],
    ['Best friend', 'patrick'],
    ['pet', 'gary'],
    ['word buddy', 'squidward'],
    ['manager', 'Mr. Krabs'],
    ['teacher', 'Mrs. Puff'],
    ['location', 'bikini bottom']
]);

// 1
console.log(bobMap);

// 2 
console.log(bobMap.keys());

// 3
console.log(bobMap.get('location'));

// 4
console.log(bobMap.size);

// 5
bobMap.delete("location");

// 6
console.log(bobMap.size);

// 7 
console.log(bobMap);

// 8 
console.log(bobMap.has('location'));
