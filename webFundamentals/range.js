function range(start, end, incr) {
    for (var i = start; i <= end; i = i + incr) {
        if (incr == undefined) { 
        incr = 1;
        } else if (end == undefined) {
            end = start;
            start = 0;
            console.log(i);
        } else {
            console.log(i);
        }
    }
}


range(-2, 20, 2);