from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanResponse")


@_attrs_define
class SubscriptionPlanResponse:
    """Schema for subscription plan response data.

    Example:
        {'agents_quantity': 1, 'by_default': True, 'contacts_month_limit': 150, 'disk_space_gb': 1,
            'integrations_quantity': 1, 'is_active': True, 'managers_quantity': 1, 'note': 'Базовий план для нових
            користувачів', 'price_uah_monthly': 0, 'price_uah_yearly': 0, 'projects_quantity': 1, 'title': 'Безкоштовний',
            'uuid': '123e4567-e89b-12d3-a456-426614174000'}

    Attributes:
        uuid (UUID): Unique identifier of the subscription plan
        title (str): Title of the subscription plan
        price_uah_monthly (int): Monthly price in UAH
        projects_quantity (int): Number of projects allowed
        managers_quantity (int): Number of managers allowed
        agents_quantity (int): Number of agents allowed
        disk_space_gb (int): Disk space limit in GB
        integrations_quantity (int): Integrations count
        contacts_month_limit (int): Contacts limit per month
        is_active (bool): Whether the subscription plan is active
        by_default (bool): Whether the subscription plan is the default plan
        note (Union[None, Unset, str]): Subscription plan note
        price_uah_yearly (Union[None, Unset, int]): Yearly price in UAH
    """

    uuid: UUID
    title: str
    price_uah_monthly: int
    projects_quantity: int
    managers_quantity: int
    agents_quantity: int
    disk_space_gb: int
    integrations_quantity: int
    contacts_month_limit: int
    is_active: bool
    by_default: bool
    note: Union[None, Unset, str] = UNSET
    price_uah_yearly: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        title = self.title

        price_uah_monthly = self.price_uah_monthly

        projects_quantity = self.projects_quantity

        managers_quantity = self.managers_quantity

        agents_quantity = self.agents_quantity

        disk_space_gb = self.disk_space_gb

        integrations_quantity = self.integrations_quantity

        contacts_month_limit = self.contacts_month_limit

        is_active = self.is_active

        by_default = self.by_default

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        price_uah_yearly: Union[None, Unset, int]
        if isinstance(self.price_uah_yearly, Unset):
            price_uah_yearly = UNSET
        else:
            price_uah_yearly = self.price_uah_yearly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "title": title,
                "price_uah_monthly": price_uah_monthly,
                "projects_quantity": projects_quantity,
                "managers_quantity": managers_quantity,
                "agents_quantity": agents_quantity,
                "disk_space_gb": disk_space_gb,
                "integrations_quantity": integrations_quantity,
                "contacts_month_limit": contacts_month_limit,
                "is_active": is_active,
                "by_default": by_default,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if price_uah_yearly is not UNSET:
            field_dict["price_uah_yearly"] = price_uah_yearly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        title = d.pop("title")

        price_uah_monthly = d.pop("price_uah_monthly")

        projects_quantity = d.pop("projects_quantity")

        managers_quantity = d.pop("managers_quantity")

        agents_quantity = d.pop("agents_quantity")

        disk_space_gb = d.pop("disk_space_gb")

        integrations_quantity = d.pop("integrations_quantity")

        contacts_month_limit = d.pop("contacts_month_limit")

        is_active = d.pop("is_active")

        by_default = d.pop("by_default")

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_price_uah_yearly(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price_uah_yearly = _parse_price_uah_yearly(d.pop("price_uah_yearly", UNSET))

        subscription_plan_response = cls(
            uuid=uuid,
            title=title,
            price_uah_monthly=price_uah_monthly,
            projects_quantity=projects_quantity,
            managers_quantity=managers_quantity,
            agents_quantity=agents_quantity,
            disk_space_gb=disk_space_gb,
            integrations_quantity=integrations_quantity,
            contacts_month_limit=contacts_month_limit,
            is_active=is_active,
            by_default=by_default,
            note=note,
            price_uah_yearly=price_uah_yearly,
        )

        subscription_plan_response.additional_properties = d
        return subscription_plan_response

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
