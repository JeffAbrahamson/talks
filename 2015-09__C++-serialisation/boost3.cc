class gps_position {
  private:
    friend class boost::serialization::access;
    // When the class Archive corresponds to an
    // output archive, the & operator is defined
    // similar to <<.  Likewise, when the class
    // Archive is a type of input archive the &
    // operator is defined similar to >>.
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        ar & degrees;
        ar & minutes;
        ar & seconds;
    }
    int degrees, minutes;
    float seconds;
