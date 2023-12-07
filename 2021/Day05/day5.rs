use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::cmp;

fn main () {
    let lines = parse_coordinates();
    puzzle1(&lines);
    puzzle2(&lines);
}

struct Line {
    x1: usize,
    y1: usize,
    x2: usize,
    y2: usize,
}

impl Line {
    fn parse(input: &str) -> Option<Line> {
        let (x1 , input) = input.split_once(',')?;
        let (y1 , input) = input.split_once(" -> ")?;
        let (x2 , y2)    = input.split_once(',')?;

        Some(Line {
            x1: x1.parse().ok()?,
            y1: y1.parse().ok()?,
            x2: x2.parse().ok()?,
            y2: y2.parse().ok()?,
        })
    }
}

fn parse_coordinates() -> Vec<Line> {
    let file = File::open("./input.txt").expect("file not found");
    let reader = BufReader::new(file);

    let mut lines:Vec<Line> = Vec::new();

    reader.lines().for_each(|line| {
        let line = line.unwrap();
        let line = Line::parse(&line);
        if let Some(line) = line { lines.push(line) }
    });
    return lines;
}

fn puzzle1(lines: &Vec<Line>) -> (Vec<Vec<i32>>, i32) {

    let xmax = lines.iter().map(|l| cmp::max(l.x2, l.x1)).max().unwrap() + 1;    
    let ymax = lines.iter().map(|l| cmp::max(l.y2, l.y1)).max().unwrap() + 1;

    let mut grid: Vec<Vec<i32>> = vec![vec![0; xmax]; ymax];
    let mut res = 0;
    
    lines.iter().for_each(|line| {
        if line.x1 == line.x2 || line.y1 == line.y2 {        
            for x in cmp::min(line.x1,line.x2 )..cmp::max(line.x1,line.x2)+1 {
                for y in cmp::min(line.y1, line.y2)..cmp::max(line.y1 , line.y2)+1 {
                    grid[y][x] += 1;
                    if grid[y][x] == 2 { res += 1 }
                }
            }   
        }
    });
    println!("{}", res);
    return (grid, res);
}

fn puzzle2(lines: &Vec<Line>) {
    let (mut grid, mut res) = puzzle1(lines);

    lines.iter().for_each(|line| {
        if line.x1 != line.x2 && line.y1 != line.y2 {        
            let dir_x = (line.x2 as i32 - line.x1 as i32).signum();
            let dir_y = (line.y2 as i32 - line.y1 as i32).signum();

            let max = (line.x2 as i32 - line.x1 as i32).abs() as usize + 1;
            let (mut x, mut y) = (line.x1 as i32, line.y1 as i32);
            for _ in 0..max {
                grid[y as usize][x as usize] += 1;
                if grid[y as usize][x as usize] == 2 { res += 1 }
                x += dir_x;
                y += dir_y;
            }
        } 
    });
    println!("{}", res);
}