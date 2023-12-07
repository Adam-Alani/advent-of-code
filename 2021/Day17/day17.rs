const MIN_X: i32 = 155;
const MAX_X: i32 = 215;
const MIN_Y: i32 = -132;
const MAX_Y: i32 = -72;

fn main() {
  let mut max = Vec::new();
  for x in 0..=MAX_X {
    for y in MIN_Y..1000 {
      let new_max = simulate(x, y);
      if new_max != std::i32::MIN {
        max.push(new_max);
      }
    }
  }
  println!("{} {}", *max.iter().max().unwrap(), max.len());
}

fn simulate(mut x:i32, mut y:i32) -> i32 {
  let (mut dx, mut dy) = (0, 0);
  let mut highest :i32 = 0;
  loop {
    dx += x;
    dy += y;
    if dy > highest { highest = dy }

    x -= x.signum();
    y -= 1;
    match (MIN_X <= dx && dx <= MAX_X, MIN_Y <= dy && dy <= MAX_Y) {
      (true, true) => return highest,
      (false, _) if x == 0 => return std::i32::MIN,
      (_, false) if y < 0 && dy < MIN_Y => return std::i32::MIN,
      _ => {},
    }
  }
}