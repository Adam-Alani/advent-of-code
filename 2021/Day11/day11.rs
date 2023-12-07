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
    let mut e_levels: Vec<Vec<i32>> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        let row: Vec<i32> = line.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        e_levels.push(row);
    }
    return e_levels;
}

fn simulate(board: &mut Vec<Vec<i32>>) -> usize {
    for row in board.iter_mut() {
        for e in row.iter_mut() { *e += 1 }}

    let mut queue: Vec<(i32, i32)> = Vec::new();
    for (i, row) in board.iter().enumerate() {
        for (j, e) in row.iter().enumerate() {
            if *e > 9 { queue.push((i as i32, j as i32)) }
        }
    }

    let mut visited: Vec<Vec<bool>> = vec![vec![false; board[0].len()]; board.len()];
    while !queue.is_empty() {
        let (x, y) = queue.pop().unwrap();
        if !visited[x as usize][y as usize] {
            visited[x as usize][y as usize] = true;
            let neighbours = vec![(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)];
            for (i, j) in neighbours {
                if i < 0 || j < 0 || (i as usize) >= board.len() || (j as usize) >= board[i as usize].len() {
                    continue;
                }
                board[i as usize][j as usize] += 1;
                if board[i as usize][j as usize] > 9 { queue.push((i, j)) }
            }
        }
    }

    for row in board.iter_mut() {
        for e in row.iter_mut() {
            if *e > 9 { *e = 0 }
        }
    }
    return visited.iter().map(|row| row.iter().filter(|e| **e).count()).sum();
}

fn puzzle1() {
    let mut board = parse_input();
    println!("{}", std::iter::repeat_with(|| simulate(&mut board)).take(100).sum::<usize>());
}

fn puzzle2() {
    let mut board = parse_input();
    let mut res = 0;
    loop {
        let sum = simulate(&mut board);
        res += 1;
        if sum == 100 { break }
    }
    println!("{}", res);
}