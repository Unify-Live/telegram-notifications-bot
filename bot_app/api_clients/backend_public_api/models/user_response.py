from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """Schema for user response data.

    Example:
        {'avatar_uuid': '123e4567-e89b-12d3-a456-426614174000', 'email': 'user@example.com', 'first_name': 'Bob',
            'last_name': 'Klop', 'mobile_number': '+1234567890', 'policy_accepted': True, 'uuid':
            '123e4567-e89b-12d3-a456-426614174000'}

    Attributes:
        uuid (UUID): Unique identifier of the user
        email (str): User's email address
        timezone_uuid (Union[Unset, UUID]): User's timezone
        mobile_number (Union[None, Unset, str]): User's mobile phone number
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        policy_accepted (Union[Unset, bool]):
        avatar_uuid (Union[None, UUID, Unset]):
    """

    uuid: UUID
    email: str
    timezone_uuid: Union[Unset, UUID] = UNSET
    mobile_number: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    policy_accepted: Union[Unset, bool] = UNSET
    avatar_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        email = self.email

        timezone_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.timezone_uuid, Unset):
            timezone_uuid = str(self.timezone_uuid)

        mobile_number: Union[None, Unset, str]
        if isinstance(self.mobile_number, Unset):
            mobile_number = UNSET
        else:
            mobile_number = self.mobile_number

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        policy_accepted = self.policy_accepted

        avatar_uuid: Union[None, Unset, str]
        if isinstance(self.avatar_uuid, Unset):
            avatar_uuid = UNSET
        elif isinstance(self.avatar_uuid, UUID):
            avatar_uuid = str(self.avatar_uuid)
        else:
            avatar_uuid = self.avatar_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "email": email,
            }
        )
        if timezone_uuid is not UNSET:
            field_dict["timezone_uuid"] = timezone_uuid
        if mobile_number is not UNSET:
            field_dict["mobile_number"] = mobile_number
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if policy_accepted is not UNSET:
            field_dict["policy_accepted"] = policy_accepted
        if avatar_uuid is not UNSET:
            field_dict["avatar_uuid"] = avatar_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        email = d.pop("email")

        _timezone_uuid = d.pop("timezone_uuid", UNSET)
        timezone_uuid: Union[Unset, UUID]
        if isinstance(_timezone_uuid, Unset):
            timezone_uuid = UNSET
        else:
            timezone_uuid = UUID(_timezone_uuid)

        def _parse_mobile_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile_number = _parse_mobile_number(d.pop("mobile_number", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        policy_accepted = d.pop("policy_accepted", UNSET)

        def _parse_avatar_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                avatar_uuid_type_0 = UUID(data)

                return avatar_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        avatar_uuid = _parse_avatar_uuid(d.pop("avatar_uuid", UNSET))

        user_response = cls(
            uuid=uuid,
            email=email,
            timezone_uuid=timezone_uuid,
            mobile_number=mobile_number,
            first_name=first_name,
            last_name=last_name,
            policy_accepted=policy_accepted,
            avatar_uuid=avatar_uuid,
        )

        user_response.additional_properties = d
        return user_response

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
