/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }
*/

async function project() {
  // async function getMenu(menuUrl) {
  //   fetch(menuUrl);
  //   // return new Promise((resolve, reject) => {
  //   //   // need to check if the link is not good.
  //   //   resolve(fetch(menuUrl));
  //   //   reject("reject error!");
  //   // });
  // }

  const abc = fetch("http://localhost:8000/menu")
  .then(res => res.json())
  .then(data => {
    document.getElementById("loader").style.display = "none";
    
    document.getElementById("menu").textContent = JSON.stringify(data);
  
  });

}

project();
