User "takes bike" -> main handles -> Service.take_bike() { Station.take_bike(), Client.assign_bike() }
User "returns bike" -> main handles -> Service.return_bike() { Station.return_bike(), Client.clear_bike(), Finance.invoice()}
