// Versioning (1).
#include <boost/serialization/list.hpp>
#include <boost/serialization/string.hpp>

class bus_route {
    friend class boost::serialization::access;
    std::list<bus_stop*> stops;
    std::string driver_name;
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        ar & driver_name;  // !!
        ar & stops;
    }
