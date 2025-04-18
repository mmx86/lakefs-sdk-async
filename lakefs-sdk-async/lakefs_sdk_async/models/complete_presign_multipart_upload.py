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


from typing import Dict, List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist
from lakefs_sdk_async.models.upload_part import UploadPart

class CompletePresignMultipartUpload(BaseModel):
    """
    CompletePresignMultipartUpload
    """
    physical_address: StrictStr = Field(...)
    parts: conlist(UploadPart) = Field(..., description="List of uploaded parts, should be ordered by ascending part number")
    user_metadata: Optional[Dict[str, StrictStr]] = None
    content_type: Optional[StrictStr] = Field(None, description="Object media type")
    __properties = ["physical_address", "parts", "user_metadata", "content_type"]

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
    def from_json(cls, json_str: str) -> CompletePresignMultipartUpload:
        """Create an instance of CompletePresignMultipartUpload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item in self.parts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompletePresignMultipartUpload:
        """Create an instance of CompletePresignMultipartUpload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompletePresignMultipartUpload.parse_obj(obj)

        _obj = CompletePresignMultipartUpload.parse_obj({
            "physical_address": obj.get("physical_address"),
            "parts": [UploadPart.from_dict(_item) for _item in obj.get("parts")] if obj.get("parts") is not None else None,
            "user_metadata": obj.get("user_metadata"),
            "content_type": obj.get("content_type")
        })
        return _obj


