from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BillingFaqInstance")


@_attrs_define
class BillingFaqInstance:
    """
    Attributes:
        uuid (UUID): Unique identifier of the timezone
        question (str): Question of the FAQ
        answer (str): Answer of the FAQ
        enabled (bool): Whether the FAQ is active
        priority (int): Priority of the FAQ
    """

    uuid: UUID
    question: str
    answer: str
    enabled: bool
    priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        question = self.question

        answer = self.answer

        enabled = self.enabled

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "question": question,
                "answer": answer,
                "enabled": enabled,
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        question = d.pop("question")

        answer = d.pop("answer")

        enabled = d.pop("enabled")

        priority = d.pop("priority")

        billing_faq_instance = cls(
            uuid=uuid,
            question=question,
            answer=answer,
            enabled=enabled,
            priority=priority,
        )

        billing_faq_instance.additional_properties = d
        return billing_faq_instance

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
