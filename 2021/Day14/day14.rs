use std::collections::HashMap;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    simulate(10);
    simulate(40);
}
static START: &str = "VNVVKSNNFPBBBVSCVBBC";

fn simulate(n : usize) {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);
    let instructions = reader.lines().map(|l| {
        let lines = l.unwrap();
        let (source, target) = lines.split_once(" -> ").unwrap();
        return ((source.as_bytes()[0] as char, source.as_bytes()[1] as char), target.as_bytes()[0] as char)
    }).collect::<HashMap<_,_>>();

    let mut polymer = HashMap::new();
    for i in START.chars().collect::<Vec<_>>().windows(2) {
        *polymer.entry((i[0], i[1])).or_default() += 1;
    }

    for _ in 0..n {
        let mut new_polymer = HashMap::<(char, char), usize>::new();
        for (k, v) in polymer.iter() {
            if instructions.contains_key(k) {
                *new_polymer.entry((k.0, instructions[k])).or_default() += v;
                *new_polymer.entry((instructions[k], k.1)).or_default() += v;
            }
        }
        polymer = new_polymer;
    }

    let mut count = HashMap::<char, usize>::new();
    for (k, v) in polymer.iter() {
        *count.entry(k.0).or_default() += v;
    }
    *count.entry(START.chars().last().unwrap()).or_default() += 1;
    let max = count.iter().max_by_key(|(_, v)| *v).unwrap();
    let min = count.iter().min_by_key(|(_, v)| *v).unwrap();
    println!("{}", max.1 - min.1);
}