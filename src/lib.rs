/// # Examples:
/// 
/// ```
/// let result = algorithms::rec_int_mult(1, 1);
/// assert_eq!(result, 1);
/// ```
/// ```
/// let result = algorithms::rec_int_mult(5, 5);
/// assert_eq!(result, 25);
/// ```
/// ```
/// let result = algorithms::rec_int_mult(25, 20);
/// assert_eq!(result, 500);
/// ```
pub fn rec_int_mult(x: i32, y: i32) -> i32 {
    
    let n: usize = x.to_string().len();
    let x_str = String::from(x.to_string());
    let y_str = String::from(y.to_string());
    let mid = n/2;

    let prod: i32;

    if n == 1 {
        prod = x * y;
    } else {
        let a: i32 = x_str[0..mid].parse::<i32>().unwrap(); // first half of x
        let b: i32 = x_str[mid..n].parse::<i32>().unwrap(); // second half of x

        let c = y_str[0..mid].parse::<i32>().unwrap(); // first half of y
        let d = y_str[mid..n].parse::<i32>().unwrap(); // second half of y

        let ac = rec_int_mult(a, c);
        let ad = rec_int_mult(a, d);
        let bc = rec_int_mult(b, c);
        let bd = rec_int_mult(b, d);

        prod = i32::pow(10, n as u32) as i32 * ac + i32::pow(10, (n/2) as u32) * (ad + bc) + bd;
    }


    return prod;
    
}