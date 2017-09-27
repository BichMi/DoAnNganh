from django.db import models
from django.contrib.auth.models import AbstractUser

"""
    UserType/Loại User
    Documents : id
                type_user_name: Khách Hàng/admin/staff
"""


class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)

    def __str__(self):
        return ("%s" % (self.user_type_name))


""" 
    User
    Documents : id
                username: Bich Mi
                pass_word: 1234abcd
                frist_name: Mi
                last_name: Nguyễn Thị Bích
                date_of_birth: 01/04/1995
                sex : nữ
                nationality: Viet Nam
                certificate_of_identity_card: 2854964325
                type_user : Khach Hang
                contact_telephone: 0934489100
                email:nguyenthibichmi@gmail.com
                date_joined:29/08/2017
                
"""


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=100, null=True)
    certificate_of_identity_card = models.IntegerField(null=True)
    contact_telephone = models.IntegerField(null=True)
    user_type = models.ForeignKey(UserType, default=1)

    def __str__(self):
        return ("%s - User Name:%s \t Ho va ten: %s %s -Ngay sinh: %s - CMND: %d - Gioi tinh: %s - Quoc tich: %s - Phone: %s - Email: %s - Loai User: %s " % (
            self.pk, self.username, self.first_name, self.last_name, self.date_of_birth,
            self.certificate_of_identity_card,
            self.sex, self.nationality, self.contact_telephone, self.email, self.type_user.user_type_name))


"""
    SeatType
    Documents : id
                seat_class_name : phổ thông, phổ thông đặc biet, thương gia
                seat_class_price 
"""


class SeatType(models.Model):
    ECONOMY, PREMIUM_ECONOMY, BUSINESS = range(3)
    SEATCLASS = ((ECONOMY, "Econnomy"), (PREMIUM_ECONOMY, "Premium Economy"), (BUSINESS, "Business"))
    seat_class_name = models.SmallIntegerField(choices=SEATCLASS)
    seat_class_price = models.FloatField(null=True, blank=True, default=0.00)

    def __str__(self):
        return ("%s - %s - %f" % (self.pk, self.seat_class_name, self.seat_class_price))


"""
    Airport/sân bay
    Documents: id
                airport_name : Tân Sơn nhất
                airport_address
"""


class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    airport_address = models.CharField(max_length=200)

    def __str__(self):
        return ("%s - %s - %s" % (self.pk, self.airport_name, self.airport_address))


"""
    TicketType/loại vé
    Documents : id
                ticket_type_name : nguoi lon(>12 tuoi)/ tre em(2 -> 12 tuoi)/ em be(<2 tuoi)
                ticket_type_price : 

"""


class TicketType(models.Model):
    ADULTS, CHILDREN, BABY = range(3)
    TYPETICKET = ((ADULTS, "Adults"), (CHILDREN, "Childrent"), (BABY, "Baby"))
    ticket_type_name = models.SmallIntegerField(choices=TYPETICKET)
    ticket_type_price = models.FloatField(null=True, blank=True, default=0.00)

    def __str__(self):
        return ("%s - %d - %f" % (self.pk, self.type_ticket_name, self.ticket_type_price))


"""
    Airline/hãng hàng không
    Documents:  id
                airline_name : jestar
                airline_price
"""


class Airline(models.Model):
    airline_name = models.CharField(max_length=50)
    airline_price = models.FloatField(null=True, blank=True, default=0.00)

    def __str__(self):
        return ("%s - %s - %f " % (self.pk, self.airline_name, self.airline_price))


"""
    Planes/máy bay
    Documents:  id
                planes_name : JT01
                airline_id : Jestar
                manufacturer : nhà sản xuất
                numbers_of_seats_1  : 15
                numbers_of_seats_2 : 30
                payload_allowed : 60T
                gate_number : 6

"""


class Plane(models.Model):
    planes_name = models.CharField(max_length=50, null=True)
    airline = models.ForeignKey(Airline)
    manufacturer = models.CharField(max_length=100, null=True)
    numbers_of_seats_1 = models.IntegerField(null=True)
    numbers_of_seats_2 = models.IntegerField(null=True)
    payload_allowed = models.IntegerField(null=True)
    gate_number = models.IntegerField(null=True)

    def __str__(self):
        return ("%s - %s - %s - %s - %d - %d - %d - %d" % (
            self.pk, self.planes_name, self.airline, self.manufacturer, self.numbers_of_seats_1,
            self.numbers_of_seats_2, self.payload_allowed, self.gate_number))


"""
    FlightRoute/ tuyến bay
    Documents : id
                flight_route_name:HCM-HN
                from_airport: Tan Son nhat
                to_airport: Noi Bai
                distance : 3000 km
"""


class FlightRoute(models.Model):
    flight_route_name = models.CharField(max_length=255)
    from_airport = models.ForeignKey(Airport, related_name='from_airport')
    to_airport = models.ForeignKey(Airport, related_name='to_airport')
    distance = models.IntegerField()

    def __str__(self):
        return (
        "%s - %s - %s - %s - %d" % (self.pk, self.flight_route_name, self.from_airport, self.to_airport, self.distance))


"""	
    Flight/chuyến bay
    Documents:  id
                flight_route_id: mã tuyến bay
                planes_id: mã máy bay
                from_location : TPHCM
                to_location : Ha Noi
                departure_time: 10:30:00 29/08/2017
                flight_time:  02:10:00
                airport_mid/ Sân bay trung gian : Đà Nẵng
"""


class Flight(models.Model):
    flight_route = models.ForeignKey(FlightRoute)
    planes = models.ForeignKey(Plane)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField(null=True, blank=True)
    flight_time = models.TimeField()
    airport_mid = models.ForeignKey(Airport)
    time_to_airport_mid = models.TimeField(null=True)
    time_from_airport_mid = models.TimeField(null=True)

    def __str__(self):
        return ("%s - %s - %s - %s - %s - %s - %s - %s" % (
            self.pk, self.from_location, self.to_location, self.departure_time, self.flight_time, self.airport_mid,
            self.time_to_airport_mid, self.time_from_airport_mid))


"""
    BookTicket/đặt vé máy bay
    Documents : id
                user_id : 01
                flight_id:
"""


class TicketBook(models.Model):
    user = models.ForeignKey(User, help_text='Khách Hàng')
    flight = models.ForeignKey(Flight)

    def __str__(self):
        return ("%s - ID User book: %s - ID Flight: %s" % (
            self.pk, self.user, self.flight))


"""
    BookInfo
    Documents:  id
                book_id: đặt vé id
                type_seat_id /loại ghế id
                type_ticket_id / loai vé id
                airline_id / hãng hàng không
                price_ticket_book: use algorithm
                seat_number : 03

"""


class BookInfo(models.Model):
    book = models.ForeignKey(TicketBook)
    seat_type = models.ForeignKey(SeatType)
    ticket_type = models.ForeignKey(TicketType)
    airline = models.ForeignKey(Airline)
    ticket_book_price = models.FloatField(null=True, blank=True, default=0.00)
    seat_number = models.IntegerField()

    def __str__(self):
        return ("%s -%f - %d" % (self.pk, self.ticket_book_price, self.seat_number))


"""
    số ghế ngồi của từng hạng ghế  = số vé đã đặt của từng hạng ghế
    
"""