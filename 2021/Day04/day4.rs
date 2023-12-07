#![feature(drain_filter)]
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

static DRAWS:&[i32] = &[38,54,68,93,72,12,33,8,98,88,21,91,53,61,26,36,18,80,73,47,3,5,55,92,67,52,25,40,56,95,9,62,30,31,85,65,14,2,78,75,15,39,87,27,58,42,60,32,41,83,51,77,10,66,70,4,37,6,89,23,16,49,48,63,94,97,86,64,74,82,7,0,11,71,44,43,50,69,45,81,20,28,46,79,90,34,35,96,99,59,1,76,22,24,17,57,13,19,84,29];

fn main() {
    puzzle1();
    puzzle2();
}

fn parse_boards() -> Vec<Vec<Vec<i32>>> {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);

    let mut boards:Vec<Vec<Vec<i32>>> = Vec::new();
    let mut board:Vec<Vec<i32>> = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();

        if line.len() == 0 {
            boards.push(board);
            board = Vec::new();
            continue;
        }

        let row:Vec<i32> = line.split_whitespace().map(|s| s.parse().unwrap()).collect();
        board.push(row);
    }

    return boards;
}

fn bingo(board: &Vec<Vec<i32>>) -> bool {
    
    if board.iter().any(|row| row.iter().all(|&x| x < 0)) { return true }
    
    for i in 0..5 {
        let mut col = Vec::new();
        for j in 0..5 {
            col.push(board[j][i]);
        }
        if col.iter().all(|&x| x < 0) { return true }
    }

    false
}

fn count_score(board: &Vec<Vec<i32>>) -> i32 {
    let mut score = 0;
    for i in 0..5 {
        for j in 0..5 {
            if board[i][j] >= 0 { score += board[i][j] }
        }
    }
    return score;
}

fn mark_board(board : &mut Vec<Vec<i32>>, draw: i32) {
    for row in board.iter_mut() {
        if row.contains(&draw) {
            let index = row.iter().position(|&x| x == draw).unwrap();
            row[index] = -1;
        }  
    }
}

fn puzzle1(){
    let mut boards = parse_boards();
    'outer: for draw in DRAWS {
        for board in boards.iter_mut() {
            mark_board(board, *draw);
            if bingo(board) {
                println!("{}", count_score(board) * draw);
                break 'outer
            }
        }
    }  
}

fn puzzle2() {
    let mut boards = parse_boards();
    let mut found = 0;

    for draw in DRAWS {
        boards.drain_filter(|board| {
            mark_board(board, *draw);
            if bingo(board) {
                found = count_score(board) * draw;
                true
            } else { false }
        });
    }
    println!("{}", found);
}