import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceNewsInstance")


@_attrs_define
class ServiceNewsInstance:
    """
    Attributes:
        uuid (UUID): Unique identifier of the service news
        title (str): Title of the service news
        created_at (datetime.datetime): When the service news was created
        label_text (str): Text for the label of the service news
        label_color_hex (str): Color of the label in hex format
        description (Union[None, Unset, str]): Description of the service news
        image_uuid (Union[None, UUID, Unset]): UUID of the image associated with the service news
    """

    uuid: UUID
    title: str
    created_at: datetime.datetime
    label_text: str
    label_color_hex: str
    description: Union[None, Unset, str] = UNSET
    image_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        title = self.title

        created_at = self.created_at.isoformat()

        label_text = self.label_text

        label_color_hex = self.label_color_hex

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        image_uuid: Union[None, Unset, str]
        if isinstance(self.image_uuid, Unset):
            image_uuid = UNSET
        elif isinstance(self.image_uuid, UUID):
            image_uuid = str(self.image_uuid)
        else:
            image_uuid = self.image_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "title": title,
                "created_at": created_at,
                "label_text": label_text,
                "label_color_hex": label_color_hex,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image_uuid is not UNSET:
            field_dict["image_uuid"] = image_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        title = d.pop("title")

        created_at = isoparse(d.pop("created_at"))

        label_text = d.pop("label_text")

        label_color_hex = d.pop("label_color_hex")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_image_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_uuid_type_0 = UUID(data)

                return image_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        image_uuid = _parse_image_uuid(d.pop("image_uuid", UNSET))

        service_news_instance = cls(
            uuid=uuid,
            title=title,
            created_at=created_at,
            label_text=label_text,
            label_color_hex=label_color_hex,
            description=description,
            image_uuid=image_uuid,
        )

        service_news_instance.additional_properties = d
        return service_news_instance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
