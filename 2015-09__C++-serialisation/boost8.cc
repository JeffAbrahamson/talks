// Pointers.
class bus_route {
    friend class boost::serialization::access;
    bus_stop* stops[10];
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version)     {
        for(int i = 0; i < 10; ++i) {
            ar & stops[i];
        }
    }
