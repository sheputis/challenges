use std::fs;
use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file_path = "./input.txt";
    let file = fs::File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let left: &str = "L";
    let mut current_number: i32 = 50;
    let mut zero_count: i32 = 0;
    for line in reader.lines() {
        let line = line?;
        let direction = &line[0..1];
        let mut number = line[1..].trim().parse::<i32>()?;

        if direction == left {
            number = - number;
        }

        current_number += number;
        current_number = current_number % 100;
        if current_number < 0 {
            current_number = 100 + current_number;
        } else if current_number == 0 {
            zero_count += 1;
        }
    }
    println!("{}", zero_count);
    Ok(())
}
