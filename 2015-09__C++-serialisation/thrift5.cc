transport->open();

client.ping();
cout << "1 + 1 = " << client.add(1, 1) << endl;
