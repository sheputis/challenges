use std::fs::read_to_string;
use std::path::PathBuf;
use std::time::Instant;

fn compare_partitions(string: &String, size: i64, n_partitions: i64) -> bool {
    let partition_size: usize = size as usize / n_partitions as usize;
    let partition: &str = &string[0..partition_size];
    for k in 1..n_partitions as usize {
        let start = k * partition_size;
        let end = start + partition_size;
        if partition != &string[start..end] {
            return false;
        };
    }
    true
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let start = Instant::now();
    let path: PathBuf = "./input.txt".into();
    let input_string = read_to_string(path)?;

    let mut total_sum: i64 = 0;
    for range in input_string.split(",") {
        let (start_str, end_str) = range.trim().split_once("-").unwrap();
        let (start, end) = (
            start_str.trim().parse::<i64>().unwrap(),
            end_str.trim().parse::<i64>().unwrap(),
        );
        for i in start..=end {
            let i_str = i.to_string();
            let i_len = i_str.len() as i64;

            for nr_partitions in 2..=i_len {
                if i_len % nr_partitions == 0 {
                    if compare_partitions(&i_str, i_len, nr_partitions) {
                        total_sum += i as i64;
                        break;
                    }
                }
            }
        }
    }
    println!("Took: {:?}", start.elapsed()); // it takes consistently about 1 second.
    println!("{:?}", total_sum);
    Ok(())
}
