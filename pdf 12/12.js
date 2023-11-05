const student1 = {
    name: `moshe`, age: 12, grade: [23, 100, 50, 70, 65], avgGrade: function () {
        let avg = 0;
        for (let i = 0; i < 5; i++) {
            avg += this.grade[i];
        }
        avg = avg / 5;
        avg += this.name.match(/[aeiou]/gi).length;
        return avg;

    }
};

const student2 = {
    name: `david`, age: 23, grade: [65, 100, 100, 90, 95], avgGrade: function () {
        let avg = 0;
        for (let i = 0; i < 5; i++) {
            avg += this.grade[i];
        }
        avg = avg / 5;
        avg += this.name.match(/[aeiou]/gi).length;
        return avg;
    }
};

const student3 = {
    name: `jack`, age: 41, grade: [100, 100, 100, 100, 95], avgGrade: function () {
        let avg = 0;
        for (let i = 0; i < 5; i++) {
            avg += this.grade[i];
        }
        avg = avg / 5;
        avg += this.name.match(/[aeiou]/gi).length;
        return avg;
    }
};

const student4 = {
    name: `joe`, age: 13, grade: [95, 80, 85, 45, 0], avgGrade: function () {
        let avg = 0;
        for (let i = 0; i < 5; i++) {
            avg += this.grade[i];
        }
        avg = avg / 5;
        avg += this.name.match(/[aeiou]/gi).length;
        return avg;
    }
};

const student5 = {
    name: `max`, age: 12, grade: [100, 54, 87, 67, 90], avgGrade: function () {
        let avg = 0;
        for (let i = 0; i < 5; i++) {
            avg += this.grade[i];
        }
        avg = avg / 5;
        avg += this.name.match(/[aeiou]/gi).length;
        return avg;

    }
};


const students = [student1, student2, student3, student4, student5];

for (let i = 0; i < students.length; i++) {
    console.log(`the index of student${i+1} is ${i}`);
    console.log(students[i]);
}

const adults = students.filter(student => student.age >= 18);
console.log(adults);



const myCar = {make: 'hyndai', make: 'i30', year: 2015, carAge: function(){
    date = new Date().getFullYear();
    return date - this.year;
}}

console.log(myCar);
console.log(`carAge: ${myCar.carAge()}`);

