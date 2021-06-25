from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from featureflags.models import UNSET, Unset

if TYPE_CHECKING:
    from .clause import Clause, Clauses

from .tag import Tag
from .target import Target

T = TypeVar("T", bound="Segment")


@attr.s(auto_attribs=True)
class Segment(object):
    identifier: str
    name: str
    environment: Union[Unset, str] = UNSET
    tags: Union[Unset, List[Tag]] = UNSET
    included: Union[Unset, List[Target]] = UNSET
    excluded: Union[Unset, List[Target]] = UNSET
    rules: Union[Unset, 'Clauses'] = UNSET
    created_at: Union[Unset, int] = UNSET
    modified_at: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        name = self.name
        environment = self.environment
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        included: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()

                included.append(included_item)

        excluded: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = []
            for excluded_item_data in self.excluded:
                excluded_item = excluded_item_data.to_dict()

                excluded.append(excluded_item)

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        created_at = self.created_at
        modified_at = self.modified_at
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment
        if tags is not UNSET:
            field_dict["tags"] = tags
        if included is not UNSET:
            field_dict["included"] = included
        if excluded is not UNSET:
            field_dict["excluded"] = excluded
        if rules is not UNSET:
            field_dict["rules"] = rules
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        name = d.pop("name")

        environment = d.pop("environment", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = Target.from_dict(included_item_data)

            included.append(included_item)

        excluded = []
        _excluded = d.pop("excluded", UNSET)
        for excluded_item_data in _excluded or []:
            excluded_item = Target.from_dict(excluded_item_data)

            excluded.append(excluded_item)

        rules: Clauses = Clauses()
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = Clause.from_dict(rules_item_data)

            rules.append(rules_item)

        created_at = d.pop("createdAt", UNSET)

        modified_at = d.pop("modifiedAt", UNSET)

        version = d.pop("version", UNSET)

        segment = cls(
            identifier=identifier,
            name=name,
            environment=environment,
            tags=tags,
            included=included,
            excluded=excluded,
            rules=rules,
            created_at=created_at,
            modified_at=modified_at,
            version=version,
        )

        segment.additional_properties = d
        return segment

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


class Segments(Dict[str, Segment]):
    def evaluate(self, target: Target) -> bool:
        return True