# Link: https://nss-evening-curriculum.netlify.app/python/class-properties-sensitive-information

class Patient:
    def __init__(self, ssn, dob, insurance, first_name, last_name, address):
        self.__social_security_number = ssn
        self.__date_of_birth = dob
        self.__health_insurance_account_number = insurance
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    # Read-only property for SSN
    @property
    def social_security_number(self):
        return self.__social_security_number

    # Read-only property for DOB
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    # Read-only property for insurance account
    @property
    def health_insurance_account_number(self):
        return self.__health_insurance_account_number

    # Calculated property for full name
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    # Address getter
    @property
    def address(self):
        return self.__address

    # Address setter
    @address.setter
    def address(self, new_address):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            raise TypeError("Address must be a string")
