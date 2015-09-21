// Arrays.
class bus_route {
    friend class boost::serialization::access;
    bus_stop* stops[10];
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        ar & stops;
    }
