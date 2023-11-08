/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }
*/

async function project() {
  const setupMenu = fetch("http://localhost:8000/menu")
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("loader").style.display = "none";
      const menuDiv = document.getElementById("menu");
      console.log(data);
      const updateCart = (amount, price) => {
        console.log(amount, price);
      };
      for (key in data) {
        // console.log(typeof data[key]);
        if (typeof data[key] === "object") {
          for (nestedKey in data[key]) {
            // console.log(typeof data[key][nestedKey]);
            const itemData = data[key][nestedKey];
            console.log(itemData.price);
            const span = document.createElement("span");
            span.className = "item";
            const h3 = document.createElement("h3");
            const text = document.createTextNode(
              `${itemData.name} ($${itemData.price.toFixed(2)})`
            );
            h3.append(text);
            span.append(h3);
            menuDiv.append(span);

            const p = document.createElement("p");
            const pText = document.createTextNode(itemData.description);
            p.append(pText);
            span.append(p);

            const label = document.createElement("label");
            const input = document.createElement("input");
            input.setAttribute("type", "number");
            input.setAttribute("min", 0);
            input.setAttribute("max", 5);
            input.setAttribute("quantity", 0);

            input.addEventListener("change", () => {
              const amount = document.querySelector('input').value;
              console.log(amount + "change" + itemData.price);
              const textForSummary = `${
                itemData.name
              } (${amount} x $${itemData.price.toFixed(2)} = $${(
                amount * itemData.price
              ).toFixed(2)})`;
              const orderSummary = document.getElementById("order-summary");
              orderSummary.querySelector("p").textContent = textForSummary;
            });
            const lText = document.createTextNode("Quantity:");

            label.append(lText, input);
            span.append(label);
          }
        }
      }
    });
  console.log(await setupMenu);
}

project();
