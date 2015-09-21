boost::shared_ptr<TTransport> socket(
    new TSocket("localhost", 9090));
boost::shared_ptr<TTransport> transport(
    new TBufferedTransport(socket));
boost::shared_ptr<TProtocol> protocol(
    new TBinaryProtocol(transport));
CalculatorClient client(protocol);

