from ..models import Reservation
from .base_repository import BaseRepository


class ReservationRepository(BaseRepository):
    model = Reservation

    def list(self, status=None, guest_id=None):
        query = Reservation.query
        if status:
            query = query.filter_by(status=status)
        if guest_id:
            query = query.filter_by(guest_id=guest_id)
        return query.order_by(Reservation.check_in).all()
