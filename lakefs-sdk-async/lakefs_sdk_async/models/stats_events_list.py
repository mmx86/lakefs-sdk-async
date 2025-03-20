# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from lakefs_sdk_async.models.stats_event import StatsEvent

class StatsEventsList(BaseModel):
    """
    StatsEventsList
    """
    events: conlist(StatsEvent) = Field(...)
    __properties = ["events"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StatsEventsList:
        """Create an instance of StatsEventsList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatsEventsList:
        """Create an instance of StatsEventsList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatsEventsList.parse_obj(obj)

        _obj = StatsEventsList.parse_obj({
            "events": [StatsEvent.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None
        })
        return _obj


