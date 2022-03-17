from bs4 import BeautifulSoup
import requests
from details import details
counter = 0
for detail in details:
    
    fullname = detail["fullName"].strip()
    firstname = fullname.split(' ')[0]
    lastname = fullname.split(' ')[1] if len(fullname.split(' ')) > 1 else firstname

    phone = f"0{detail['phoneNumber']}"
    # print(f'{firstname} {lastname}\n{phone}\n\n')

    payload = {"firstname":firstname, "lastname": lastname, "ccode": "+234","phone": phone,"zone": "2ND TIER CHURCH GROUP 3","country": "Nigeria", "state": "Edo","city": "Benin","need_healing2":"on"}
    r = requests.post("https://healingstreams.tv/3days/online_reg.php?r=2TCG3", data=payload)

    soup = BeautifulSoup(r.text, "html.parser")
    try:
        msg=soup.select_one(".justify-content-center").select_one(".col-lg-7").select_one("h4").find("b").text
        if msg=="IMPORTANT ACTION TO TAKE":
            msg="done..."
            counter += 1
        print(fullname+": "+msg)
    except:
        try:
            msg=soup.select_one(".justify-content-center").select_one(".col-lg-7").select_one("h6").contents[0].strip()
            print(fullname+": "+msg)
        except:
            print("An error occurred...")


print("TOTAL DONE : "+str(counter))
