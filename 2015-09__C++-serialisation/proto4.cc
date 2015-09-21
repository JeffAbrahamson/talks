//Checks if all the required fields have been set.
bool IsInitialized() const;

// Returns a human-readable representation of the
// message, particularly useful for debugging.
string DebugString() const;

// Overwrites the message with the given message's
// values.
void CopyFrom(const Person& from);

// Clears all the elements back to the empty state.
void Clear();