from dataclasses import dataclass
from typing import Optional

from src.enum.panel_enum.filters_enum.and_or import AndOr
from src.enum.panel_enum.filters_enum.field import Field
from src.enum.panel_enum.filters_enum.operator import Operators


@dataclass
class Filters:
    andOr: Optional[AndOr] = None
    field: Optional[Field] = None
    operators: Optional[Operators] = None
    value: Optional[str] = None

    def __str__(self):
        return f"Filters(andOr={self.andOr}, field={self.field}, operators={self.operators}, value={self.value})"
