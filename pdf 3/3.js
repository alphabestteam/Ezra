function findSeashellsIndicies(target, values) {
    for (let x = 0; x < values.length; i++) {
        for (let y = x + 1; y < values.length; y++){
            if (values[x] + values[y] === target){
                return [x,y];
            }
        }
    }
    return [];
}

document.write(findSeashellsIndicies(30,[25, 21, 15, 10, 5]))