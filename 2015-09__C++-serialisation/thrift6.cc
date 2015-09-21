SharedStruct ss;
client.getStruct(ss, 1);
cout << "Received log: " << ss << endl;

transport->close();
