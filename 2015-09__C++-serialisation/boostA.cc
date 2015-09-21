// STL.
#include <boost/serialization/list.hpp>

class bus_route {
    friend class boost::serialization::access;
    std::list<bus_stop*> stops;
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        ar & stops;
    }
