boost::shared_ptr<TFileTransport>
    transport(new TFileTransport(filename));
boost::shared_ptr<TBinaryProtocol>
    protocol(new TBinaryProtocol(transport));
myObj.write(protocol.get());
