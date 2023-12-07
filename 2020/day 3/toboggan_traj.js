//input is very annoying

function toboggan(inputlist) {
    let total = 0;
    let xc = 3;
    for (i = 1 ; i < inputlist.length ; i++) {
        if (inputlist[i][xc] == "#") {
            total += 1;
        }
        xc = (xc + 3) % inputlist[i].length
        }
    return total;
    }

function hardcore(x ,  y) {
    let total = 0;
    let xc = x;
    for (i = y ; i < inputs.length ; i += y) {
        if (inputs[i][xc] == "#") {
            total += 1;
        }
        xc = (xc + x ) % inputs[i].length
        }
    return total;
    }

console.log(hardcore(1 , 1) * hardcore(3 , 1)* hardcore(5 , 1) * hardcore(7 , 1)* hardcore(1, 2))