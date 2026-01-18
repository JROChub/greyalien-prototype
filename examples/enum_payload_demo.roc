module main

enum Option { None, Some(Int) }

fn main() {
  let value = Some(5);
  let msg = match value {
    Some(5) => { "five"; }
    _ => { "other"; }
  };
  print("value is " + msg);
}
