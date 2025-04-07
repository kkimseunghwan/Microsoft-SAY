

from p02_View import ConsoleScreen
from p02_Doctor import DoctorC

if __name__ == "__main__":
    guest = ConsoleScreen.GetGuestInfo()
    DoctorC.calculBMI(guest)
    DoctorC.GetResult(guest)
    ConsoleScreen.tellResult(guest)
    
    



