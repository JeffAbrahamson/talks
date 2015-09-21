// Serializable members.
class bus_stop {
    friend class boost::serialization::access;
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        ar & latitude;
        ar & longitude;
    }
    gps_position latitude;
    gps_position longitude;
