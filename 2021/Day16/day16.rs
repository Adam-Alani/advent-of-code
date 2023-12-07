fn main() {
  let mut transmission = parse_input();
  println!("{:?}", parse_bits(&mut transmission));
}

fn parse_bits(mut transmission:  &mut Vec<char>) -> (u64,u64) {
  let mut version_bin = String::new();

  for _ in 0..3 {
    version_bin.push(transmission.remove(0));
  }
  let mut version = u64::from_str_radix(&version_bin, 2).unwrap();

  let mut typeid_bin = String::new();
  for _ in 0..3 {
    typeid_bin.push(transmission.remove(0));
  }
  let typeID = u64::from_str_radix(&typeid_bin, 2).unwrap();

  match typeid_bin.as_str() {
    "100" => return (version,as_literal(&mut transmission)),
    "000" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;
      return (version, val.iter().sum());
    },
    "001" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;
      return (version, val.iter().product());  
    },
    "010" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;
      return (version, *val.iter().min().unwrap());
    },
    "011" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;
      return (version, *val.iter().max().unwrap());
    },
    "101" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;

      if val[0] > val[1] {
        return (version, 1);
      } else { return (version, 0) }
    },
    "110" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;

      if val[0] < val[1] {
        return (version, 1);
      } else { return (version, 0) }
    },
    "111" => {
      let (new_version, val) = as_operator(&mut transmission);
      version += new_version;

      if val[0] == val[1] {
        return (version, 1);
      } else { return (version, 0) }
    },
    _ => panic!("Unknown typeid: {}", typeid_bin) 
  }

}

fn as_literal(transmission:  &mut Vec<char>) -> u64 {
  let mut packets = String::new();
  loop {
    let head = transmission.remove(0);
    for _ in 0..4 {
      packets.push(transmission.remove(0));
    }
    if head == '0' { break }
  }
  return u64::from_str_radix(&packets, 2).unwrap();  
}

fn as_operator(transmission:  &mut Vec<char>) -> (u64, Vec<u64>) {
  let length_type = transmission.remove(0); 

  if length_type == '0' {
    let mut total_length = String::new();
    for _ in 0..15 {
      total_length.push(transmission.remove(0));
    }
    let len = u64::from_str_radix(&total_length, 2).unwrap();

    let mut version_sum = 0;
    let mut values = vec!();
    let start = transmission.len();

    loop {
        let (version, value) = parse_bits(transmission);
        version_sum += version;
        values.push(value);

        let now = transmission.len();
        if start - now >= (len as usize) {
            break;
        }
    }
    return (version_sum, values);

  } else {
    let mut total_length = String::new();
    for _ in 0..11 {
      total_length.push(transmission.remove(0));
    }
    let len = u64::from_str_radix(&total_length, 2).unwrap();
    let mut version_sum = 0;
    let mut values = vec!();

    for _ in 0..len {
        let (version, value) = parse_bits(transmission);
        version_sum += version;
        values.push(value);
    }
    return (version_sum, values);
  }
}

fn parse_input() -> Vec<char> {
  let input = std::fs::read_to_string("input.txt").unwrap();
  let mut transmission : Vec<String> = Vec::new();
  input.chars().for_each(|c| {
    match c {
      '0' => transmission.push("0000".to_string()),
      '1' => transmission.push("0001".to_string()),
      '2' => transmission.push("0010".to_string()),
      '3' => transmission.push("0011".to_string()),
      '4' => transmission.push("0100".to_string()),
      '5' => transmission.push("0101".to_string()),
      '6' => transmission.push("0110".to_string()),
      '7' => transmission.push("0111".to_string()),
      '8' => transmission.push("1000".to_string()),
      '9' => transmission.push("1001".to_string()),
      'A' => transmission.push("1010".to_string()),
      'B' => transmission.push("1011".to_string()),
      'C' => transmission.push("1100".to_string()),
      'D' => transmission.push("1101".to_string()),
      'E' => transmission.push("1110".to_string()),
      'F' => transmission.push("1111".to_string()),
      _ => {}
    }
  });
  let mut char_transmission:Vec<char> = Vec::new();
  transmission.iter().for_each(|s| {
    s.chars().for_each(|c| {
      char_transmission.push(c);
    });
  });
  return char_transmission;
}