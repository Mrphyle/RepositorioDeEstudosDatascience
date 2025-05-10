function sum(n1,n2) {
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    let Sum = n1+n2;
    console.log('The sum Of ' + n1 + ' and ' + n2 + ' is ' + Sum);
};
function sub(n1,n2) {
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    let Sub = n1-n2;
    console.log('The substraction Of ' + n1 + ' and ' + n2 + ' is ' + Sub);
}
function mul(n1,n2) {
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    let Mul = n1*n2;
    console.log('The multiplication Of ' + n1 + ' and ' + n2 + ' is ' + Mul);
}
function div(n1,n2) {
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    let Div = n1/n2;
    console.log('The division Of ' + n1 + ' and ' + n2 + ' is ' + Div);
}
function euation2grade(a,b,c) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    let delta = b*b - 4*a*c;
    if (delta > 0) {
        let x1 = (-b + Math.sqrt(delta)) / (2 * a);
        let x2 = (-b - Math.sqrt(delta)) / (2 * a);
        console.log('The equation has two real roots: ' + x1 + ' and ' + x2);
    } else if (delta == 0) {
        let x = -b / (2 * a);
        console.log('The equation has one real root: ' + x);
    } else {
        console.log('The equation has no real roots');
    }

}
sum(10,20);
sub(20,10);
mul(10,20);
div(20,10);
euation2grade(1, -3, 2);
