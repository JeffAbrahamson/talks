int main() {
    std::ofstream ofs("filename");
    const gps_position g(35, 59, 24.567f);

    {
        boost::archive::text_oarchive oa(ofs);
        oa << g;
    }

    gps_position newg;  // Later...
    {
        std::ifstream ifs("filename");
        boost::archive::text_iarchive ia(ifs);
        ia >> newg;
    }
    return 0;
}
