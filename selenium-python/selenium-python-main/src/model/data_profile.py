from dataclasses import dataclass, field
from typing import Optional

from src.enum.data_profiles_enum.item_type import ItemType
from src.enum.data_profiles_enum.related_data import RelatedData


@dataclass
class DataProfile:
    dataProfileName: str = "Action Implementation By Status"
    itemType: Optional[ItemType] = field(default=None)
    relatedData: Optional[RelatedData] = field(default=None)

    def __eq__(self, other):
        if not isinstance(other, DataProfile):
            return False
        return (self.dataProfileName == other.dataProfileName and
                self.itemType == other.itemType and
                self.relatedData == other.relatedData)

    def __hash__(self):
        return hash((self.dataProfileName, self.itemType, self.relatedData))


# Constructor overload
def create_data_profile(dataProfile: Optional[str] = None) -> DataProfile:
    if dataProfile is not None:
        return DataProfile(dataProfileName=dataProfile)
    return DataProfile()
