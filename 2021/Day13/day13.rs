use std::fs;
use std::collections::HashSet;
fn main() {
    puzzle1();
    puzzle2();
}
type Point = (i32,i32);

fn parse_input() -> (Vec<Point>, Vec<(char, i32)>) {
    let input = fs::read_to_string("input.txt").unwrap();
    let (dots, folds) = input.split_once("\n--").unwrap();
    let dots: Vec<Point> = dots
        .split("\n")
        .map(|line| {
            let mut coords = line.split(",");
            (coords.next().unwrap().parse().unwrap(),coords.next().unwrap().trim().parse().unwrap())   
        })
        .collect();
    let mut folds_vec: Vec<(char, i32)> = Vec::new();
    for line in folds.trim().split("\n") {
        let coords = line.strip_prefix("fold along ").unwrap().trim();
        let (ori, val) = coords.split_once("=").unwrap();
        folds_vec.push((ori.chars().next().unwrap(), val.parse().unwrap()));
    }
    return (dots, folds_vec);
}

fn apply_fold(dots: &mut HashSet<Point>, fold:(char, i32)) {
    dots.clone().iter().filter(|p| {
        match fold.0 {
            'x' => p.0 > fold.1,
            _ => p.1 > fold.1,
        }
    }).for_each(|p| {
        dots.remove(p);
        dots.insert({
            match fold.0 {
                'x' => (2* fold.1 - p.0, p.1),
                _ => (p.0,  2*fold.1 - p.1),
            }
        });
    });
}

fn puzzle1() {
    let (dots_vec, folds) = parse_input();
    let mut dots: HashSet<Point> = dots_vec.into_iter().collect();
    apply_fold(&mut dots, folds[0]);
    println!("{}", dots.iter().count());
}
fn puzzle2() {
    let (dots_vec, folds) = parse_input();
    let mut dots: HashSet<Point> = dots_vec.into_iter().collect();
    for fold in folds {
        apply_fold(&mut dots, fold);
    }
    let xmax = dots.iter().map(|p| p.0).max().unwrap();
    let ymax = dots.iter().map(|p| p.1).max().unwrap();
    for y in 0..=ymax {
        for x in 0..=xmax {
            if dots.contains(&(x,y)) {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!();
    }
}