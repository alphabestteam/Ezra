/*3*/ const main_heading = document.getElementById('main-heading');

/*4*/ console.log(main_heading.id);
/*5*/ console.log(main_heading.className);
/*6*/ console.log(main_heading.classList);
/*7*/ console.log(main_heading.dataset);
/*8*/ console.log(main_heading.getAttribute('nonStandard'));
      console.log(main_heading.classList.add('border','bg-lightcyan'));

/*9*/ let content = main_heading.textContent;
      console.log(content);
/*10*/ console.log(content.trim());

/*11*/ content = main_heading.textContent = "Hello there pearl!";

/*12*/ const lineBreak = document.createElement('br');
       const spanElement = document.createElement('span');
       const addSentence = document.createTextNode(`it's me SpongeBob!`);

       main_heading.appendChild(lineBreak);
       // adding the text to a span element first.
       spanElement.appendChild(addSentence);
       main_heading.appendChild(spanElement);


/*13*/ console.log(main_heading);

/*14*/ const cloned = main_heading.cloneNode(true);
       console.log(cloned);

/*15*/ const subHeading = document.createElement('h2');
       subHeading.textContent = "jellyfish hunting is the best";

/*16*/ document.body.appendChild(subHeading);

/*17*/ const lorem_ipsum ="Lorem ipsum dolor sit amet consectetur adipisicing elit." +
                "Labore eum, earum deserunt numquam quis explicabo. Delectus" +
                "id, cum voluptate dicta aperiam sunt voluptatum quis eaque" +
                "aliquam distinctio reiciendis iste minima?";

/*18*/ lorem_arr = lorem_ipsum.split(" ");
console.log(lorem_arr);
