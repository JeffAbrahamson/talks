Work work;
work.op = Operation::DIVIDE;
work.num1 = 1;
work.num2 = 0;

try {
    client.calculate(1, work);
    cout << "Division by zero!" << endl;
} catch (InvalidOperation& io) {
    cout << "InvalidOperation: " << io.why << endl;
    cout << io << endl;  // Same thing.
}
