const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
    if (fuelLeft * literPerKm === distance) return true;
    else return false;
}

alert(isSufficientFuel(6, 3, 2));
