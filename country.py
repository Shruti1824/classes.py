class country():
    def acceptcountry(self):
        self.name=(input("Enter country name"))

        def displaycountry(self):
            print("Enter name of country",self.name)

            class state(country):
                def acceptstate(self):
                    self.state(input("enter state name"))

                    def displaystate(self):
                        print("Enter state name",self.state)

                        c=state()
                        c.acceptcountry()
                        c.displaycountry()
                        c.displaystate()
                        c.acceptstate()
