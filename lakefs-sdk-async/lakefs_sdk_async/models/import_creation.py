# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictBool, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, conlist
from lakefs_sdk_async.models.commit_creation import CommitCreation
from lakefs_sdk_async.models.import_location import ImportLocation

class ImportCreation(BaseModel):
    """
    ImportCreation
    """
    paths: conlist(ImportLocation) = Field(...)
    commit: CommitCreation = Field(...)
    force: Optional[StrictBool] = False
    __properties = ["paths", "commit", "force"]

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
    def from_json(cls, json_str: str) -> ImportCreation:
        """Create an instance of ImportCreation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in paths (list)
        _items = []
        if self.paths:
            for _item in self.paths:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paths'] = _items
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImportCreation:
        """Create an instance of ImportCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImportCreation.parse_obj(obj)

        _obj = ImportCreation.parse_obj({
            "paths": [ImportLocation.from_dict(_item) for _item in obj.get("paths")] if obj.get("paths") is not None else None,
            "commit": CommitCreation.from_dict(obj.get("commit")) if obj.get("commit") is not None else None,
            "force": obj.get("force") if obj.get("force") is not None else False
        })
        return _obj


