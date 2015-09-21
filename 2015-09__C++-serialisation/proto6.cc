AddressBook address_book;

Person* person = address_book.add_person();
person->set_id(id);
person->set_name(name);
if (!email.empty()) {
    person->set_email(email);
}

Person::PhoneNumber* phone_number
    = person->add_phone();
phone_number->set_number(number);
phone_number->set_type(Person::MOBILE);
