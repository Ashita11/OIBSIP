
function fun(a) {
    val = document.getElementById("output").value;
    if (a == '+' || a == '-' || a == '/' || a == '*') {
        if (Number.isInteger(parseInt(val.charAt(val.length - 1)))) {
            document.getElementById("output").value = val + a;
        }
    }
    else {
        document.getElementById("output").value = (val != null) ? (val + a) : (a);
    }
}

function clr() {
    document.getElementById("output").value = "";
}

function cal() {
    let val = document.getElementById("output").value;
    val = eval(val);
    document.getElementById("output").value = val
}