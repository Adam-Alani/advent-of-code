use std::fs;

fn main() {
    puzzle1();
    puzzle2();
}

fn parse_input() -> Vec<i32>  {
    return fs::read_to_string("./input.txt").unwrap().split(",").filter_map(|w| w.parse().ok()).collect();
}

fn solve(lambda: fn(x: i32) -> i32) {
    let input = parse_input();

    let lowest = *input.iter().min().unwrap() ;
    let highest = *input.iter().max().unwrap() ;

    let mut min = 1000000000;
    for i in lowest..=highest {
        let mut curr_sum = 0;
        for crab in input.iter() {
            curr_sum += lambda((crab-i).abs());
        }
        if curr_sum < min { min = curr_sum}
    }
    println!("{}", min);
}

fn puzzle1() {
    solve(|x| x);
}
fn puzzle2() {
    solve(|x| x*(x+1)/2);
}
