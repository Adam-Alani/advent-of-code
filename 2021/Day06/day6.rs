use std::fs;

fn main() {
    println!("{}", simulate(80));
    println!("{}", simulate(256)); 
}

fn simulate(days: i16) -> u128 {
    let mut fish = parse_input();
    for _ in 0..days {
        fish[7] += fish[0];
        fish.rotate_left(1);
    }
    return fish.iter().sum();
}

fn parse_input() -> [u128; 9]  {
    let mut fish = [0;9];
    fs::read_to_string("./input.txt").unwrap().split(",").for_each(|x| {
        fish[x.parse::<usize>().unwrap()] += 1
    });
    return fish;
}
