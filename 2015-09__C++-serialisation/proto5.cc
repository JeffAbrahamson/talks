// Serializes the message and stores the bytes in
// the given string. Note that the bytes are binary,
// not text; we only use the string class as a
// convenient container.
bool SerializeToString(string* output) const;

// Parses a message from the given string.
bool ParseFromString(const string& data);

// Writes the message to the given C++ ostream.
bool SerializeToOstream(ostream* output) const;

// Parses a message from the given C++ istream. 
bool ParseFromIstream(istream* input);