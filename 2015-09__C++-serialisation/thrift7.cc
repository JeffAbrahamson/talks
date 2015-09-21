int main() {
  boost::shared_ptr<TProtocolFactory>
          protocolFactory(
              new TBinaryProtocolFactory());
  boost::shared_ptr<CalculatorHandler>
          handler(new CalculatorHandler());
  boost::shared_ptr<TProcessor> processor(
      new CalculatorProcessor(handler));
  boost::shared_ptr<TServerTransport>
          serverTransport(new TServerSocket(9090));
  boost::shared_ptr<TTransportFactory>
          transportFactory(
              new TBufferedTransportFactory());

  TSimpleServer server(processor, serverTransport,
                       transportFactory,
                       protocolFactory);
