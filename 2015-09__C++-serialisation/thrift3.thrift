service Calculator extends shared.SharedService {
   void ping(),
   i32 add(1:i32 num1, 2:i32 num2),
   i32 calculate(1:i32 logid, 2:Work w)
           throws (1:InvalidOperation ouch),

   /**
    * This method has a oneway modifier. That
    * means the client only makes a request and
    * does not listen for any response at
    * all. Oneway methods must be void.
    */
   oneway void zip()
}
