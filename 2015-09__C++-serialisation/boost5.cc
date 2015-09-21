// Non-intrusive version.
template<class Archive>
void serialize(Archive & ar, gps_position & g,
               const unsigned int version) {
    ar & g.degrees;
    ar & g.minutes;
    ar & g.seconds;
}
