use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    puzzle1();
    puzzle2();
}

fn parse_input() -> Vec<Vec<i32>> {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);

    let mut h_map: Vec<Vec<i32>> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        let row: Vec<i32> = line.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();

        h_map.push(row);
    }
    return h_map;
}

fn is_low_point(h_map: &Vec<Vec<i32>>, i:i32, j:i32, val: i32) -> bool {
    let neighbours = vec![
        (i-1, j),
        (i, j-1),
        (i, j+1),
        (i+1, j),
    ];
    for (i, j) in neighbours {
        if i < 0 || j < 0 || (i as usize) >= h_map.len() || (j as usize) >= h_map[i as usize].len() {
            continue;
        }
        if h_map[i as usize][j as usize] <= val {
            return false;
        }
    }
    return true;
}
fn puzzle1() {
    let h_map = parse_input();
    let mut res = 0;
    for i in 0..h_map.len() {
        for j in 0..h_map[i].len() {
            if is_low_point(&h_map, i as i32, j as i32, h_map[i][j]) {
                res += 1 + h_map[i][j];
            }
        }
    }
    println!("{}", res);
}

fn calculate_basin(h_map: &Vec<Vec<i32>>, i:i32, j:i32) -> i32 {
    let mut visited: Vec<Vec<bool>> = vec![vec![false; h_map[0].len()]; h_map.len()];
    visited[i as usize][j as usize] = true;

    let mut queue: Vec<(i32, i32)> = Vec::new();
    queue.push((i, j));

    let mut res = 0;
    while !queue.is_empty() {
        let (i, j) = queue.pop().unwrap();
        let neighbours = vec![
            (i-1, j),
            (i, j-1),
            (i, j+1),
            (i+1, j),
        ];
        for (i, j) in neighbours {
            if i < 0 || j < 0 || (i as usize) >= h_map.len() || (j as usize) >= h_map[i as usize].len() {
                continue;
            }
            if !visited[i as usize][j as usize] && h_map[i as usize][j as usize] < 9 {
                visited[i as usize][j as usize] = true;
                queue.push((i, j));
            }
        }
        res += 1;

    }
    return res;
}

fn puzzle2() {
    let h_map = parse_input();
    let mut res:Vec<i32> = Vec::new();
    for i in 0..h_map.len() {
        for j in 0..h_map[i].len() {
            if is_low_point(&h_map, i as i32, j as i32, h_map[i][j]) {
                res.push(calculate_basin(&h_map, i as i32, j as i32));
            }
        }
    }
    let mut res_sorted = res.clone();
    res_sorted.sort();
    res_sorted.reverse();
    println!("{}", res_sorted[0] * res_sorted[1] * res_sorted[2]);
}