exception InvalidOperation {
  1: i32 whatOp,
  2: string why
}

struct SharedStruct {
  1: i32 key
  2: string value
}

service SharedService {
  SharedStruct getStruct(1: i32 key)
}
