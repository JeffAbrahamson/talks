const map<string,string> MAPCONSTANT =
    {'hello':'world',
     'goodnight':'moon'}
    
enum Operation {
  ADD = 1,
  // ...
}

struct Work {
  1: i32 num1 = 0,
  2: i32 num2,
  3: Operation op,
  4: optional string comment,
}
