use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    puzzle1();
    puzzle2();
}

fn parse_input() -> Vec<Vec<char>>  {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);

    let mut lines: Vec<Vec<char>> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        let row: Vec<char> = line.chars().collect();
        lines.push(row);
    }
    return lines;
}

fn closed_cmp (c: char) -> char {
    match c {
        '{' => '}',
        '[' => ']',
        '<' => '>',
        '(' => ')',
        _ => ' ',
    }
}

fn get_score (c:char) -> i32 {
    match c {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137, 
        _ => 0,
    }
}

fn auto_score (c:char) -> i128 {
    match c {
        ')' => 1,
        ']' => 2,
        '}' => 3,
        '>' => 4,
        _ => 0,
    }
}

fn puzzle1() {
    let brackets = parse_input();
    let mut score = 0;
    for bracket in brackets {
        let mut stack: Vec<char> = Vec::new();
        for c in bracket {
            if closed_cmp(c) != ' ' {
                stack.push(c);
            } else {
                let last = stack.pop();
                if last.is_some() && closed_cmp(last.unwrap()) != c {
                    score += get_score(c);
                    break;
                }
            }
        }
    }   
    println!("{}", score);     
}

fn puzzle2() {
    let brackets = parse_input();
    let mut scores: Vec<i128> = Vec::new();
    for bracket in brackets {
        let mut stack: Vec<char> = Vec::new();
        let mut incomplete = true;
        for c in bracket {
            if closed_cmp(c) != ' ' {
                stack.push(c);
            } else {
                let last = stack.pop();
                if last.is_some() && closed_cmp(last.unwrap()) != c {
                    incomplete = false;
                    break;
                }
            }
        }
        if incomplete {
            let mut score:i128 = 0;
            for c in stack.iter().rev() {
                score = score * 5 + auto_score(closed_cmp(*c));
            }
            scores.push(score);
        }
    }
    scores.sort();
    println!("{}", scores[scores.len()/2]);
}