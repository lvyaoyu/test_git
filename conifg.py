# -*- coding: utf-8 -*-
# @Time : 2022-03-08 12:08 
# @Author : YD


from pydantic import BaseModel


class _Setting(BaseModel):
    branch_name = 'main'
    update_time = '2022-03-08 12:11'


setting = _Setting()

__all__ = ['setting']
