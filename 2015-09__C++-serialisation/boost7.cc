// Derived classes.
#include <boost/serialization/base_object.hpp>

class bus_stop_corner : public bus_stop {
    friend class boost::serialization::access;
    template<class Archive>
    void serialize(Archive & ar,
                   const unsigned int version) {
        // serialize base class information
        ar & boost::serialization::base_object<
            bus_stop>(*this);
        ar & street1;
        ar & street2;
    }
    std::string street1;
    std::string street2;
