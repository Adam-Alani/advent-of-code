use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn main() {
    puzzle1();
    puzzle2();
}


fn puzzle1() {

    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);
  
  
    let mut depth = 0;
    let mut position = 0;
  
    for (_, line) in reader.lines().enumerate() {

      let line = line.unwrap();
      let parsed_line:Vec<&str> = line.split(" ").collect();
      let dir = parsed_line[0];
      let intensity = parsed_line[1].parse::<i32>().unwrap();

      match dir {
        "forward" => {
          position += intensity;
        }
        "up" => {
          depth -= intensity;
        }
        "down" => {
          depth += intensity;
        }
        _ => {
          println!("Error: {}", dir);
        }
      }
    }
    println!("{}", depth * position);

}

fn puzzle2() {

    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);
  
  
    let mut depth = 0;
    let mut position = 0;
    let mut aim = 0;
  
    for (_, line) in reader.lines().enumerate() {

      let line = line.unwrap();
      let parsed_line:Vec<&str> = line.split(" ").collect();
      let dir = parsed_line[0];
      let intensity = parsed_line[1].parse::<i32>().unwrap();

      match dir {
        "forward" => {
          position += intensity;
          depth += aim * intensity;
        }
        "up" => {
          aim -= intensity;
        }
        "down" => {
          aim += intensity;
        }
        _ => {
          println!("Error: {}", dir);
        }
      }
    }
    println!("{}", depth * position);

}