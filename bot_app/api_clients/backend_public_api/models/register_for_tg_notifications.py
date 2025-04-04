from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterForTgNotifications")


@_attrs_define
class RegisterForTgNotifications:
    """
    Example:
        {'connection_code': 'H$TO53g:O34OJ$GJO£GJR$£OL:RGE', 'tg_full_name': 'John Doe', 'tg_id': 123456789,
            'tg_user_name': '@johndoe'}

    Attributes:
        connection_code (str): Connection code generated by our backend
        tg_id (int): Telegram ID of the user
        tg_full_name (str): Full name of the user
        tg_user_name (Union[None, Unset, str]): Whether the user has a username in Telegram
    """

    connection_code: str
    tg_id: int
    tg_full_name: str
    tg_user_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_code = self.connection_code

        tg_id = self.tg_id

        tg_full_name = self.tg_full_name

        tg_user_name: Union[None, Unset, str]
        if isinstance(self.tg_user_name, Unset):
            tg_user_name = UNSET
        else:
            tg_user_name = self.tg_user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_code": connection_code,
                "tg_id": tg_id,
                "tg_full_name": tg_full_name,
            }
        )
        if tg_user_name is not UNSET:
            field_dict["tg_user_name"] = tg_user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_code = d.pop("connection_code")

        tg_id = d.pop("tg_id")

        tg_full_name = d.pop("tg_full_name")

        def _parse_tg_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tg_user_name = _parse_tg_user_name(d.pop("tg_user_name", UNSET))

        register_for_tg_notifications = cls(
            connection_code=connection_code,
            tg_id=tg_id,
            tg_full_name=tg_full_name,
            tg_user_name=tg_user_name,
        )

        register_for_tg_notifications.additional_properties = d
        return register_for_tg_notifications

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
