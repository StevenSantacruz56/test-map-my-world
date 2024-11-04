from decimal import Decimal
from sqlalchemy import Numeric, TypeDecorator


class FloatDecimal(TypeDecorator):
    impl = Numeric
    cache_ok = True

    def __init__(self, precision=10, scale=4, asdecimal=True, **kwargs):
        self.precision = precision
        self.scale = scale
        self.asdecimal = asdecimal
        super().__init__(precision=self.precision, scale=self.scale, asdecimal=self.asdecimal, **kwargs)

    def process_bind_param(self, value, dialect):
        if value is not None:
            return Decimal(value).quantize(Decimal('0' * (self.scale-1) + '.1'))
        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            value = float(value)
        return value
