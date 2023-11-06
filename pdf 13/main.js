const main_heading = document.getElementById('main-heading');

console.log(main_heading.id);
console.log(main_heading.className);
console.log(main_heading.classList);
console.log(main_heading.dataset);
console.log(main_heading.getAttribute('nonStandard'));
console.log(main_heading.classList.add('border','bg-lightcyan'));


console.log(main_heading.textContent);
console.log(main_heading.textContent.trim());

main_heading.textContent = "Hello there pearl!";
const span = document.createElement("span");

main_heading.textContent += "<br><span>its me SpongeBob!</span>";







