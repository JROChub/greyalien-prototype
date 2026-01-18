enum Option { None, Some(Int) }

fn main() {
  let x = Some(2);
  let out = match x {
    Some(2) => { "two"; }
    _ => { "no"; }
  };
  print(out);
}
