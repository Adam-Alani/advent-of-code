use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    puzzle1();
}

fn puzzle1() {
    let signals = parse_input();
    let mut res = 0;
    for signal in signals {
        for output in signal.output {
            if output.len() == 2 || output.len() == 3 || output.len() == 4 || output.len() == 7 {
                res += 1;
            }
        }
    }
    println!("{}", res);
}

struct Signal {
    output: Vec<String>,
    pattern: Vec<String>,
}

impl Signal {
    fn parse(input: &str) -> Option<Signal> {
        let (pattern, output) = input.split_once('|')?;
        let pattern = pattern
            .split_whitespace()
            .into_iter()
            .map(str::to_owned)
            .collect();
        let output = output
            .split_whitespace()
            .into_iter()
            .map(str::to_owned)
            .collect();
        Some(Signal { output, pattern })
    }
}

fn parse_input() -> Vec<Signal> {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);
    let mut lines: Vec<Signal> = Vec::new();
    reader.lines().for_each(|line| {
        let line = line.unwrap();
        let line = Signal::parse(&line);
        if let Some(line) = line {
            lines.push(line)
        }
    });
    return lines;
}
