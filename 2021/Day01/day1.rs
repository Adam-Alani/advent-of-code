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


  let mut res = 0;
  let mut current = 0;

  for (_, line) in reader.lines().enumerate() {
    let line = line.unwrap();
    let num: i32 = line.parse().unwrap();

    if num > current {
      res += 1;
    }
    current = num;
  }
  println!("{}", res -1);

}


fn puzzle2() {

  let file = File::open("./input.txt").expect("file not found");
  let reader = BufReader::new(file);

  let lines: Vec<i32> = reader
  .lines()
  .map(|line| line.unwrap().parse::<i32>().unwrap())
  .collect();

  let mut res = 0;
  let mut current = 0;

  for i in 0..lines.len() - 2 {
    let num: i32 = lines[i] + lines[i+1] + lines[i+2];

    if num > current {
      res += 1;
    }
    current = num;
  }

  println!("{}", res -1);
}