use std::cmp;

/**
# Examples:
```
let result = algorithms::rec_int_mult(5, 5);
assert_eq!(result, 25);
```
```
let result = algorithms::rec_int_mult(25, 20);
assert_eq!(result, 500);
```
*/
pub fn rec_int_mult(x: i32, y: i32) -> i32 {
    
    let n = cmp::max(
        (x as f32).log10().floor() as usize,
        (y as f32).log10().floor() as usize,
    ) + 1 as usize;
    
    let prod: i32;

    if n == 1 || x == 0 || y == 0{
        prod = x * y;
    } else {
        let mid: usize = n as usize / 2;
        let x_str = x.to_string();
        let y_str = y.to_string();

        let a: i32 = x_str[0..mid].parse::<i32>().unwrap(); // first half of x
        let b: i32 = x_str[mid..n].parse::<i32>().unwrap(); // second half of x

        let c = y_str[0..mid].parse::<i32>().unwrap(); // first half of y
        let d = y_str[mid..n].parse::<i32>().unwrap(); // second half of y

        let ac = rec_int_mult(a, c);
        let ad = rec_int_mult(a, d);
        let bc = rec_int_mult(b, c);
        let bd = rec_int_mult(b, d);

        prod = i32::pow(10, n as u32) as i32 * ac + i32::pow(10, (n / 2) as u32) * (ad + bc) + bd;
    }

    return prod;
}

fn karatsuba(x: i32, y: i32) -> i32 {
    
    let n = cmp::max(
        (x as f32).log10().floor() as usize,
        (y as f32).log10().floor() as usize,
    ) + 1 as usize;
    
    let prod: i32;

    if n == 1 {
        prod = x * y;
    } else {
        let mid: usize = n as usize / 2;
        let x_str = x.to_string();
        let y_str = y.to_string();

        let a: i32 = x_str[0..mid].parse::<i32>().unwrap(); // first half of x
        let b: i32 = x_str[mid..n].parse::<i32>().unwrap(); // second half of x

        let c = y_str[0..mid].parse::<i32>().unwrap(); // first half of y
        let d = y_str[mid..n].parse::<i32>().unwrap(); // second half of y

        let p = a + b;
        let q = c + d;
        
        let ac = karatsuba(a, c);
        let bd = karatsuba(b, d);
        let pq = karatsuba(p, q);

        let adbc = pq - ac - bd;

        prod = i32::pow(10, n as u32) as i32 * ac + i32::pow(10, (n/2) as u32) as i32 * adbc + bd;

    }   

    return prod;

}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rec_int_mult_large_int_x_1000_y_2000() {
        assert_eq!(rec_int_mult(1000, 2000), 2000000);
    }

    #[test]
    fn test_rec_int_mult_large_int_x_1000_y_2001() {
        assert_eq!(rec_int_mult(1000, 2001), 2001000);
    }

    #[test]
    fn test_karatsuba_mult_5_5() {
        assert_eq!(karatsuba(5, 5), 25);
    }

    #[test]
    fn test_karatsuba_mult_25_25() {
        assert_eq!(karatsuba(25, 25), 625);
    }

    #[test]
    fn test_karatsuba_mult_2500_2500() {
        assert_eq!(karatsuba(2500, 2500), 6250000);
    }
}

