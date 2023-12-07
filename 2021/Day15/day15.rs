use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::collections::BinaryHeap;

fn main() {
    let board = parse_input();
    djistra(&board);

    let mut big = vec![vec![0; 5 * board.len()]; 5 * board[0].len()];
    for i in 0..5 {
        for j in 0..5 {
            for x in 0..board.len() {
                for y in 0..board[x].len() {
                    let mut cell = board[x][y] + i + j;
                    if cell > 9 {cell -= 9}
                    big[i as usize * board.len() + x][j as usize * board[x].len() + y] = cell;
                }
            }
            
        }
    }
    djistra(&big.to_vec());
}

fn parse_input() -> Vec<Vec<i32>> {
    let file = File::open("./input.txt").unwrap();
    let reader = BufReader::new(file);
    let mut board: Vec<Vec<i32>> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();
        let row: Vec<i32> = line.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        board.push(row);
    }
    return board;
}

fn djistra(board: &Vec<Vec<i32>>) {

    let mut dist = vec![vec![i32::MAX; board[0].len()]; board.len()];
    let mut queue = BinaryHeap::new();
    queue.push((0, 0, 0));
    dist[0][0] = 0;
    
    while let Some((cost,x, y)) = queue.pop() {
        if x == (board.len() - 1) as i32 && y == (board[0].len() - 1) as i32 { 
            println!("{}", -cost);
         }
        if -cost > dist[x as usize][y as usize] { continue }
        for (dx, dy) in &[(-1, 0), (1, 0), (0, -1), (0, 1)] {
            let nx = x as i32 + dx;
            let ny = y as i32 + dy;
            if nx < 0 || nx >= board.len() as i32 || ny < 0 || ny >= board[0].len() as i32 {
                continue;
            }
            let new_cost = -cost + board[nx as usize][ny as usize];
            if new_cost < dist[nx as usize][ny as usize] {
                queue.push((-new_cost,nx, ny));
                dist[nx as usize][ny as usize] = new_cost;
            }
        }
    }
}

