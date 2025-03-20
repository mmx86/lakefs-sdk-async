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


from typing import Dict, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr

class Merge(BaseModel):
    """
    Merge
    """
    message: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    strategy: Optional[StrictStr] = Field(None, description="In case of a merge conflict, this option will force the merge process to automatically favor changes from the dest branch ('dest-wins') or from the source branch('source-wins'). In case no selection is made, the merge process will fail in case of a conflict")
    force: Optional[StrictBool] = Field(False, description="Allow merge into a read-only branch or into a branch with the same content")
    allow_empty: Optional[StrictBool] = Field(False, description="Allow merge when the branches have the same content")
    __properties = ["message", "metadata", "strategy", "force", "allow_empty"]

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
    def from_json(cls, json_str: str) -> Merge:
        """Create an instance of Merge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Merge:
        """Create an instance of Merge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Merge.parse_obj(obj)

        _obj = Merge.parse_obj({
            "message": obj.get("message"),
            "metadata": obj.get("metadata"),
            "strategy": obj.get("strategy"),
            "force": obj.get("force") if obj.get("force") is not None else False,
            "allow_empty": obj.get("allow_empty") if obj.get("allow_empty") is not None else False
        })
        return _obj


